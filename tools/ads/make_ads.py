"""Render the square ad images (800 x 800 PNG) for the manufacturing campaign.

    python tools/brochure/make_brochure.py   # once, for the dashboard and explorer images it reuses
    python tools/ads/make_ads.py             # writes tools/ads/out/zudo-mfg-ad-a.png, -b.png, -c.png

Upload the files from tools/ads/out/ to the ad platform. They are not published on the site.
"""
import functools, http.server, os, socketserver, sys, threading

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, 'out')


def main():
    os.makedirs(OUT, exist_ok=True)

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass

    httpd = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=ROOT))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={'width': 800, 'height': 900}, device_scale_factor=1)
            pg.goto(f'http://127.0.0.1:{httpd.server_address[1]}/tools/ads/ads.html', wait_until='networkidle')
            pg.evaluate('document.fonts.ready')
            for k in ('a', 'b', 'c'):
                path = os.path.join(OUT, f'zudo-mfg-ad-{k}.png')
                pg.locator(f'#{k}').screenshot(path=path)
                print(os.path.relpath(path, ROOT), os.path.getsize(path) // 1024, 'KB')
            b.close()
    finally:
        httpd.shutdown()


if __name__ == '__main__':
    sys.exit(main())
