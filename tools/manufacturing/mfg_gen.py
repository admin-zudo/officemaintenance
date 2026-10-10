"""Generate the Manufacturing section. Run from the repo root, then run tools/build.py:

    python tools/manufacturing/mfg_gen.py     # pages under /manufacturing/ and their figures
    python tools/build.py                     # shared header/footer, CSS bundle, sitemap, link check

Content lives in the content_*.py files next to this script. Figures are described in those files with
figs.fig(...) and rendered to Asset/img/manufacturing/. Case studies are illustrative reference
implementations, not client projects, and every app screen is a concept mockup; the templates say so.
"""
import html, json, os, re, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import figs  # noqa: E402

SITE = 'https://zudoworks.com'
ROOT = figs.ROOT
BASE = '/manufacturing/'

SUBNAV = [(BASE, 'Overview'), (BASE + 'zoho-implementation/', 'Zoho implementation'), (BASE + 'ai-automation/', 'AI automation'),
          (BASE + 'workflows/', 'Workflows'), (BASE + 'guides/', 'Guides'), (BASE + 'case-studies/', 'Case studies')]

ORG = {"@type": "Organization", "@id": SITE + "/#organization", "name": "Zudo Works", "url": SITE + "/",
       "logo": {"@type": "ImageObject", "url": SITE + "/Asset/brand/zudo-works-logo.svg"}}
AUTHORS = {
    'arun': dict(
        name='Arunkumar V', meta='Arunkumar V',
        byline='By <a href="/about/#leadership" rel="author">Arunkumar V</a>, CTO at Zudo Works',
        avatar='<img class="author-avatar" src="/Asset/img/team/arunkumar-v-avatar.webp" alt="Arunkumar V" width="44" height="44">',
        avatar_lg='<img class="author-avatar author-avatar--lg" src="/Asset/img/team/arunkumar-v-avatar.webp" alt="Arunkumar V" width="64" height="64" loading="lazy">',
        box_name='<a href="/about/#leadership">Arunkumar V</a>, Chief Technology Officer, Zudo Works',
        box='Arunkumar builds Zoho Creator apps, Zoho CRM systems, Deluge automations and integrations for businesses in the US, UK, Australia, New Zealand and India. He received the &ldquo;Master of Creator&rdquo; award at the Zoho Creator Partner Hackathon 2025.',
        links='<a href="https://www.linkedin.com/in/arunkumar-v-5509aa1aa/" target="_blank" rel="noopener">LinkedIn</a><a href="/about/#leadership">About Arunkumar</a>',
        ld={"@type": "Person", "@id": SITE + "/#arunkumar-v", "name": "Arunkumar V", "jobTitle": "Chief Technology Officer",
            "image": SITE + "/Asset/img/team/arunkumar-v.jpg", "url": SITE + "/about/#leadership", "worksFor": {"@id": SITE + "/#organization"},
            "sameAs": ["https://www.linkedin.com/in/arunkumar-v-5509aa1aa/"]}),
    'team': dict(
        name='Zudo Works development team', meta='Zudo Works development team',
        byline='By the <a href="/about/">Zudo Works development team</a>',
        avatar='<img class="author-avatar author-avatar--team" src="/Asset/brand/zudo-works-logo.svg" alt="Zudo Works" width="44" height="44">',
        avatar_lg='<img class="author-avatar author-avatar--lg author-avatar--team" src="/Asset/brand/zudo-works-logo.svg" alt="Zudo Works" width="64" height="64" loading="lazy">',
        box_name='The <a href="/about/">Zudo Works development team</a>',
        box='Zudo Works builds Zoho Creator apps, Zoho CRM systems, Deluge automations and integrations. This piece was written by the developers who design and build them, and reviewed by our CTO, Arunkumar V.',
        links='<a href="/about/">About Zudo Works</a><a href="/work/">Project experience</a>',
        ld=ORG),
}


def plain(t): return html.unescape(re.sub(r'<[^>]+>', ' ', t))
def esc(t): return html.escape(plain(t).strip())
def words(*parts): return len(' '.join(plain(p) for p in parts).split())
def nice(d): return date(*map(int, d.split('-'))).strftime('%d %B %Y').lstrip('0')
def ld(o): return '  <script type="application/ld+json">\n' + json.dumps(o, indent=2, ensure_ascii=False) + '\n  </script>'


def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + r} for i, (r, n) in enumerate(trail)]}


def crumbs(trail):
    out = []
    for r, n in trail[:-1]:
        out.append(f'<a href="{r}">{n}</a>\n            <span class="breadcrumb-sep" aria-hidden="true">/</span>')
    out.append(f'<span class="breadcrumb-current" aria-current="page">{trail[-1][1]}</span>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">\n            ' + '\n            '.join(out) + '\n          </nav>'


def subnav(route):
    cur = max((r for r, _ in SUBNAV if route.startswith(r)), key=len)
    items = ''.join(f'<li><a href="{r}"{" aria-current=\"page\"" if r == cur and r == route else ""}>{n}</a></li>' for r, n in SUBNAV)
    return f'    <nav class="mfg-subnav" aria-label="Manufacturing section"><div class="container"><ul>{items}</ul></div></nav>'


def faq_html(faqs):
    if not faqs: return ''
    out = []
    for q, a in faqs:
        out.append(f'''          <div class="faq-item">
            <button type="button" class="faq-question" aria-expanded="false">
              <span>{html.escape(q, quote=False)}</span>
              <svg class="faq-toggle" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <p>{html.escape(a, quote=False)}</p>
            </div>
          </div>''')
    return '        <div class="faq-list">\n' + '\n'.join(out) + '\n        </div>'


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def shell(route, title, desc, og_image, og_type, blocks, main, author=None, extra_meta=''):
    t, d = html.escape(title), html.escape(desc)
    assert len(title) <= 62, f'title too long ({len(title)}): {title}'
    assert len(desc) <= 162, f'description too long ({len(desc)}): {route}'
    am = f'  <meta name="author" content="{author}">\n' if author else ''
    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <!-- @head -->
    <!-- @/head -->

  <title>{t}</title>
  <meta name="description" content="{d}">
{am}  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:url" content="{SITE}{route}">
  <meta property="og:image" content="{SITE}{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Zudo Works">
  <meta property="og:locale" content="en_US">
{extra_meta}  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{SITE}{og_image}">
{chr(10).join(blocks)}
</head>

<body>
    <!-- @header -->
    <!-- @/header -->

  <main id="main-content">
{main}
  </main>

    <!-- @footer -->
    <!-- @/footer -->
</body>

</html>
'''


def cta(title, text, b1=('Book a Discovery Call', '/contact/'), b2=('See How We Price', '/pricing/')):
    boo = ' data-booking' if b1[1] == '/contact/' else ''
    return f'''    <section class="cta-banner">
      <div class="container">
        <h2>{title}</h2>
        <p>{text}</p>
        <div class="btn-group justify-center">
          <a href="{b1[1]}" class="btn btn-white btn-lg"{boo}>{b1[0]}</a>
          <a href="{b2[1]}" class="btn btn-outline-white btn-lg">{b2[0]}</a>
        </div>
      </div>
    </section>'''


# ------------------------------------------------------------------ cards
def item_route(it): return BASE + ('case-studies/' if it['type'] == 'case' else 'guides/') + it['slug'] + '/'


def card(it, level='h3'):
    au = AUTHORS[it['author']]['name']
    meta = f'<span class="mfg-card-author">{au}</span> &middot; {read_time(it)} min read'
    return f'''          <article class="post-card">
            <a class="post-card-image" href="{item_route(it)}" tabindex="-1" aria-hidden="true">
              <img src="/Asset/img/manufacturing/{it['slug']}.webp" alt="{html.escape(it['hero_alt'])}" width="1200" height="675" loading="lazy">
            </a>
            <div class="post-card-body">
              <p class="post-card-category">{it['category']}</p>
              <{level}><a href="{item_route(it)}">{it['title']}</a></{level}>
              <p class="post-card-excerpt">{it['desc']}</p>
              <p class="post-card-meta">{meta}</p>
            </div>
          </article>'''


def read_time(it):
    body = it.get('body') or ' '.join(s[2] for s in it['sections'])
    return max(3, round(words(body, ' '.join(q + ' ' + a for q, a in it.get('faqs', []))) / 220))


def toc_items(body):
    return re.findall(r'<h2[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', body, flags=re.S)


def sources_html(srcs):
    if not srcs: return ''
    li = '\n'.join(f'              <li><a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a></li>' for t, u in srcs)
    return f'''          <section class="mfg-sources" aria-label="Sources">
            <h2 id="sources">Sources</h2>
            <p>Product capabilities change. We checked these pages in October 2026; confirm anything you plan around.</p>
            <ol>
{li}
            </ol>
          </section>'''


def author_box(key):
    a = AUTHORS[key]
    return f'''          <aside class="author-box" aria-label="About the author">
            {a['avatar_lg']}
            <div>
              <p class="author-box-label">Written by</p>
              <p class="author-box-name">{a['box_name']}</p>
              <p>{a['box']}</p>
              <p class="author-box-links">{a['links']}</p>
            </div>
          </aside>'''


def facts_dl(facts):
    if not facts: return ''
    return '<dl class="mfg-facts">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in facts) + '</dl>'


def related_section(items, title='Related guides and case studies', label='Keep reading'):
    return f'''    <section class="section section--alt" id="related">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">{label}</p>
          <h2>{title}</h2>
        </div>
        <div class="post-grid">
{chr(10).join(card(i) for i in items)}
        </div>
      </div>
    </section>'''


def article_ld(it, route, extra=None):
    o = {"@context": "https://schema.org", "@type": "Article", "mainEntityOfPage": {"@type": "WebPage", "@id": SITE + route},
         "headline": plain(it['title']), "description": it['desc'],
         "image": [f"{SITE}/Asset/img/manufacturing/{it['slug']}.webp", f"{SITE}/Asset/og/mfg-{it['slug']}.jpg"],
         "datePublished": it['published'], "dateModified": it.get('modified', it['published']),
         "author": AUTHORS[it['author']]['ld'], "publisher": ORG, "articleSection": it['category'],
         "keywords": it['keyword'], "wordCount": words(it.get('body') or ' '.join(s[2] for s in it['sections'])), "inLanguage": "en"}
    if extra: o.update(extra)
    return o


MISSING = set()


def pick(ALL, slugs):
    out = []
    for s in slugs:
        if s in ALL: out.append(ALL[s])
        else: MISSING.add(s)
    return out


# ------------------------------------------------------------------ guide pages
def guide_page(a, ALL):
    route = item_route(a)
    trail = [('/', 'Home'), (BASE, 'Manufacturing'), (BASE + 'guides/', 'Guides'), (route, plain(a['title']))]
    au = AUTHORS[a['author']]
    tone = a.get('tone', '')
    layout = a.get('layout', 'toc-left')
    cls = ['mfg-post', f"mfg-post--{a.get('kind', 'guide')}"]
    if layout != 'toc-left': cls.append('mfg-post--' + layout)
    if tone: cls.append('mfg-post--' + tone)
    hero_cls = 'post-hero' + (f' mfg-hero--{tone}' if tone else '')
    body = a['body'].strip('\n')
    toc = '\n'.join(f'              <li><a href="#{i}">{plain(t)}</a></li>' for i, t in toc_items(body))
    blocks = [ld(article_ld(a, route)), ld(crumbs_ld(trail))]
    if a.get('faqs'): blocks.append(ld(faq_ld(a['faqs'])))
    faq = ('          <h2 id="faq">Frequently asked questions</h2>\n' + faq_html(a['faqs'])) if a.get('faqs') else ''
    if faq: toc += '\n              <li><a href="#faq">Frequently asked questions</a></li>'
    related = pick(ALL, a['related'])
    svc = ' &middot; '.join(f'<a href="{r}">{n}</a>' for r, n in a.get('services', []))
    main = f'''    <article class="post {' '.join(cls)}">
      <header class="{hero_cls}">
        <div class="container container--post">
          {crumbs([('/', 'Home'), (BASE, 'Manufacturing'), (BASE + 'guides/', 'Guides'), (route, a['category'])])}
          <p class="section-label">{a['category']} &middot; {a['kind_label']}</p>
          <h1>{a['title']}</h1>
          <p class="post-lead">{a['lead']}</p>
          <div class="post-byline">
            {au['avatar']}
            <div>
              <p class="post-byline-name">{au['byline']}</p>
              <p class="post-byline-meta"><time datetime="{a['published']}">{nice(a['published'])}</time> &middot; {read_time(a)} min read</p>
            </div>
          </div>
          {facts_dl(a.get('facts'))}
        </div>
      </header>
{subnav(route)}
      <div class="container container--post">
        <figure class="post-cover">
          <img src="/Asset/img/manufacturing/{a['slug']}.webp" alt="{html.escape(a['hero_alt'])}" width="1200" height="675" fetchpriority="high">
          <figcaption>{a['hero_cap']}</figcaption>
        </figure>
      </div>

      <div class="container post-layout">
        <aside class="post-toc" aria-label="On this page">
          <details open>
            <summary>On this page</summary>
            <ol>
{toc}
            </ol>
          </details>
        </aside>

        <div class="post-body">
          <div class="quick-answer">
            <p class="quick-answer-label">In short</p>
            <p>{a['answer']}</p>
          </div>
{body}
{faq}
{sources_html(a.get('sources'))}
          <p class="post-services"><strong>Related services:</strong> {svc}</p>

{author_box(a['author'])}
        </div>
      </div>
    </article>

{related_section(related)}

{cta(a.get('cta_title', 'Want this working in your factory?'), a.get('cta_text', 'Tell us how the process runs today. We will map it, show you what a first version looks like and price it before you commit.'))}'''
    extra = (f'  <meta property="article:published_time" content="{a["published"]}">\n'
             f'  <meta property="article:author" content="{SITE}/about/">\n  <meta property="article:section" content="{html.escape(a["category"])}">\n')
    return shell(route, a['seo_title'] + ' | Zudo Works', a['desc'], f"/Asset/og/mfg-{a['slug']}.jpg", 'article', blocks, main, author=au['meta'], extra_meta=extra)


# ------------------------------------------------------------------ case study pages
NOTE = ('<p class="mfg-note"><strong>Illustrative case study.</strong> This is a reference implementation we designed to show how a problem like this can be solved. '
        'The company is a composite, not a client, and no customer data, quotes or measured results are shown. Screens are concept mockups, not screenshots of a live system. '
        'Names and numbers inside the screens are made-up example data. Expected benefits are stated as directions, not figures.</p>')


def case_page(c, ALL):
    route = item_route(c)
    trail = [('/', 'Home'), (BASE, 'Manufacturing'), (BASE + 'case-studies/', 'Case studies'), (route, plain(c['title']))]
    au = AUTHORS[c['author']]
    tpl = c['template']   # dossier | ba | ai
    secs, toc = '', ''
    for n, (sid, title, body) in enumerate(c['sections'], 1):
        secs += f'\n          <h2 id="{sid}"><span class="cs-num">{n:02d}</span><span>{title}</span></h2>\n{body.strip(chr(10))}\n'
        toc += f'<li><a href="#{sid}">{title}</a></li>'
    facts = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in c['facts'])
    side = f'''        <aside class="cs-side" aria-label="Case study summary">
          <div class="cs-side-inner">
            <div class="cs-card{' cs-card--dark' if tpl == 'ai' else ''}"><h2>At a glance</h2><dl>{facts}</dl></div>
            <div class="cs-card"><h2>Contents</h2><ol>{toc}</ol></div>
          </div>
        </aside>'''
    lay = {'dossier': 'cs-layout', 'ba': 'cs-layout cs-layout--left', 'ai': 'cs-layout'}[tpl]
    hero_tone = {'dossier': '', 'ba': ' mfg-hero--green', 'ai': ' mfg-hero--dark'}[tpl]
    blocks = [ld(article_ld(c, route, {"abstract": "Illustrative reference implementation. The company described is a composite, not a client."})), ld(crumbs_ld(trail))]
    if c.get('faqs'): blocks.append(ld(faq_ld(c['faqs'])))
    faq = ('\n          <h2 id="faq"><span class="cs-num">Q</span><span>Questions about this reference implementation</span></h2>\n' + faq_html(c['faqs'])) if c.get('faqs') else ''
    related = pick(ALL, c['related'])
    main = f'''    <article class="post mfg-post cs cs--{tpl}">
      <header class="post-hero{hero_tone}">
        <div class="container container--post">
          {crumbs([('/', 'Home'), (BASE, 'Manufacturing'), (BASE + 'case-studies/', 'Case studies'), (route, c['category'])])}
          <p class="section-label">Illustrative case study &middot; {c['category']}</p>
          <h1>{c['title']}</h1>
          <p class="post-lead">{c['lead']}</p>
          <div class="post-byline">
            {au['avatar']}
            <div>
              <p class="post-byline-name">{au['byline']}</p>
              <p class="post-byline-meta"><time datetime="{c['published']}">{nice(c['published'])}</time> &middot; {read_time(c)} min read &middot; Reference implementation</p>
            </div>
          </div>
        </div>
      </header>
{subnav(route)}
      <div class="container container--post">
        <figure class="post-cover">
          <img src="/Asset/img/manufacturing/{c['slug']}.webp" alt="{html.escape(c['hero_alt'])}" width="1200" height="675" fetchpriority="high">
          <figcaption>{c['hero_cap']}</figcaption>
        </figure>
      </div>

      <div class="container {lay}">
        <div class="post-body cs-body">
          {NOTE}
{secs}{faq}
{sources_html(c.get('sources'))}

{author_box(c['author'])}
        </div>
{side}
      </div>
    </article>

{related_section(related, 'Related guides and reference implementations')}

{cta(c.get('cta_title', 'Have a process like this one?'), c.get('cta_text', 'Send us a description of how it runs today. We will tell you what we would build first, what we would leave alone and what it would cost.'))}'''
    extra = f'  <meta property="article:published_time" content="{c["published"]}">\n  <meta property="article:section" content="Case study">\n'
    return shell(route, c['seo_title'] + ' | Zudo Works', c['desc'], f"/Asset/og/mfg-{c['slug']}.jpg", 'article', blocks, main, author=au['meta'], extra_meta=extra)


# ------------------------------------------------------------------ solution and hub pages
def hero_block(p, route, trail):
    tone = f" mfg-hero--{p['tone']}" if p.get('tone') else ''
    btns = ''.join(f'<a href="{h}" class="btn {c} btn-lg"{" data-booking" if h == "/contact/" else ""}>{t}</a>\n            '
                   for t, h, c in p['buttons'])
    return f'''    <section class="mfg-hero{tone}">
      <div class="container">
        {crumbs(trail)}
        <div class="mfg-hero-grid">
          <div>
            <p class="section-label">{p['label']}</p>
            <h1>{p['h1']}</h1>
            <p class="page-lead">{p['lead']}</p>
            <div class="btn-group">
            {btns.rstrip()}
            </div>
            {facts_dl(p.get('facts'))}
          </div>
          <figure class="mfg-hero-visual">
            <img src="/Asset/img/manufacturing/{p['hero']}.webp" alt="{html.escape(p['hero_alt'])}" width="1200" height="675" fetchpriority="high">
          </figure>
        </div>
      </div>
    </section>
{subnav(route)}'''


def solution_page(p, ALL):
    route = p['route']
    trail = [('/', 'Home'), (BASE, 'Manufacturing')] + ([] if route == BASE else [(route, p['crumb'])])
    if p.get('collection'):
        items = ALL[p['collection']]
        first = ld({"@context": "https://schema.org", "@type": "CollectionPage", "name": p['seo_title'], "description": p['desc'], "url": SITE + route,
                    "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#organization"},
                    "mainEntity": {"@type": "ItemList", "itemListElement": [
                        {"@type": "ListItem", "position": i + 1, "url": SITE + item_route(it), "name": plain(it['title'])} for i, it in enumerate(items)]}})
    else:
        first = ld({"@context": "https://schema.org", "@type": "Service", "name": p['service_name'], "serviceType": p['service_type'],
                    "description": p['desc'], "url": SITE + route, "provider": {"@id": SITE + "/#organization"},
                    "areaServed": ["New Zealand", "Australia", "United Kingdom", "United States", "India"],
                    "audience": {"@type": "BusinessAudience", "audienceType": "Small and midsized manufacturers"}})
    blocks = [first, ld(crumbs_ld(trail))]
    if p.get('faqs'): blocks.append(ld(faq_ld(p['faqs'])))
    body = p['sections'](ALL) if callable(p['sections']) else p['sections']
    faq = ''
    if p.get('faqs'):
        faq = f'''    <section class="section" id="faq">
      <div class="container container--prose">
        <div class="section-header section-header--left">
          <p class="section-label">Questions</p>
          <h2>{p.get('faq_title', 'Frequently asked questions')}</h2>
        </div>
{faq_html(p['faqs'])}
      </div>
    </section>'''
    main = hero_block(p, route, trail) + '\n' + body.strip('\n') + '\n' + faq + '\n' + cta(*p['cta'])
    return shell(route, p['seo_title'] + ' | Zudo Works', p['desc'], f"/Asset/og/mfg-{p['hero']}.jpg", 'website', blocks, main)


def write(route, content):
    path = os.path.join(ROOT, route.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def main():
    import content_pages, content_guides, content_cases
    guides, cases = content_guides.GUIDES, content_cases.CASES
    for g in guides: g['type'] = 'guide'
    for c in cases: c['type'] = 'case'
    ALL = {i['slug']: i for i in guides + cases}
    ALL['_guides'], ALL['_cases'] = guides, cases
    ALL['_card'] = card
    for p in content_pages.PAGES:
        write(p['route'], solution_page(p, ALL))
    for g in guides:
        write(item_route(g), guide_page(g, ALL))
        print(f"  guide {g['slug']}: {words(g['body'])} words, {g['body'].count('<figure') + 1} visuals, by {AUTHORS[g['author']]['name']}")
    for c in cases:
        write(item_route(c), case_page(c, ALL))
        body = ' '.join(s[2] for s in c['sections'])
        print(f"  case  {c['slug']}: {words(body)} words, {body.count('<figure') + 1} visuals ({body.count('mfg-fig--ui')} app screens), {len(c['sections'])} sections")
    failed = figs.render_all(only=sys.argv[1:] or None)
    if MISSING: print('  MISSING related items:', ', '.join(sorted(MISSING)))
    return 1 if failed or MISSING else 0


if __name__ == '__main__':
    sys.exit(main())
