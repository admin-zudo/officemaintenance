"""Render an article cover scene to the two image files the site uses. Run from the repo root.

    python tools/insights/covers/render_cover.py <slug>

Reads  tools/insights/covers/<slug>.html  (a 1600x900 scene; copy an existing one as the starting point)
Writes Asset/img/insights/<slug>.webp     (1600x900, article and card image)
       Asset/og/<slug>.jpg                (1200x630, social sharing image)
Needs: pip install playwright pillow, plus a Chromium that Playwright can find.
"""
import io, os, sys
from PIL import Image
from playwright.sync_api import sync_playwright

slug = sys.argv[1]
src = os.path.abspath(f'tools/insights/covers/{slug}.html')


def shot(page, w, h, zoom):
    page.add_style_tag(content=f'.scene{{--z:{zoom}}}')
    page.wait_for_timeout(400)
    png = page.screenshot(clip={'x': (1600 - w) / 2, 'y': (900 - h) / 2, 'width': w, 'height': h})
    return Image.open(io.BytesIO(png)).convert('RGB')


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1600, 'height': 900})
    page.goto('file://' + src)
    shot(page, 1600, 900, 1).save(f'Asset/img/insights/{slug}.webp', 'WEBP', quality=82, method=6)
    shot(page, 1200, 630, 0.8).save(f'Asset/og/{slug}.jpg', 'JPEG', quality=84, optimize=True, progressive=True)
    browser.close()
print('wrote', f'Asset/img/insights/{slug}.webp', f'Asset/og/{slug}.jpg')
