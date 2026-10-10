"""Figures for the Manufacturing section.

Content files call fig(...) to describe a diagram or an illustrative app screen. Each call registers a scene
and returns the <figure> HTML to embed. render_all() writes the scenes, checks their layout and renders them
to Asset/img/manufacturing/<name>.webp. Nothing here is a real screenshot: app screens are concept mockups.
"""
import hashlib, html as H, io, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa: F401,F403  (cover building blocks: m_compare, m_steps, m_rows, m_tiles, ...)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCENES = os.path.join(ROOT, 'tools/manufacturing/scenes')
OUT = os.path.join(ROOT, 'Asset/img/manufacturing')
FIGS = {}


def esc(t): return H.escape(str(t), quote=False)


def fig(name, main, alt, cap, w=1200, h=640, theme='blue', title=None, sub=None, fct=None, ui=False, hero=False, link=True):
    """Register a figure scene and return its embed HTML."""
    assert name not in FIGS, 'duplicate figure ' + name
    cls = 'scene fig' + (' t' if title else '') + (' f' if fct else '')
    head = f'<div class="ft" data-block><b>{title}</b>' + (f'<span>{sub}</span>' if sub else '') + '</div>' if title else ''
    scene = ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../insights/covers/_base.css">'
             '<link rel="stylesheet" href="../../insights/covers/_kit.css"><link rel="stylesheet" href="../_fig.css"></head>\n'
             f'<body class="theme-{theme}" data-strict style="--W:{w}px;--H:{h}px"><div class="{cls}">\n{head}\n{main}\n{facts(fct) if fct else ""}\n</div></body></html>\n')
    FIGS[name] = dict(scene=scene, w=w, h=h, hero=hero)
    badge = '<span class="mfg-badge">Concept screen</span> ' if ui else ''
    return (f'<figure class="mfg-fig{" mfg-fig--ui" if ui else ""}"><div class="mfg-fig-frame" tabindex="0" role="group" aria-label="Figure: scroll sideways on small screens">'
            f'<img src="/Asset/img/manufacturing/{name}.webp" alt="{H.escape(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
            f'<figcaption>{badge}{cap}</figcaption></figure>')


# ------------------------------------------------------------------ diagram blocks
def hero(d, right, solid=False):
    return (f'<div class="main hero{" solid" if solid else ""}"><div class="hl" data-block><span class="tag">{d["tag"]}</span><h1>{d["h1"]}</h1><p>{d["sub"]}</p>'
            f'<div class="brand push">{LOGO}Zudo Works</div></div><div class="hr">{right}</div></div>')


def m_lanes(stages, lanes):
    """Swimlane: stages across the top, one row per lane. A cell is None, (title, sub) or (title, sub, tone)."""
    out = '<div></div>' + ''.join(f'<div class="hd">{i+1}<i>&middot;</i>{s}</div>' for i, s in enumerate(stages))
    for name, cells in lanes:
        out += f'<div class="ln">{name}</div>'
        for c in cells:
            if not c: out += '<div class="cell"></div>'; continue
            tone = c[2] if len(c) > 2 else 'on'
            out += f'<div class="cell {tone}"><b>{c[0]}</b>' + (f'<span>{c[1]}</span>' if c[1] else '') + '</div>'
    return f'<div class="main lanes c" data-block style="--n:{len(stages)};padding:16px;grid-template-rows:auto">{out}</div>'


def m_arch(layers):
    """Stacked layers: (label, sub, [chips], highlighted)."""
    out = ''
    for l in layers:
        hi = len(l) > 3 and l[3]
        out += (f'<div class="layer{" hi" if hi else ""}" data-block><div class="ll"><b>{l[0]}</b><span>{l[1]}</span></div><div class="chips">'
                + ''.join(f'<span>{c}</span>' for c in l[2]) + '</div></div>')
    return f'<div class="main arch">{out}</div>'


def m_cols(cols):
    """Columns joined by arrows: (kicker, title, [items], highlighted)."""
    out = ''
    for c in cols:
        hi = len(c) > 3 and c[3]
        out += f'<div class="colx c{" hi" if hi else ""}" data-block><span class="k">{c[0]}</span><h3>{c[1]}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in c[2]) + '</ul></div>'
    return f'<div class="main cols" style="--n:{len(cols)}">{out}</div>'


def m_formula(eq, parts, result):
    return (f'<div class="main formula c" data-block><div class="eq">{eq}</div><div class="ex" style="--n:{len(parts)}">'
            + ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in parts) + f'</div><div class="res">{result}</div></div>')


# ------------------------------------------------------------------ illustrative app screens
def app(name, sub, nav, active, title, subtitle, content, actions='', side=True):
    aside = ''
    if side:
        aside = (f'<div class="aside"><div class="an">{name}<small>{sub}</small></div>' + ''.join(f'<a class="{"on" if n == active else ""}">{n}</a>' for n in nav)
                 + '<div class="sp">Concept screen</div></div>')
    return (f'<div class="main app{"" if side else " nos"}" data-block>{aside}<div class="amain"><div class="atop"><div><b>{title}</b><small>{subtitle}</small></div>'
            f'<div class="tr">{actions}<span class="illus">Illustrative</span></div></div><div class="acont">{content}</div></div></div>')


def kpis(items):
    out = ''
    for it in items:
        d = f' <em class="{it[3] if len(it) > 3 else "fl"}">{it[2]}</em>' if len(it) > 2 and it[2] else ''
        out += f'<div><span>{it[0]}</span><b>{it[1]}</b>{d}</div>'
    return f'<div class="kp" style="--n:{len(items)}">{out}</div>'


def cell(c):
    if isinstance(c, tuple):
        if c[0] == 'st': return f'<div><span class="st {c[1]}">{c[2]}</span></div>'
        if c[0] == 'r': return f'<div class="r">{c[1]}</div>'
        if c[0] == 's': return f'<div class="s">{c[1]}</div>'
        if c[0] == 'sn': return f'<div class="sn">{c[1]}</div>'
    return f'<div>{c}</div>'


def table(cols, headers, rows):
    out = ''.join(f'<div class="h{" r" if h.startswith(">") else ""}">{h.lstrip(">")}</div>' for h in headers)
    for r in rows:
        out += ''.join(cell(('s', c) if i == 0 and not isinstance(c, tuple) else c) for i, c in enumerate(r))
    return f'<div class="tb" style="--c:{cols}">{out}</div>'


def panel(title, inner, meta='', style=''):
    return f'<div class="pn" style="{style}"><h4>{title}<span>{meta}</span></h4>{inner}</div>'


def fields(items, n=3): return f'<div class="fld" style="--n:{n}">' + ''.join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in items) + '</div>'
def stepper(items): return f'<div class="stp" style="--n:{len(items)}">' + ''.join(f'<div class="{s}">{n}</div>' for n, s in items) + '</div>'
def listing(items): return '<div class="lst">' + ''.join(f'<div><i class="{t}"></i><div>{a}' + (f'<small>{b}</small>' if b else '') + '</div></div>' for t, a, b in items) + '</div>'
def g2(a, b, ratio='1.55fr'): return f'<div class="g2" style="--a:{ratio}">{a}{b}</div>'
def bars2(items): return '<div class="bar2">' + ''.join(f'<div><span>{l}</span><u><i style="--w:{w}%"></i></u><em>{v}</em></div>' for l, w, v in items) + '</div>'
def acts(*btns): return '<div class="acts">' + ''.join(f'<span class="{c}">{t}</span>' for c, t in btns) + '</div>'
def note(t): return f'<p class="note">{t}</p>'


def kanban(cols):
    out = ''
    for name, cards in cols:
        out += f'<div class="kc"><h4>{name}<span>{len(cards)}</span></h4>'
        for c in cards:
            tag = f'<span class="st {c[2][0]}">{c[2][1]}</span>' if len(c) > 2 and c[2] else ''
            out += f'<div class="kd"><b>{c[0]}</b><span>{c[1]}</span>{tag}</div>'
        out += '</div>'
    return f'<div class="kb" style="--n:{len(cols)}">{out}</div>'


def chat(msgs):
    out = ''
    for m in msgs:
        if m[0] == 'q': out += f'<div class="mq">{m[1]}</div>'
        else: out += f'<div class="ma">{m[1]}' + (f'<small>{m[2]}</small>' if len(m) > 2 and m[2] else '') + '</div>'
    return f'<div class="msg">{out}</div>'


def svg_line(series, labels, w=440, h=200, ymax=None, colors=('#226DB4', '#089949', '#E09E0F'), names=None, dashed=(), ymin=0):
    """Simple line chart. series: list of value lists (None allowed for gaps)."""
    vals = [v for s in series for v in s if v is not None]
    ymax = ymax or max(vals) * 1.12
    px, py, pw, ph = 44, 16, w - 56, h - 50
    X = lambda i: px + pw * i / (len(labels) - 1)
    Y = lambda v: py + ph * (1 - (v - ymin) / (ymax - ymin))
    g = ''.join(f'<line x1="{px}" x2="{px+pw}" y1="{py+ph*k/4:.1f}" y2="{py+ph*k/4:.1f}" stroke="#EEF1F5"/>'
                f'<text x="{px-8}" y="{py+ph*k/4+4:.1f}" font-size="13" fill="#7C869A" text-anchor="end">{ymin+(ymax-ymin)*(1-k/4):.0f}</text>' for k in range(5))
    g += ''.join(f'<text x="{X(i):.1f}" y="{h-8}" font-size="13" fill="#7C869A" text-anchor="middle">{l}</text>' for i, l in enumerate(labels))
    for si, s in enumerate(series):
        pts = [(X(i), Y(v)) for i, v in enumerate(s) if v is not None]
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        dash = ' stroke-dasharray="6 6"' if si in dashed else ''
        g += f'<path d="{d}" fill="none" stroke="{colors[si % 3]}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"{dash}/>'
        g += ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="#fff" stroke="{colors[si % 3]}" stroke-width="2"/>' for x, y in pts)
    if names:
        g += ''.join(f'<rect x="{px + 4 + i*150}" y="3" width="12" height="4" rx="2" fill="{colors[i % 3]}"/><text x="{px + 22 + i*150}" y="10" font-size="13" fill="#55607A" font-weight="600">{n}</text>' for i, n in enumerate(names))
    return f'<svg class="cht" viewBox="0 0 {w} {h}" font-family="Inter,sans-serif">{g}</svg>'


def svg_bars(vals, labels, w=440, h=200, ymax=None, hi=(), color='#226DB4', hicolor='#D9363A', target=None, unit=''):
    ymax = ymax or max(vals) * 1.15
    px, py, pw, ph = 44, 16, w - 56, h - 50
    bw = pw / len(vals) * 0.62
    g = ''.join(f'<line x1="{px}" x2="{px+pw}" y1="{py+ph*k/4:.1f}" y2="{py+ph*k/4:.1f}" stroke="#EEF1F5"/>'
                f'<text x="{px-8}" y="{py+ph*k/4+4:.1f}" font-size="13" fill="#7C869A" text-anchor="end">{ymax*(1-k/4):.0f}{unit}</text>' for k in range(5))
    for i, v in enumerate(vals):
        x = px + pw * (i + .5) / len(vals) - bw / 2; bh = ph * v / ymax
        g += f'<rect x="{x:.1f}" y="{py+ph-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="5" fill="{hicolor if i in hi else color}"/>'
        g += f'<text x="{x+bw/2:.1f}" y="{h-8}" font-size="13" fill="#7C869A" text-anchor="middle">{labels[i]}</text>'
    if target is not None:
        y = py + ph * (1 - target / ymax)
        g += f'<line x1="{px}" x2="{px+pw}" y1="{y:.1f}" y2="{y:.1f}" stroke="#089949" stroke-width="2" stroke-dasharray="6 5"/><text x="{px+pw}" y="{y-5:.1f}" font-size="13" fill="#067A3B" font-weight="700" text-anchor="end">target {target}{unit}</text>'
    return f'<svg class="cht" viewBox="0 0 {w} {h}" font-family="Inter,sans-serif">{g}</svg>'


def phone(title, sub, inner): return f'<div class="ph" data-block><div class="sc"><div class="ptop">{title}<small>{sub}</small></div><div class="pb">{inner}</div></div></div>'
def pf(label, value): return f'<div class="f"><span>{label}</span><b>{value}</b></div>'
def pscan(t): return f'<div class="scan">{t}</div>'
def pbtn(t, cls=''): return f'<div class="pbtn {cls}">{t}</div>'
def phones(ps, callouts=None):
    co = ''
    if callouts: co = '<div class="phc">' + ''.join(f'<div data-block><b>{b}</b><span>{s}</span></div>' for b, s in callouts) + '</div>'
    return f'<div class="main phones">{"".join(ps)}{co}</div>'


# ------------------------------------------------------------------ rendering
def _check_js(w, h):
    src = open(os.path.join(ROOT, 'tools/insights/covers/render_cover.py'), encoding='utf-8').read()
    js = src[src.index('CHECK = r"""') + len('CHECK = r"""'):]
    js = js[:js.index('"""')]
    js = js.replace('1600 - EDGE', f'{w} - EDGE').replace('900 - EDGE', f'{h} - EDGE')
    extra = r"""
  // 5. nothing inside a block may be cut off by it or hang outside it
  document.querySelectorAll('[data-block]').forEach(blk => {
    const rb = blk.getBoundingClientRect();
    blk.querySelectorAll('*').forEach(e => {
      if (e.closest('svg') && e.tagName !== 'svg') return;
      const r = e.getBoundingClientRect();
      if (!r.width || !r.height) return;
      if (r.bottom > rb.bottom + 1.5 || r.right > rb.right + 1.5 || r.top < rb.top - 1.5 || r.left < rb.left - 1.5) problems.push('cut off or outside its block: ' + name(e));
      const cs = getComputedStyle(e);
      if (cs.overflowY !== 'visible' && e.scrollHeight > e.clientHeight + 2) problems.push('content cut off vertically: ' + name(e));
    });
  });
  return [...new Set(problems)];
}
"""
    i = js.rindex('return [...new Set(problems)];')
    return js[:i] + extra.lstrip('\n')


def render_all(only=None, force=False):
    from PIL import Image
    from playwright.sync_api import sync_playwright
    os.makedirs(SCENES, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    hp = os.path.join(SCENES, '.hashes.json')
    hashes = json.load(open(hp)) if os.path.exists(hp) else {}
    deps = ''.join(open(os.path.join(ROOT, p), encoding='utf-8').read() for p in
                   ('tools/manufacturing/_fig.css', 'tools/insights/covers/_kit.css', 'tools/insights/covers/_base.css'))
    todo, failed = [], []
    for name, f in FIGS.items():
        if only and not any(o in name for o in only): continue
        hsh = hashlib.md5((f['scene'] + deps).encode()).hexdigest()
        out = os.path.join(OUT, name + '.webp')
        if not force and hashes.get(name) == hsh and os.path.exists(out): continue
        todo.append((name, f, hsh, out))
    if not todo:
        print(f'figures: {len(FIGS)} up to date'); return 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, f, hsh, out in todo:
            path = os.path.join(SCENES, name + '.html')
            open(path, 'w', encoding='utf-8', newline='\n').write(f['scene'])
            pg = b.new_page(viewport={'width': f['w'], 'height': f['h']}, device_scale_factor=2)
            pg.goto('file://' + path); pg.wait_for_timeout(250)
            probs = pg.evaluate(_check_js(f['w'], f['h']))
            if probs:
                failed.append((name, probs)); pg.close(); continue
            im = Image.open(io.BytesIO(pg.screenshot())).convert('RGB').resize((f['w'], f['h']), Image.LANCZOS)
            im.save(out, 'WEBP', quality=90, method=6)
            if f['hero']:
                t = (f['h'] - 630) // 2
                im.crop((0, t, 1200, t + 630)).save(os.path.join(ROOT, 'Asset/og', 'mfg-' + name + '.jpg'), 'JPEG', quality=88, optimize=True, progressive=True)
            hashes[name] = hsh; pg.close()
        b.close()
    json.dump(hashes, open(hp, 'w'), indent=0, sort_keys=True)
    print(f'figures: rendered {len(todo) - len(failed)} of {len(todo)} changed ({len(FIGS)} total)')
    for name, probs in failed:
        print('  LAYOUT FAIL', name); [print('     -', x) for x in probs[:6]]
    return len(failed)
