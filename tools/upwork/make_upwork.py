"""Build the Upwork capability guide: a 10-page A4 PDF and an 8-slide 16:9 PowerPoint.

    python tools/brochure/make_brochure.py   # once, for the shared images in tools/brochure/build/
    python tools/upwork/make_upwork.py       # writes tools/upwork/out/

Attach the files from tools/upwork/out/ to Upwork proposals. They are not published on the site.
Upwork rule: the documents carry no email, phone, WhatsApp, website, booking link or QR code, because
sharing contact details before a contract starts can get the account suspended. Keep it that way.
"""
import datetime, importlib.util, os, re, sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SHARED = os.path.join(ROOT, 'tools', 'brochure', 'build')
OUT = os.path.join(HERE, 'out')
PDF = os.path.join(OUT, 'Zudo-Works-Capabilities-Upwork.pdf')
PPTX = os.path.join(OUT, 'Zudo-Works-Capabilities-Upwork.pptx')
# Anything that looks like contact details must never reach these documents
FORBIDDEN = re.compile(r'@|zudoworks\.com|wa\.me|whatsapp\.com|\+91|63843|tel:|mailto:|bookings', re.I)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    os.makedirs(OUT, exist_ok=True)
    img = {k: os.path.join(SHARED, f) for k, f in (('handshake', 'handshake.png'), ('explorer', 'explorer.png'),
           ('lanes', 'lanes.png'), ('ops', 'ops.png'), ('cto', 'cto.jpg'), ('cert', 'cert.jpg'), ('logos', 'logos.png'))}
    img['logo'] = os.path.join(ROOT, 'Asset', 'brand', 'zudo-works-logo-512.png')
    missing = [p for p in img.values() if not os.path.exists(p)]
    if missing:
        sys.exit('Missing shared images; run python tools/brochure/make_brochure.py first:\n  ' + '\n  '.join(missing))

    brochure = load('make_brochure', os.path.join(ROOT, 'tools', 'brochure', 'make_brochure.py'))
    with open(os.path.join(HERE, 'guide.html'), encoding='utf-8') as f:
        doc = f.read()
    fills = {'{{YEAR}}': str(datetime.date.today().year), '{{IMG_HANDSHAKE}}': brochure.rel(img['handshake']),
             '{{IMG_EXPLORER}}': brochure.rel(img['explorer']), '{{IMG_LANES}}': brochure.rel(img['lanes']),
             '{{IMG_CTO}}': brochure.rel(img['cto']), '{{IMG_CERT}}': brochure.rel(img['cert'])}
    for k, v in fills.items():
        doc = doc.replace(k, v)
    left = re.findall(r'\{\{[A-Z_]+\}\}', doc)
    assert not left, f'unfilled placeholders: {left}'
    body = re.sub(r'<!--.*?-->|<style>.*?</style>|<[^>]+>', ' ', doc, flags=re.S)
    hit = FORBIDDEN.search(body)
    assert not hit, f'contact details in the guide text: "{body[max(0, hit.start() - 40):hit.end() + 40]}"'
    filled = os.path.join(OUT, 'guide.filled.html')
    with open(filled, 'w', encoding='utf-8') as f:
        f.write(doc)

    httpd, base = brochure.serve()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            page = b.new_page()
            page.goto(base + '/tools/upwork/out/guide.filled.html', wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            pages = page.evaluate('document.querySelectorAll(".page").length')
            over = page.evaluate('''[...document.querySelectorAll(".page")].map((p, i) => {
                const b = p.getBoundingClientRect().bottom - 30;
                const kids = [...p.querySelectorAll("*")].filter(e => !e.closest(".foot, .cover-art, .cover-bottom"));
                return kids.some(e => e.getBoundingClientRect().bottom > b) ? i + 1 : 0; }).filter(Boolean)''')
            page.pdf(path=PDF, format='A4', print_background=True, prefer_css_page_size=True)
            b.close()
    finally:
        httpd.shutdown()
    os.remove(filled)

    deck = load('deck_upwork', os.path.join(HERE, 'deck_upwork.py'))
    slides = deck.build(PPTX, img)
    print(f'PDF  {os.path.relpath(PDF, ROOT)}: {pages} pages, {os.path.getsize(PDF) // 1024} KB'
          + (f', content near the bottom edge on pages {over}' if over else ''))
    print(f'PPTX {os.path.relpath(PPTX, ROOT)}: {slides} slides, {os.path.getsize(PPTX) // 1024} KB')


if __name__ == '__main__':
    sys.exit(main())
