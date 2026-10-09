"""Render an article cover scene to the two image files the site uses. Run from the repo root.

    python tools/insights/covers/render_cover.py <slug>

Reads  tools/insights/covers/<slug>.html  (a 1600x900 scene; start from _template-panel.html)
Writes Asset/img/insights/<slug>.webp     (1600x900, article and card image)
       Asset/og/<slug>.jpg                (1200x630, social sharing image)
Needs: pip install playwright pillow, plus a Chromium that Playwright can find.

Scenes whose <body> has the attribute data-strict are checked before anything is written: no block may
overlap or crowd another, nothing may be cut off by the image edge, and no text may spill out of its box.
The script exits with an error and a list of problems if the layout is not clean. Fix the scene and re-run.
"""
import io, os, sys
from PIL import Image
from playwright.sync_api import sync_playwright

slug = sys.argv[1]
src = os.path.abspath(f'tools/insights/covers/{slug}.html')
out_dir = sys.argv[2] if len(sys.argv) > 2 else None   # optional: write previews here instead of into the site

CHECK = r"""
() => {
  const GAP = 14, EDGE = 28, problems = [];
  const name = e => (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : e.tagName.toLowerCase())
      + ' "' + (e.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 28) + '"';
  const box = e => e.getBoundingClientRect();
  const hit = (a, b, g) => a.left < b.right + g && b.left < a.right + g && a.top < b.bottom + g && b.top < a.bottom + g;
  // 1. top-level blocks must not overlap or crowd each other, and must sit inside the image
  const blocks = [...document.querySelectorAll('[data-block]')];
  blocks.forEach((a, i) => {
    const ra = box(a);
    if (ra.left < EDGE || ra.top < EDGE || ra.right > 1600 - EDGE || ra.bottom > 900 - EDGE) problems.push('too close to the image edge: ' + name(a));
    blocks.slice(i + 1).forEach(b => { if (!a.contains(b) && !b.contains(a) && hit(ra, box(b), GAP)) problems.push('overlapping or crowded: ' + name(a) + ' and ' + name(b)); });
  });
  // 2. inside each block: children must not overlap each other or spill outside
  blocks.forEach(blk => {
    const rb = box(blk), kids = [...blk.children].filter(k => k.tagName !== 'svg' || k.getBoundingClientRect().width < 200);
    kids.forEach((a, i) => {
      const ra = box(a);
      if (ra.width === 0) return;
      if (ra.left < rb.left - 1 || ra.right > rb.right + 1 || ra.top < rb.top - 1 || ra.bottom > rb.bottom + 1) problems.push('spills out of its box: ' + name(a));
      kids.slice(i + 1).forEach(b => { const r2 = box(b); if (r2.width && hit(ra, r2, -1)) problems.push('overlapping inside a box: ' + name(a) + ' and ' + name(b)); });
    });
  });
  // 3. no text cut off or wider than its container
  document.querySelectorAll('[data-block] *').forEach(e => {
    if (e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).display !== 'inline' && e.tagName !== 'svg' && !e.closest('svg')) problems.push('text wider than its container: ' + name(e));
  });
  // 4. round nodes: text must stay inside the circle, not just the square around it
  document.querySelectorAll('.node').forEach(n => {
    const r = box(n), cx = r.left + r.width / 2, cy = r.top + r.height / 2, rad = r.width / 2 - 8;
    [...n.children].forEach(k => { const b = box(k);
      [[b.left, b.top], [b.right, b.top], [b.left, b.bottom], [b.right, b.bottom]].forEach(([x, y]) => {
        if (Math.hypot(x - cx, y - cy) > rad && k.tagName !== 'svg') problems.push('text touches the circle edge: ' + name(k)); }); });
  });
  return [...new Set(problems)];
}
"""


def shot(page, w, h, zoom):
    page.add_style_tag(content=f'.scene{{--z:{zoom}}}')
    page.wait_for_timeout(400)
    png = page.screenshot(clip={'x': (1600 - w) / 2, 'y': (900 - h) / 2, 'width': w, 'height': h})
    return Image.open(io.BytesIO(png)).convert('RGB').resize((w, h), Image.LANCZOS)


with sync_playwright() as p:
    browser = p.chromium.launch()
    # Rendered at double size and scaled down, so text and edges stay sharp.
    page = browser.new_page(viewport={'width': 1600, 'height': 900}, device_scale_factor=2)
    page.goto('file://' + src)
    page.wait_for_timeout(400)
    strict = page.evaluate("document.body.hasAttribute('data-strict')")
    if strict:
        problems = page.evaluate(CHECK)
        if problems:
            browser.close()
            sys.exit('Layout check failed for ' + slug + ':\n  - ' + '\n  - '.join(problems))
    cover = out_dir + f'/{slug}.png' if out_dir else f'Asset/img/insights/{slug}.webp'
    og = out_dir + f'/{slug}-og.png' if out_dir else f'Asset/og/{slug}.jpg'
    c, o = shot(page, 1600, 900, 1), shot(page, 1200, 630, 0.74 if strict else 0.8)
    if out_dir:
        c.save(cover); o.save(og)
    else:
        c.save(cover, 'WEBP', quality=92, method=6)
        o.save(og, 'JPEG', quality=90, optimize=True, progressive=True)
    browser.close()
print('layout check passed;' if strict else 'no layout check (old-style scene);', 'wrote', cover, og)
