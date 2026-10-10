"""Zudo Works site build.

Run from the repository root after editing any page, partial, CSS or JS file:

    python tools/build.py

The HTML pages are the source of truth. This script only rewrites the regions
between these markers, so everything else in a page stays hand-editable:

    <!-- @head -->   ... <!-- @/head -->     tools/partials/head.html
    <!-- @header --> ... <!-- @/header -->   tools/partials/header.html
    <!-- @footer --> ... <!-- @/footer -->   tools/partials/footer.html

It also bundles css/*.css into css/site.css and the shared scripts into
js/site.js (both cache-busted by content hash), regenerates sitemap.xml and
checks every internal link. Commit the generated files; Cloudflare Pages
serves the repository as-is, with no build step.
"""

import datetime
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://zudoworks.com'
SKIP_DIRS = {'.git', '.kilo', 'tools', 'Asset', 'css', 'js', 'node_modules'}

CSS_SOURCES = ['variables', 'reset', 'base', 'components', 'hero', 'sections',
               'responsive', 'cookie-consent', 'helpers', 'system', 'manufacturing']
JS_SOURCES = ['main', 'animations', 'cookie-consent', 'booking', 'salesiq', 'media']

# Pages that should not appear in the sitemap or get a canonical tag
NOINDEX = {'/404.html'}

# Meta keywords per page. Google ignores this tag, but Bing and some AI tools read it,
# so keep each list short and true to the page. Articles use their own keyword from
# the BlogPosting data (tools/insights/articles_*.py).
KEYWORDS = {
    '/': 'Zudo Works, Zoho developers, Zoho Creator development, Zoho CRM implementation, Deluge, Zoho integrations, custom software',
    '/services/': 'Zoho services, Zoho Creator, Zoho CRM, Deluge development, Zoho integrations, business process automation',
    '/zoho-development/': 'Zoho consultants, Zoho development partner, Zoho implementation, Zoho One, Zoho Books, Zoho customization',
    '/zoho-creator-development/': 'Zoho Creator development, Zoho Creator partner, Zoho Creator developer, custom Zoho apps, Zoho Creator portals',
    '/zoho-crm-development/': 'Zoho CRM implementation, Zoho CRM customization, Zoho CRM consultant, Zoho CRM migration, Blueprint',
    '/deluge-development/': 'Deluge developer, Deluge scripting, Zoho custom functions, Zoho automation, Deluge examples',
    '/zoho-integrations/': 'Zoho integrations, Zoho API, Zoho webhooks, Zoho Flow, Zoho middleware, Zoho Books integration',
    '/business-process-automation/': 'business process automation, Zoho workflow automation, approval workflows, Zoho Flow, Deluge',
    '/custom-software-development/': 'custom software development, web application development, internal tools, Laravel, Node.js',
    '/support-maintenance/': 'Zoho support, Zoho maintenance, Zoho admin support, Zoho CRM support, Zoho retainer',
    '/pricing/': 'Zoho developer pricing, Zoho developer hourly rate, Zoho project cost calculator, Zoho implementation cost',
    '/work/': 'Zudo Works reviews, Zudo Works projects, Zoho project experience, Zoho case studies',
    '/about/': 'Zudo Works, about Zudo Works, Arunkumar V, Zoho Creator Master of Creator award, Zoho developers Chennai',
    '/contact/': 'contact Zudo Works, book a Zoho consultation, Zoho developer WhatsApp, Zoho discovery call',
    '/insights/': 'Zoho guides, Zoho CRM guides, Zoho Creator guides, Deluge tutorials, Zoho blog',
    '/locations/': 'Zoho consultants worldwide, Zoho partner by country, Zoho consultants US UK Australia New Zealand India',
    '/locations/india/': 'Zoho consultants India, Zoho partner India, Zoho developers Chennai, Zoho partner Delhi, Zoho partner Mumbai',
    '/locations/united-states/': 'Zoho consultants USA, Zoho partner US, Zoho developers United States, Zoho CRM consultant USA',
    '/locations/united-kingdom/': 'Zoho consultants UK, Zoho partner UK, Zoho developers United Kingdom, Zoho Books VAT MTD',
    '/locations/australia/': 'Zoho consultants Australia, Zoho partner Australia, Zoho developers Sydney Melbourne, Zoho Xero integration',
    '/locations/new-zealand/': 'Zoho consultants New Zealand, Zoho partner NZ, Zoho developers Auckland, Zoho Xero integration',
    '/manufacturing/': 'manufacturing workflow automation, Zoho for manufacturing, manufacturing software New Zealand, production tracking, custom manufacturing apps',
    '/manufacturing/zoho-implementation/': 'Zoho implementation for manufacturers, Zoho Inventory manufacturing, Zoho Creator manufacturing, Zoho Books, Zoho Analytics',
    '/manufacturing/ai-automation/': 'AI in manufacturing, AI for small manufacturers, demand forecasting, document processing, Zia, manufacturing AI use cases',
    '/manufacturing/workflows/': 'manufacturing workflows, quote to cash, procure to pay, production tracking, quality workflow, maintenance workflow',
    '/manufacturing/guides/': 'manufacturing guides, inventory accuracy, production tracking, traceability, manufacturing dashboards, Zoho Creator',
    '/manufacturing/case-studies/': 'manufacturing case studies, manufacturing reference implementations, Zoho manufacturing examples',
    '/privacy/': 'Zudo Works privacy policy',
    '/terms/': 'Zudo Works terms of service',
}

ROBOTS = 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'


def keywords_for(route, html):
    if route in KEYWORDS:
        return KEYWORDS[route]
    m = re.search(r'"keywords":\s*"([^"]+)"', html)
    return f'Zudo Works, {m.group(1)}' if m else ''



def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return f.read()


def write_if_changed(path, content):
    full = os.path.join(ROOT, path)
    if os.path.exists(full) and read(path) == content:
        return False
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    return True


def short_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()[:10]


def minify_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};])\s*', r'\1', css)
    return css.replace(';}', '}').strip() + '\n'


def bundle_css():
    parts = [read(f'css/{name}.css') for name in CSS_SOURCES]
    out = '/* Generated by tools/build.py from css/*.css. Do not edit. */\n' + minify_css('\n'.join(parts))
    write_if_changed('css/site.css', out)
    return short_hash(out)


def bundle_js():
    parts = [f'/* --- js/{name}.js --- */\n' + read(f'js/{name}.js').lstrip('﻿') for name in JS_SOURCES]
    out = '/* Generated by tools/build.py from js/*.js. Do not edit. */\n' + '\n'.join(parts)
    write_if_changed('js/site.js', out)
    return short_hash(out)


def find_pages():
    pages = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT).replace('\\', '/')
        if rel != '.' and rel.split('/')[0] in SKIP_DIRS:
            dirnames[:] = []
            continue
        for name in filenames:
            if name == 'index.html' or (rel == '.' and name == '404.html'):
                path = name if rel == '.' else f'{rel}/{name}'
                pages.append(path)
    return sorted(pages)


def route_for(path):
    if path == '404.html':
        return '/404.html'
    return '/' + path[:-len('index.html')]


def replace_region(html, name, content, path):
    pattern = re.compile(r'(<!-- @%s -->\n).*?\s*(<!-- @/%s -->)' % (name, name), re.S)
    if not pattern.search(html):
        sys.exit(f'{path}: missing <!-- @{name} --> ... <!-- @/{name} --> markers')
    return pattern.sub(lambda m: m.group(1) + content.rstrip('\n') + '\n    ' + m.group(2), html, count=1)


def nav_with_active(header, route):
    def mark(m):
        href = m.group(1)
        active = route == href or (href != '/' and route.startswith(href))
        cls = 'navbar-link active" aria-current="page' if active else 'navbar-link'
        return f'<a href="{href}" class="{cls}">'
    return re.sub(r'<a href="([^"]+)" class="navbar-link">', mark, header)


def add_twitter_text(html):
    """Copy og:title / og:description into Twitter tags when a page doesn't set its own."""
    for name in ('title', 'description'):
        if f'<meta name="twitter:{name}"' in html:
            continue
        m = re.search(r'<meta property="og:%s"\s+content="([^"]*)">' % name, html)
        card = re.search(r'\n( *)<meta name="twitter:card"[^>]*>', html)
        if m and card:
            tag = f'\n{card.group(1)}<meta name="twitter:{name}" content="{m.group(1)}">'
            html = html[:card.end()] + tag + html[card.end():]
    return html


def git_date(path):
    try:
        dirty = subprocess.run(['git', 'status', '--porcelain', '--', path], cwd=ROOT,
                               capture_output=True, text=True).stdout.strip()
        if not dirty:
            out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', path], cwd=ROOT,
                                 capture_output=True, text=True).stdout.strip()
            if out:
                return out
    except OSError:
        pass
    return datetime.date.today().isoformat()


def build_sitemap(pages):
    rows = []
    for path in pages:
        route = route_for(path)
        if route in NOINDEX:
            continue
        html = read(path)
        # Image sitemap entries: the share image plus article covers and team photos in the page
        images = re.findall(r'<meta property="og:image" content="([^"]+)"', html)
        main = html.split('<main', 1)[-1]
        images += [SITE + src for src in re.findall(r'<img[^>]+src="(/Asset/img/(?:insights|team|manufacturing)/[^"]+)"', main)]
        images = list(dict.fromkeys(images))[:6]
        image_xml = ''.join(f'\n    <image:image>\n      <image:loc>{src}</image:loc>\n    </image:image>' for src in images)
        rows.append(f'  <url>\n    <loc>{SITE}{route}</loc>\n    <lastmod>{git_date(path)}</lastmod>{image_xml}\n  </url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + '\n'.join(rows) + '\n</urlset>\n')
    write_if_changed('sitemap.xml', xml)
    return len(rows)


def check_links(pages):
    routes = {route_for(p) for p in pages}
    problems = []
    for path in pages:
        html = read(path)
        for attr, url in re.findall(r'\b(href|src)="([^"]*)"', html):
            if re.match(r'^(https?:|mailto:|tel:|#|data:|javascript:)', url) or url == '':
                continue
            if not url.startswith('/'):
                problems.append(f'{path}: relative {attr} "{url}"')
                continue
            clean = re.sub(r'[?#].*$', '', url)
            if clean.endswith('.html') and clean != '/404.html':
                problems.append(f'{path}: link to .html URL "{url}"')
            elif clean.endswith('/'):
                if clean not in routes:
                    problems.append(f'{path}: broken page link "{url}"')
            else:
                fs = os.path.join(ROOT, clean.lstrip('/').replace('%20', ' '))
                if not os.path.exists(fs):
                    problems.append(f'{path}: missing file "{url}"')
    return problems


def main():
    css_hash = bundle_css()
    js_hash = bundle_js()
    head_tpl = read('tools/partials/head.html').replace('{{CSS_HASH}}', css_hash)
    header_tpl = read('tools/partials/header.html')
    footer_tpl = (read('tools/partials/footer.html')
                  .replace('{{JS_HASH}}', js_hash)
                  .replace('{{YEAR}}', str(datetime.date.today().year)))

    pages = find_pages()
    changed = 0
    for path in pages:
        route = route_for(path)
        url = SITE + route
        canonical = '' if route in NOINDEX else (f'    <link rel="canonical" href="{url}">\n'
                                                f'    <link rel="alternate" hreflang="en" href="{url}">\n'
                                                f'    <link rel="alternate" hreflang="x-default" href="{url}">\n')
        html = read(path)
        # Articles set their own author; every other page is authored by the company
        outside_head = re.sub(r'<!-- @head -->.*?<!-- @/head -->', '', html, flags=re.S)
        author = '' if '<meta name="author"' in outside_head else '    <meta name="author" content="Zudo Works">\n'
        meta = ''
        if route not in NOINDEX:
            meta = f'    <meta name="robots" content="{ROBOTS}">\n'
            kw = keywords_for(route, html)
            if kw:
                meta += f'    <meta name="keywords" content="{kw}">\n'
        head = head_tpl.replace('{{CANONICAL}}', canonical).replace('{{AUTHOR}}', author).replace('{{ROBOTS}}', meta)
        navbar_class = 'navbar' if route == '/' else 'navbar scrolled'
        header = nav_with_active(header_tpl.replace('{{NAVBAR_CLASS}}', navbar_class), route)

        html = replace_region(html, 'head', head, path)
        html = add_twitter_text(html)
        html = replace_region(html, 'header', header, path)
        html = replace_region(html, 'footer', footer_tpl, path)
        html = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + SITE + route + m.group(2), html)
        if write_if_changed(path, html):
            changed += 1

    count = build_sitemap(pages)
    problems = check_links(pages)
    print(f'{len(pages)} pages, {changed} updated, {count} in sitemap, css {css_hash}, js {js_hash}')
    for p in problems:
        print('  WARN', p)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
