"""Building blocks shared by the figure scenes (the same blocks the Insights cover layouts use)."""
import os, sys
LOGO = '<img src="../../../Asset/brand/zudo-works-logo.svg" alt="">'

def avatar(kind='person', size=64):
    skin, body = {'person': ('#F2C6A5', 'var(--solid)'), 'analyst': ('#D9A27E', 'var(--solid)'), 'worker': ('#F2C6A5', 'var(--solid)')}[kind]
    hair = {'person': '<path d="M30.500 43c-2-17 8-25 18-25 11 0 20 8 17.500 25-2-8-6-12-10-13-6 3-17 3-21 1-2 3-3.500 7-4.500 12z" fill="#1A1A2E"/>',
            'analyst': '<path d="M29 52c-5-20 6-35 19-35s24 14 19 35c-1-9-3-15-7-19-7 4-17 4-24 0-4 4-6 10-7 19z" fill="#3B2314"/>',
            'worker': '<path d="M27 37c1-13 10-20 21-20s20 7 21 20z" fill="#F9B21D"/><rect x="24" y="35" width="48" height="5" rx="2.500" fill="#E09E0F"/>'}[kind]
    cid = 'c' + kind
    return (f'<svg class="av" style="width:{size}px;height:{size}px" viewBox="0 0 96 96" fill="none"><circle cx="48" cy="48" r="46" fill="var(--tint)"/>'
            f'<clipPath id="{cid}"><circle cx="48" cy="48" r="46"/></clipPath><g clip-path="url(#{cid})">'
            f'<path d="M14 100c0-21 15-33 34-33s34 12 34 33z" fill="{body}"/><path d="M40 62h16v10c0 4-16 4-16 0z" fill="#E8B594"/>'
            f'<ellipse cx="48" cy="45" rx="16" ry="18" fill="{skin}"/>{hair}</g></svg>')

BRAND = f'<div class="brand" data-block>{LOGO}Zudo Works</div>'
def url(t='Read the full guide'): return f'<div class="url" data-block>{t} <b>zudoworks.com/insights</b><i>&rarr;</i></div>'
def facts(fs): return '<div class="facts">' + ''.join(f'<div class="fact" data-block><b>{a}</b><span>{b}</span></div>' for a, b in fs) + '</div>'

# ---------- heads
def head_col(style, d, who=None):
    w = f'<div class="who">{avatar(who)}<p>{d["take"]}</p></div>' if who else f'<div class="rule" style="align-self:stretch"></div><p class="take">{d["take"]}</p>'
    return (f'<div class="head {style}" data-block><span class="tag">{d["tag"]}</span><h1>{d["h1"]}</h1><p class="sub">{d["sub"]}</p>{w}'
            f'<div class="brand push">{LOGO}Zudo Works</div></div>')
def head_bar(d):
    return (f'<div class="head bar" data-block><div><span class="tag">{d["tag"]}</span><h1>{d["h1"]}</h1></div>'
            f'<div class="r"><p class="take">{d["take"]}</p><div class="brand">{LOGO}Zudo Works</div></div></div>')
def head_hero(d):
    return (f'<div class="head hero"><div data-block><span class="tag">{d["tag"]}</span><h1>{d["h1"]}</h1><p class="sub">{d["sub"]}</p></div>'
            f'<div class="takebox" data-block><small>{d.get("tk","Key point")}</small><p>{d["take"]}</p></div></div>')
def head_center(d):
    return f'<div class="head center" data-block><span class="tag">{d["tag"]}</span><h1>{d["h1"]}</h1><p class="sub">{d["sub"]}</p></div>'
def head_band(d, u='Read the full guide'):
    return (f'<div class="head band" data-block><div><span class="tag">{d["tag"]}</span><h1>{d["h1"]}</h1></div>'
            f'<div class="r"><div class="brand">{LOGO}Zudo Works</div><div class="url">{u} <b>zudoworks.com/insights</b></div></div></div>')

# ---------- mains
def li(items): return ''.join(f'<li>{x}</li>' for x in items)
def m_compare(a, b):
    f = lambda o, c: f'<div class="opt c" data-block style="--dot:{c}"><span class="k" style="color:{c}">{o["k"]}</span><h2>{o["h"]}</h2><p class="s">{o["s"]}</p><ul class="dots">{li(o["li"])}</ul></div>'
    return f'<div class="main m-compare">{f(a, "var(--accent)")}<div class="vs" data-block>vs</div>{f(b, "#C2540A")}</div>'
def m_split(a, b, c1='#1B5A96', c2='#0B6E4F'):
    f = lambda o, c: f'<div class="side" data-block style="--c1:{c}"><span class="k">{o["k"]}</span><h2>{o["h"]}</h2><p class="s">{o["s"]}</p><ul>{li(o["li"])}</ul></div>'
    return f'<div class="main m-split">{f(a, c1)}<div class="vs" data-block>vs</div>{f(b, c2)}</div>'
def m_steps(steps, cols=None, label='STEP'):
    cols = cols or ['#3CCB7F', '#F9B21D', '#F28B3C', '#F2686A']
    return f'<div class="main m-steps" style="--n:{len(steps)}">' + ''.join(
        f'<div class="step c" data-block style="--c1:{cols[i % len(cols)]}"><span class="n">{label} {i+1}</span><h2>{h}</h2><p>{p}</p>' + (f'<span class="v">{v}</span>' if v else '') + '</div>'
        for i, (h, p, v) in enumerate(steps)) + '</div>'
def m_rows(rows):
    out = ''
    for i, r in enumerate(rows):
        note = f'<p class="note">{r[2]}</p>' if len(r) > 2 and r[2] else ''
        out += f'<div class="row c{"" if note else " nn"}" data-block><div class="num">{i+1}</div><div><h2>{r[0]}</h2><p class="f">{r[1]}</p></div>{note}</div>'
    return f'<div class="main m-rows">{out}</div>'
def m_tiles(ts):
    return '<div class="main m-tiles">' + ''.join(f'<div class="tile c" data-block><div class="ic">{i}</div><b>{b}</b><span>{s}</span></div>' for i, b, s in ts) + '</div>'
def m_timeline(ps):
    return f'<div class="main m-timeline c" data-block style="--n:{len(ps)}">' + ''.join(
        f'<div class="tp"><span class="k">{k}</span><div class="rail"></div><div class="dot"></div><b>{b}</b><span>{s}</span></div>' for k, b, s in ps) + '</div>'
def m_stat(n, cap, minis):
    return (f'<div class="main m-stat"><div class="big" data-block><div class="n">{n}</div><div class="cap">{cap}</div></div><div class="stack">'
            + ''.join(f'<div class="mini c" data-block><b>{b}</b><span>{s}</span></div>' for b, s in minis) + '</div></div>')
def m_check(items, mark='&#10003;'):
    return '<div class="main m-check">' + ''.join(f'<div class="chk c" data-block><i>{mark}</i><span>{x}</span></div>' for x in items) + '</div>'
def m_matrix(qs, on=0):
    return '<div class="main m-matrix">' + ''.join(f'<div class="q c{" on" if i == on else ""}" data-block><span class="k">{k}</span><h2>{h}</h2><p>{p}</p></div>' for i, (k, h, p) in enumerate(qs)) + '</div>'
def m_funnel(bs, cols=None):
    cols = cols or ['#1B5A96', '#226DB4', '#2D7FCC', '#5A9BD8', '#7FB2E2']
    return '<div class="main m-funnel">' + ''.join(f'<div class="fb" data-block style="--w:{w}%;--c1:{cols[i % len(cols)]}">{b}<span>{s}</span></div>' for i, (b, s, w) in enumerate(bs)) + '</div>'
def m_ba(a, b):
    f = lambda o, cls: f'<div class="ba c {cls}" data-block><span class="k">{o["k"]}</span><h2>{o["h"]}</h2><ul class="dots">{li(o["li"])}</ul></div>'
    return f'<div class="main m-ba">{f(a, "before")}<div class="arrow" data-block>&rarr;</div>{f(b, "after")}</div>'
def m_bars(rows):
    return '<div class="main bars c" data-block>' + ''.join(f'<div class="br"><span>{l}</span><div class="track"><div class="fill" style="--w:{w}%"></div></div><span class="val">{v}</span></div>' for l, w, v in rows) + '</div>'
def m_table(hdr, rows, cols=None):
    cells = ''.join(f'<div class="th">{h}</div>' for h in hdr)
    for r in rows: cells += f'<div class="rh">{r[0]}</div>' + ''.join(f'<div>{x}</div>' for x in r[1:])
    cols = cols or ('1.05fr ' + ' '.join(['1fr'] * (len(hdr) - 1)))
    return f'<div class="main tbl c" data-block style="grid-template-columns:{cols};grid-template-rows:repeat({len(rows)+1},minmax(0,1fr))">{cells}</div>'
def m_hub(center, left, right):
    col = lambda xs: '<div class="stack">' + ''.join(f'<div class="mini c" data-block><b>{b}</b><span>{s}</span></div>' for b, s in xs) + '</div>'
    return f'<div class="main m-hub">{col(left)}<div class="hubc" data-block><b>{center[0]}</b><span>{center[1]}</span></div>{col(right)}</div>'
def m_chat(q, a, who='person', q2=None):
    extra = f'<div class="bub qn" data-block>{q2}</div>' if q2 else ''
    return f'<div class="main m-chat"><div class="bub qn" data-block>{q}</div><div class="arow" data-block>{avatar(who, 72)}<div class="bub an">{a}</div></div>{extra}</div>'
def m_score(cs):
    out = ''
    for k, h, n, items in cs:
        out += (f'<div class="sc c" data-block><span class="k">{k}</span><h2>{h}</h2><div class="rate">' + ''.join(f'<i class="{"on" if j < n else ""}"></i>' for j in range(5))
                + f'</div><ul class="dots">{li(items)}</ul></div>')
    return f'<div class="main m-score">{out}</div>'
def m_chev(cs, cols=None):
    cols = cols or ['#1B5A96', '#226DB4', '#0B6E4F', '#089949']
    return f'<div class="main m-chev" data-block style="--n:{len(cs)}">' + ''.join(f'<div class="cv" style="--c1:{cols[i % len(cols)]}"><small>STEP {i+1}</small><b>{b}</b><span>{s}</span></div>' for i, (b, s) in enumerate(cs)) + '</div>'
def m_quote(text, name, role, who='person'):
    return f'<div class="main quote c" data-block><div class="mark">&ldquo;</div><p>{text}</p><div class="by">{avatar(who)}<div><b>{name}</b>{role}</div></div></div>'
def m_vt(rs):
    return '<div class="main vt c" data-block>' + ''.join(f'<div class="vr"><span class="k">{k}</span><i class="d"></i><div><b>{b}</b><span>{s}</span></div></div>' for k, b, s in rs) + '</div>'
def m_dd(do, dont, hd=('Do', 'Avoid')):
    return (f'<div class="main m-dd"><div class="dd c" data-block><h2><i>&#10003;</i>{hd[0]}</h2><ul>{li(do)}</ul></div>'
            f'<div class="dd no c" data-block><h2><i>&#10005;</i>{hd[1]}</h2><ul>{li(dont)}</ul></div></div>')
def m_tiers(ts, on=1):
    return '<div class="main m-tiers">' + ''.join(f'<div class="tier c{" on" if i == on else ""}" data-block><span class="k">{k}</span><h2>{h}</h2><p class="s">{s}</p><ul class="dots">{li(items)}</ul></div>' for i, (k, h, s, items) in enumerate(ts)) + '</div>'
def m_pills(gs):
    return '<div class="main m-pills">' + ''.join(f'<div class="pg c" data-block><span class="k">{k}</span><div class="pl">' + ''.join(f'<span>{p}</span>' for p in ps) + '</div></div>' for k, ps in gs) + '</div>'

# ---------- assemble
def scene(theme, frame, head, main, fct=None, foot='', note=''):
    body = f'<div class="body{" wf" if fct else ""}">{main}{facts(fct) if fct else ""}</div>'
    return (f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="_base.css"><link rel="stylesheet" href="_kit.css"></head>\n'
            f'<!-- {note} -->\n<body class="theme-{theme}" data-strict><div class="scene kit f-{frame}">\n{head}\n{body}\n{foot}\n</div></body></html>\n')
def foot_url(t='Read the full guide'): return f'<div class="foot end">{url(t)}</div>'
def foot_both(t='Read the full guide'): return f'<div class="foot">{BRAND}{url(t)}</div>'

def build(kind, theme, d, main, fct=None, who=None, u='Read the full guide', note=''):
    if kind in ('left-card', 'left-bare', 'left-solid'):
        return scene(theme, 'left', head_col(kind.split('-')[1], d, who), main, fct, foot_url(u), note)
    if kind == 'right-card':  return scene(theme, 'right', head_col('card', d, who), main, fct, foot_url(u), note)
    if kind == 'right-solid': return scene(theme, 'right', head_col('solid', d, who), main, fct, foot_url(u), note)
    if kind == 'top-bar':     return scene(theme, 'top', head_bar(d), main, fct, foot_url(u), note)
    if kind == 'top-hero':    return scene(theme, 'top', head_hero(d), main, fct, foot_both(u), note)
    if kind == 'top-center':  return scene(theme, 'top', head_center(d), main, fct, foot_both(u), note)
    if kind == 'bottom-band': return scene(theme, 'bottom', head_band(d, u), main, fct, '', note)
    raise ValueError(kind)
