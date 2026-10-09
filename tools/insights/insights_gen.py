"""Generate /insights/<slug>/ articles and the /insights/ index. Run from the repo root."""
import html, json, os, re, sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import articles_a, articles_b, articles_c, articles_ext, articles_meta, articles_answers, articles_watch  # noqa: E402

SITE = 'https://zudoworks.com'
ARTICLES = articles_a.ARTICLES + articles_b.ARTICLES + articles_c.ARTICLES
for _a in ARTICLES:  # insert extra sections before the FAQ heading
    _x = articles_ext.EXT.get(_a['slug'])
    if _x:
        assert '<h2 id="faq">' in _a['body'], _a['slug']
        _a['body'] = _a['body'].replace('<h2 id="faq">', _x.strip('\n') + '\n\n<h2 id="faq">', 1)
for _a in ARTICLES:  # short search title and meta description
    _a['seo_title'], _a['meta_description'] = articles_meta.META[_a['slug']]
BY_SLUG = {a['slug']: a for a in ARTICLES}

# Service pages each article supports (rendered as a "Related services" line)
SERVICE_NAMES = {
    '/zoho-creator-development/': 'Zoho Creator development', '/zoho-crm-development/': 'Zoho CRM implementation',
    '/deluge-development/': 'Deluge development', '/zoho-integrations/': 'Zoho integrations',
    '/business-process-automation/': 'Business process automation', '/custom-software-development/': 'Custom software',
    '/support-maintenance/': 'Support and maintenance', '/zoho-development/': 'Zoho development', '/pricing/': 'Pricing',
}
SERVICES_FOR = {
    'zoho-creator-vs-power-apps': ['/zoho-creator-development/', '/custom-software-development/', '/pricing/'],
    'migrate-hubspot-salesforce-to-zoho-crm': ['/zoho-crm-development/', '/zoho-integrations/', '/pricing/'],
    'zoho-crm-implementation-cost': ['/zoho-crm-development/', '/pricing/', '/support-maintenance/'],
    'deluge-script-examples': ['/deluge-development/', '/business-process-automation/', '/zoho-integrations/'],
    'zoho-agentic-ai-hyperautomation': ['/zoho-crm-development/', '/business-process-automation/', '/deluge-development/'],
    'zoho-analytics-agentic-data-foundations-2026': ['/zoho-integrations/', '/zoho-development/', '/business-process-automation/'],
    'zoho-partner-software-development': ['/zoho-development/', '/pricing/', '/support-maintenance/'],
    'zoho-partner-program-explained': ['/zoho-development/', '/zoho-creator-development/', '/zoho-crm-development/'],
    'zoho-crm-vs-hubspot': ['/zoho-crm-development/', '/zoho-integrations/', '/pricing/'],
    'zoho-mcp-claude-chatgpt': ['/business-process-automation/', '/zoho-integrations/', '/zoho-crm-development/'],
    'zoho-for-manufacturing': ['/zoho-creator-development/', '/zoho-integrations/', '/custom-software-development/'],
    'zoho-flow-vs-deluge': ['/zoho-integrations/', '/deluge-development/', '/custom-software-development/'],
}


def services_line(a):
    routes = SERVICES_FOR[a['slug']] + (['/zoho-development/'] if '/zoho-development/' not in SERVICES_FOR[a['slug']] else [])
    links = ' &middot; '.join(f'<a href="{r}">{SERVICE_NAMES[r]}</a>' for r in routes)
    return f'          <p class="post-services"><strong>Related services:</strong> {links}</p>'



AUTHOR = {
    "@type": "Person",
    "@id": SITE + "/#arunkumar-v",
    "name": "Arunkumar V",
    "alternateName": "Arunkumar Venkadesan",
    "jobTitle": "Chief Technology Officer",
    "image": SITE + "/Asset/img/team/arunkumar-v.jpg",
    "url": SITE + "/about/#leadership",
    "worksFor": {"@id": SITE + "/#organization"},
    "award": "Master of Creator (Global Winner) award, Zoho Creator Partner Hackathon 2025",
    "sameAs": ["https://www.linkedin.com/in/arunkumar-v-5509aa1aa/", "https://www.upwork.com/freelancers/arunk191"],
}
PUBLISHER = {"@type": "Organization", "@id": SITE + "/#organization", "name": "Zudo Works",
             "logo": {"@type": "ImageObject", "url": SITE + "/Asset/brand/zudo-works-logo.svg"}}


def plain(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


def nice_date(d):
    y, m, dd = map(int, d.split('-'))
    return date(y, m, dd).strftime('%d %B %Y').lstrip('0')


def words(a):
    text = plain(a['body']) + ' ' + ' '.join(q + ' ' + ans for q, ans in a.get('faqs', []))
    return len(text.split())


def read_time(a):
    return max(1, round(words(a) / 220))


def ld(obj):
    return '  <script type="application/ld+json">\n' + json.dumps(obj, indent=2, ensure_ascii=False) + '\n  </script>'


def toc(a):
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', a['body'])
    return '\n'.join(f'              <li><a href="#{i}">{t}</a></li>' for i, t in items)


def faq_html(faqs):
    out = []
    for q, ans in faqs:
        out.append(f'''          <div class="faq-item">
            <button type="button" class="faq-question" aria-expanded="false">
              <span>{html.escape(q, quote=False)}</span>
              <svg class="faq-toggle" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <p>{html.escape(ans, quote=False)}</p>
            </div>
          </div>''')
    return '        <div class="faq-list">\n' + '\n'.join(out) + '\n        </div>'


def byline(a, small=False):
    pub, mod = a['published'], a['modified']
    dates = f'<time datetime="{pub}">{nice_date(pub)}</time>'
    if mod != pub:
        dates = f'Published {dates} &middot; Updated <time datetime="{mod}">{nice_date(mod)}</time>'
    return dates + f' &middot; {read_time(a)} min read'


def card(a, level='h3', featured=False):
    cls = 'post-card post-card--featured' if featured else 'post-card'
    return f'''          <article class="{cls}">
            <a class="post-card-image" href="/insights/{a['slug']}/" tabindex="-1" aria-hidden="true">
              <img src="/Asset/img/insights/{a['slug']}.webp" alt="{html.escape(a['cover_alt'])}" width="1600" height="900" loading="lazy">
            </a>
            <div class="post-card-body">
              <p class="post-card-category">{a['category']}</p>
              <{level}><a href="/insights/{a['slug']}/">{a['title']}</a></{level}>
              <p class="post-card-excerpt">{a['description']}</p>
              <p class="post-card-meta">Arunkumar V &middot; {byline(a)}</p>
            </div>
          </article>'''


def article_page(a):
    url = f"{SITE}/insights/{a['slug']}/"
    img = f"{SITE}/Asset/img/insights/{a['slug']}.webp"
    og = f"{SITE}/Asset/og/{a['slug']}.jpg"
    title_plain = plain(a['title'])
    blocks = [
        ld({"@context": "https://schema.org", "@type": "BlogPosting",
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "headline": title_plain, "description": plain(a['description']),
            "abstract": articles_answers.ANSWERS[a['slug']],
            "image": [img, og], "datePublished": a['published'], "dateModified": a['modified'],
            "author": AUTHOR, "publisher": PUBLISHER, "articleSection": a['category'],
            "keywords": a['keyword'], "wordCount": words(a), "inLanguage": "en"}),
        ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Insights", "item": SITE + "/insights/"},
            {"@type": "ListItem", "position": 3, "name": title_plain, "item": url}]}),
    ]
    if a.get('faqs'):
        blocks.append(ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}}
            for q, ans in a['faqs']]}))
    seo = html.escape(plain(a['seo_title']))
    desc = html.escape(plain(a['meta_description']))
    related = '\n'.join(card(BY_SLUG[s]) for s in a['related'])
    body = a['body'].strip('\n')
    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <!-- @head -->
    <!-- @/head -->

  <title>{seo} | Zudo Works</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Arunkumar V">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{html.escape(title_plain)}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{og}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Zudo Works">
  <meta property="og:locale" content="en_US">
  <meta property="article:published_time" content="{a['published']}">
  <meta property="article:modified_time" content="{a['modified']}">
  <meta property="article:author" content="{SITE}/about/#leadership">
  <meta property="article:section" content="{html.escape(plain(a['category']))}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title_plain)}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og}">
{chr(10).join(blocks)}
</head>

<body>
    <!-- @header -->
    <!-- @/header -->

  <main id="main-content">
    <article class="post">
      <header class="post-hero">
        <div class="container container--post">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="/">Home</a>
            <span class="breadcrumb-sep" aria-hidden="true">/</span>
            <a href="/insights/">Insights</a>
            <span class="breadcrumb-sep" aria-hidden="true">/</span>
            <span class="breadcrumb-current" aria-current="page">{a['category']}</span>
          </nav>
          <p class="section-label">{a['category']}</p>
          <h1>{a['title']}</h1>
          <p class="post-lead">{a['lead']}</p>
          <div class="post-byline">
            <img class="author-avatar" src="/Asset/img/team/arunkumar-v-avatar.webp" alt="Arunkumar V" width="44" height="44">
            <div>
              <p class="post-byline-name">By <a href="/about/#leadership" rel="author">Arunkumar V</a>, CTO at Zudo Works</p>
              <p class="post-byline-meta">{byline(a)}</p>
            </div>
          </div>
        </div>
      </header>

      <div class="container container--post">
        <figure class="post-cover">
          <img src="/Asset/img/insights/{a['slug']}.webp" alt="{html.escape(a['cover_alt'])}" width="1600" height="900"
            fetchpriority="high">
          <figcaption>{a['caption']}</figcaption>
        </figure>
      </div>

      <div class="container post-layout">
        <aside class="post-toc" aria-label="On this page">
          <details open>
            <summary>On this page</summary>
            <ol>
{toc(a)}
            </ol>
          </details>
        </aside>

        <div class="post-body">
          <div class="quick-answer">
            <p class="quick-answer-label">Quick answer</p>
            <p>{html.escape(articles_answers.ANSWERS[a['slug']], quote=False)}</p>
          </div>
{body}
{faq_html(a.get('faqs', []))}
{services_line(a)}

          <aside class="author-box" aria-label="About the author">
            <img class="author-avatar author-avatar--lg" src="/Asset/img/team/arunkumar-v-avatar.webp" alt="Arunkumar V" width="64" height="64" loading="lazy">
            <div>
              <p class="author-box-label">Written by</p>
              <p class="author-box-name"><a href="/about/#leadership">Arunkumar V</a>, Chief Technology Officer, Zudo Works</p>
              <p>Arunkumar builds Zoho Creator apps, Zoho CRM systems, Deluge automations and integrations for
                businesses in the US, UK, Australia, New Zealand and India. He received the &ldquo;Master of
                Creator&rdquo; award at the Zoho Creator Partner Hackathon 2025.</p>
              <p class="author-box-links">
                <a href="https://www.linkedin.com/in/arunkumar-v-5509aa1aa/" target="_blank" rel="noopener">LinkedIn</a>
                <a href="/about/#leadership">About Arunkumar</a>
              </p>
            </div>
          </aside>
        </div>
      </div>
    </article>

    <section class="section section--alt" id="related">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Keep reading</p>
          <h2>Related articles</h2>
        </div>
        <div class="post-grid">
{related}
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div class="container">
        <h2>Planning a Zoho project?</h2>
        <p>US$15 per hour, fixed prices for defined projects, and one month of free support after launch.</p>
        <div class="btn-group justify-center">
          <a href="/contact/" class="btn btn-white btn-lg" data-booking>Book a Discovery Call</a>
          <a href="/pricing/#calculator" class="btn btn-outline-white btn-lg">Estimate My Project</a>
        </div>
      </div>
    </section>
  </main>

    <!-- @footer -->
    <!-- @/footer -->
</body>

</html>
'''


def index_page():
    items = sorted(ARTICLES, key=lambda a: (a['modified'], a['published']), reverse=True)
    newest = sorted(ARTICLES, key=lambda a: a['published'], reverse=True)
    featured, rest = newest[0], [a for a in items if a is not newest[0]]
    blog = {"@context": "https://schema.org", "@type": "Blog", "name": "Zudo Works Insights",
            "url": SITE + "/insights/", "publisher": {"@id": SITE + "/#organization"},
            "blogPost": [{"@type": "BlogPosting", "headline": plain(a['title']),
                          "url": f"{SITE}/insights/{a['slug']}/", "datePublished": a['published'],
                          "dateModified": a['modified'], "author": {"@id": SITE + "/#arunkumar-v"}}
                         for a in items]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Insights", "item": SITE + "/insights/"}]}
    cards = '\n'.join(card(a, 'h2') for a in rest)
    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <!-- @head -->
    <!-- @/head -->

  <title>Zoho Guides, Comparisons and Deluge Examples | Zudo Works</title>
  <meta name="description" content="Practical Zoho guides from our CTO: Zoho Creator vs Power Apps, CRM migration, implementation costs, Deluge script examples, AI and analytics.">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Zoho Insights | Zudo Works">
  <meta property="og:description" content="Practical Zoho guides: comparisons, migration plans, costs, Deluge examples, AI and analytics.">
  <meta property="og:url" content="{SITE}/insights/">
  <meta property="og:image" content="{SITE}/Asset/og/{featured['slug']}.jpg">
  <meta property="og:site_name" content="Zudo Works">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{SITE}/Asset/og/{featured['slug']}.jpg">
{ld(blog)}
{ld(crumbs)}
</head>

<body>
    <!-- @header -->
    <!-- @/header -->

  <main id="main-content">
    <section class="page-hero page-hero--service">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <span class="breadcrumb-sep" aria-hidden="true">/</span>
          <span class="breadcrumb-current" aria-current="page">Insights</span>
        </nav>
        <p class="section-label">Insights</p>
        <h1>Practical Zoho guides from people who build on it</h1>
        <p class="page-lead">Comparisons, migration plans, honest costs and working Deluge code, written by our CTO,
          Arunkumar V, from real project experience.</p>
      </div>
    </section>

    <section class="section" id="articles">
      <div class="container">
        <div class="post-featured">
{card(featured, 'h2', featured=True)}
        </div>
        <div class="post-grid">
{cards}
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div class="container">
        <h2>Have a Zoho question we haven&rsquo;t covered?</h2>
        <p>Ask us directly. We reply within one business day.</p>
        <div class="btn-group justify-center">
          <a href="/contact/" class="btn btn-white btn-lg" data-booking>Book a Discovery Call</a>
          <a href="/contact/#contact-form" class="btn btn-outline-white btn-lg">Send a Question</a>
        </div>
      </div>
    </section>
  </main>

    <!-- @footer -->
    <!-- @/footer -->
</body>

</html>
'''


REVIEW_DAYS = {'high': 14, 'medium': 45, 'low': 120}


def history_entry(a):
    """One index record: enough for a later run to judge an article without opening it."""
    from datetime import timedelta
    w = articles_watch.WATCH.get(a['slug'], {})
    vol = w.get('volatility', 'medium')
    checked = w.get('checked', '')
    if checked:
        y, m, d = map(int, checked.split('-'))
        next_check = (date(y, m, d) + timedelta(days=REVIEW_DAYS[vol])).isoformat()
    else:
        next_check = 'due'
    return {"title": plain(a['title']), "url": f"/insights/{a['slug']}/", "slug": a['slug'],
            "keyword": a['keyword'], "category": a['category'],
            "date": a['published'], "updated": a['modified'], "author": "Arunkumar V",
            "image": f"/Asset/img/insights/{a['slug']}.webp",
            "cover_style": w.get('cover', 'older style'),
            "summary": articles_answers.ANSWERS[a['slug']],
            "sections": [plain(t) for _, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', a['body']) if _ != 'faq'],
            "questions": [q for q, _ in a.get('faqs', [])],
            "words": words(a), "related": a['related'],
            "review": {"last_checked": checked or "never", "volatility": vol, "next_check": next_check,
                       "facts_to_watch": w.get('facts', []), "sources": w.get('sources', [])}}


def rss_feed():
    """RSS 2.0 feed of every article, newest first (linked from every page's head)."""
    from email.utils import format_datetime
    from datetime import datetime, timezone
    def rfc(d):
        return format_datetime(datetime.fromisoformat(d).replace(tzinfo=timezone.utc))
    items = sorted(ARTICLES, key=lambda a: a['published'], reverse=True)
    esc = lambda t: html.escape(plain(t), quote=False)
    body = ''.join(f'''
    <item>
      <title>{esc(a['title'])}</title>
      <link>{SITE}/insights/{a['slug']}/</link>
      <guid isPermaLink="true">{SITE}/insights/{a['slug']}/</guid>
      <description>{esc(articles_answers.ANSWERS[a['slug']])}</description>
      <category>{esc(a['category'])}</category>
      <dc:creator>Arunkumar V</dc:creator>
      <pubDate>{rfc(a['published'])}</pubDate>
    </item>''' for a in items)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
            '  <channel>\n    <title>Zudo Works Insights</title>\n'
            f'    <link>{SITE}/insights/</link>\n'
            f'    <atom:link href="{SITE}/insights/feed.xml" rel="self" type="application/rss+xml"/>\n'
            '    <description>Practical guides on Zoho CRM, Zoho Creator, Deluge and integrations from the Zudo Works team.</description>\n'
            f'    <language>en</language>\n    <lastBuildDate>{rfc(max(a["modified"] for a in ARTICLES))}</lastBuildDate>'
            + body + '\n  </channel>\n</rss>\n')


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


if __name__ == '__main__':
    for a in ARTICLES:
        write(f"insights/{a['slug']}/index.html", article_page(a))
        print(f"{a['slug']}: {words(a)} words, {read_time(a)} min")
    write('insights/index.html', index_page())
    hist = {"about": "Index of every Insights article for automated runs. Read this first instead of opening "
                     "each article. Generated by tools/insights/insights_gen.py; edit review notes in "
                     "tools/insights/articles_watch.py, not here.",
            "articles": [history_entry(a) for a in sorted(ARTICLES, key=lambda a: a['published'], reverse=True)]}
    write('blog/.automation-history.json', json.dumps(hist, indent=2, ensure_ascii=False) + '\n')
    write('insights/feed.xml', rss_feed())
    print('index + history written')
