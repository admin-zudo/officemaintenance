"""Build the Zudo Works brochure (12-page A4 PDF) and company deck (8-slide 16:9 PPTX).

    python tools/brochure/make_brochure.py

Needs: playwright (with Chromium), Pillow, python-pptx, qrcode, pymupdf. Outputs:

    Asset/brochure/zudo-works-brochure.pdf      from tools/brochure/brochure.html
    Asset/brochure/pages/page-01.webp ...       page images for the on-site reader (#brochure-viewer)
    Asset/brochure/zudo-works-company-deck.pptx from tools/brochure/deck.py

Images come from the site itself (Asset/), plus a screenshot of the scenario explorer and a Zoho logo
wall rendered here into tools/brochure/build/. Run tools/build.py first so the explorer is current.
"""
import base64, datetime, functools, html, http.server, importlib.util, os, re, socketserver, sys, threading

from PIL import Image
import qrcode
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BUILD = os.path.join(HERE, 'build')
OUT = os.path.join(ROOT, 'Asset', 'brochure')
PDF = os.path.join(OUT, 'zudo-works-brochure.pdf')
PPTX = os.path.join(OUT, 'zudo-works-company-deck.pptx')
QR_URL = 'https://zudoworks.com/contact/?utm_source=brochure&utm_medium=document&utm_campaign=company_brochure'

LOGOS = ['zoho-one', 'zoho-crm', 'zoho-creator', 'zoho-books', 'zoho-analytics', 'zoho-flow', 'zoho-desk', 'zoho-projects',
         'zoho-people', 'zoho-salesiq', 'zoho-catalyst', 'zoho-forms', 'zoho-sign', 'zoho-cliq', 'zoho-erp']
# Example flows shown in the brochure: (industry slug, flow index)
FLOWS = [('manufacturing', 0), ('real-estate', 0), ('legal', 0), ('customer-support', 0)]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    handler = functools.partial(Quiet, directory=ROOT)
    httpd = socketserver.ThreadingTCPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f'http://127.0.0.1:{httpd.server_address[1]}'


def to_file(src, name, size=None, fmt='PNG', quality=88):
    """Copy a site image into build/ as PNG or JPEG (python-pptx cannot read WebP)."""
    im = Image.open(os.path.join(ROOT, src))
    im = im.convert('RGBA' if fmt == 'PNG' else 'RGB')
    if size:
        im.thumbnail(size, Image.LANCZOS)
    path = os.path.join(BUILD, name)
    im.save(path, fmt, **({'quality': quality, 'optimize': True} if fmt == 'JPEG' else {'optimize': True}))
    return path


def qr_png():
    img = qrcode.make(QR_URL, box_size=12, border=1)
    path = os.path.join(BUILD, 'qr.png')
    img.save(path)
    return path


def render_shots(browser, base):
    ctx = browser.new_context(viewport={'width': 1440, 'height': 1000}, device_scale_factor=2)
    ctx.add_init_script("try { localStorage.setItem('zudo_cookie_consent', 'accepted'); } catch (e) {}")
    page = ctx.new_page()
    page.route('**/*googletagmanager*/**', lambda r: r.abort())
    page.route('**/salesiq*/**', lambda r: r.abort())

    # Scenario explorer, manufacturing flow, once the layer is wired and a few steps have run
    page.goto(base + '/manufacturing-software/', wait_until='networkidle')
    page.add_style_tag(content='.side-contact,.lp-bar,.cookie-banner,#cookie-consent{display:none!important}')
    fx = page.locator('[data-fx]')
    fx.scroll_into_view_if_needed()
    page.wait_for_selector('[data-fx-stage].is-wired', timeout=20000)
    page.wait_for_timeout(5200)
    fx.screenshot(path=os.path.join(BUILD, 'explorer.png'))

    # Zoho logo wall
    cells = ''.join(f'<li><img src="/Asset/zoho/{n}.svg" alt=""></li>' for n in LOGOS)
    with open(os.path.join(BUILD, 'logos.html'), 'w', encoding='utf-8') as f:
        f.write('<!doctype html><meta charset="utf-8"><style>body{margin:0;background:#fff}'
                'ul{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:0;padding:18px;list-style:none;width:1100px}'
                'li{display:flex;align-items:center;justify-content:center;height:70px;border:1px solid #E3E8EF;border-radius:12px}'
                'img{height:34px;width:auto;max-width:150px}</style><ul id="w">' + cells + '</ul>')
    page.goto(base + '/tools/brochure/build/logos.html', wait_until='networkidle')
    page.locator('#w').screenshot(path=os.path.join(BUILD, 'logos.png'))
    ctx.close()


def flows_html():
    sc = load('scenarios', os.path.join(ROOT, 'tools', 'solutions', 'scenarios.py'))
    by = {i['slug']: i for i in sc.INDUSTRIES}
    chips = ''.join(f'<span>{html.escape(i["name"])}</span>' for i in sc.INDUSTRIES)
    out = []
    for slug, n in FLOWS:
        ind = by[slug]
        fl = ind['flows'][n]
        steps = '<i></i>'.join(f'<span class="{"ai" if st[0] == "ai" else ""}">{html.escape(st[1])}</span>' for st in fl['steps'])
        out.append(f'<div class="flow"><div class="flow-h"><h3>{html.escape(fl["short"])}</h3><span class="chip">{html.escape(ind["name"])}</span></div>'
                   f'<p>{html.escape(fl["problem"])}</p><div class="steps">{steps}</div>'
                   f'<p class="res">Result: {html.escape(fl["result"])}</p></div>')
    return chips, ''.join(out), sc


def rel(path):
    return '/' + os.path.relpath(path, ROOT).replace('\\', '/')


def main():
    os.makedirs(BUILD, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    img = {
        'handshake': to_file('Asset/img/handshake-illustration.webp', 'handshake.png', (1800, 1800)),
        'ops': to_file('Asset/img/manufacturing/hub-manufacturing-ops.webp', 'ops.png'),
        'lanes': to_file('Asset/img/manufacturing/hub-manufacturing-lanes.webp', 'lanes.png'),
        'mcp': to_file('Asset/img/insights/zoho-mcp-claude-chatgpt.webp', 'mcp.jpg', (1200, 1200), 'JPEG'),
        'cto': to_file('Asset/img/team/arunkumar-v.webp', 'cto.jpg', (900, 900), 'JPEG'),
        'cert': to_file('Asset/img/team/master-of-creator-certificate.webp', 'cert.jpg', (700, 1000), 'JPEG'),
        'logo': os.path.join(ROOT, 'Asset', 'brand', 'zudo-works-logo-512.png'),
        'qr': qr_png(),
    }
    httpd, base = serve()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            render_shots(browser, base)
            img['explorer'] = os.path.join(BUILD, 'explorer.png')
            img['logos'] = os.path.join(BUILD, 'logos.png')

            chips, flows, sc = flows_html()
            with open(os.path.join(HERE, 'brochure.html'), encoding='utf-8') as f:
                doc = f.read()
            with open(img['qr'], 'rb') as f:
                qr_uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()
            fills = {'{{YEAR}}': str(datetime.date.today().year), '{{INDUSTRIES}}': chips, '{{FLOWS}}': flows, '{{QR}}': qr_uri,
                     '{{IMG_HANDSHAKE}}': rel(img['handshake']), '{{IMG_EXPLORER}}': rel(img['explorer']),
                     '{{IMG_LOGOS}}': rel(img['logos']), '{{IMG_OPS}}': rel(img['ops']), '{{IMG_LANES}}': rel(img['lanes']),
                     '{{IMG_MCP}}': rel(img['mcp']), '{{IMG_CTO}}': rel(img['cto']), '{{IMG_CERT}}': rel(img['cert'])}
            for k, v in fills.items():
                doc = doc.replace(k, v)
            left = re.findall(r'\{\{[A-Z_]+\}\}', doc)
            assert not left, f'unfilled placeholders in brochure.html: {left}'
            with open(os.path.join(BUILD, 'brochure.filled.html'), 'w', encoding='utf-8') as f:
                f.write(doc)

            page = browser.new_page()
            page.goto(base + '/tools/brochure/build/brochure.filled.html', wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            pages = page.evaluate('document.querySelectorAll(".page").length')
            over = page.evaluate('''[...document.querySelectorAll(".page")].map((p, i) => {
                const b = p.getBoundingClientRect().bottom - 30;
                const kids = [...p.querySelectorAll("*")].filter(e => !e.closest(".foot, .back-foot, .cover-art, .back-art"));
                return kids.some(e => e.getBoundingClientRect().bottom > b) ? i + 1 : 0; }).filter(Boolean)''')
            page.pdf(path=PDF, format='A4', print_background=True, prefer_css_page_size=True)
            browser.close()
    finally:
        httpd.shutdown()

    # Page images for the brochure reader in tools/partials/footer.html (data-pages must match)
    import pymupdf
    pages_dir = os.path.join(OUT, 'pages')
    os.makedirs(pages_dir, exist_ok=True)
    with pymupdf.open(PDF) as doc:
        for i, pg in enumerate(doc):
            pix = pg.get_pixmap(matrix=pymupdf.Matrix(1100 / pg.rect.width, 1100 / pg.rect.width))
            im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
            im.save(os.path.join(pages_dir, f'page-{i + 1:02d}.webp'), 'WEBP', quality=82, method=6)

    deck = load('deck', os.path.join(HERE, 'deck.py'))
    slides = deck.build(PPTX, img, sc)
    print(f'PDF  {os.path.relpath(PDF, ROOT)}: {pages} pages, {os.path.getsize(PDF) // 1024} KB'
          + (f', content near the bottom edge on pages {over}' if over else ''))
    print(f'PPTX {os.path.relpath(PPTX, ROOT)}: {slides} slides, {os.path.getsize(PPTX) // 1024} KB')


if __name__ == '__main__':
    sys.exit(main())
