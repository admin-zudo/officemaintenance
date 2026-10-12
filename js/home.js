/* ============================================================
   Homepage scenario explorer
   A visitor picks a real-world problem. The apps first appear as a
   knot of hand-wired systems; the integration and AI layer draws in,
   the knot dissolves, each app plugs into the layer, and a packet
   runs the solution step by step. Where data flows back to an
   earlier app, a green sync runs back through the layer. Until the
   visitor picks one, it moves through the scenarios on its own.
   These are example flows, not client case studies.
   ============================================================ */

(function () {
  'use strict';

  /* The flows (five per industry) live in tools/solutions/scenarios.py, which writes
     /solutions/scenarios.json for this explorer and the /solutions/ page for search.
     Each step: [logo or icon, label, what happens, optional [earlier step index, what syncs back]]. */
  var ICONS = {
    web: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    ads: '<path d="M3 11v2a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1z"/><path d="M15 9a3 3 0 0 1 0 6M18 6a7 7 0 0 1 0 12"/>',
    tablet: '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M11 18h2"/>',
    deluge: '<path d="m8 6-6 6 6 6M16 6l6 6-6 6M14 4l-4 16"/>',
    chat: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.6A8 8 0 1 1 21 12z"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    cart: '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h7.6a2 2 0 0 0 2-1.6L21 8H6"/>',
    mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    doc: '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
    ai: '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>'
  };
  var AI_NOTE = 'Zoho Zia, or Claude and ChatGPT through Zoho MCP.';

  var root = document.querySelector('[data-fx]');
  if (!root) return;

  fetch('/solutions/scenarios.json')
    .then(function (r) { return r.json(); })
    .then(start)
    .catch(function (err) { root.classList.add('is-error'); if (window.console) console.error('Explorer:', err); });

  function start(all) {
  /* A page can narrow the flows with data-fx-filter on a parent:
     "app:zoho-creator" (flows using that app; several allowed, comma-separated),
     "industry:legal", or "sync" (flows where data syncs back). */
  var host = root.closest('[data-fx-filter]'), only = host ? host.getAttribute('data-fx-filter') : '';
  var kind = only.split(':')[0], vals = (only.split(':')[1] || '').split(',');
  var S = all.filter(function (s) {
    if (kind === 'industry') return vals.indexOf(s.slug) >= 0;
    if (kind === 'sync') return s.steps.some(function (st) { return st[3]; });
    if (kind === 'app') return s.steps.some(function (st) { return vals.indexOf(st[0]) >= 0; });
    return true;
  });
  if (!S.length) S = all;

  var stage = root.querySelector('[data-fx-stage]');
  var trigger = root.querySelector('.fx-trigger');
  var list = root.querySelector('#fx-list');
  var indLabel = root.querySelector('[data-fx-ind]');
  var problemEl = root.querySelector('[data-fx-problem]');
  var solutionEl = root.querySelector('[data-fx-solution]');
  var solutionRow = root.querySelector('.fx-layer--solution');
  var trigShort = root.querySelector('[data-fx-short]');
  var capLabel = root.querySelector('[data-fx-label]');
  var capText = root.querySelector('[data-fx-text]');
  var capNote = root.querySelector('[data-fx-note]');
  var caption = root.querySelector('.fx-caption');
  var progress = root.querySelector('[data-fx-progress]');
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var TOP_Y = 24, RAIL_Y = 52, BOTTOM_Y = 80; // rows and the layer, percent of the stage height
  var RAIL = 14;                               // half the rail height, px
  var CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>';

  var current = 0, auto = !reducedMotion, visible = true;
  var clock = 0, lastT = null, holdUntil = 0, gen = 0, queue = [], anims = [];
  var PAUSE_MS = 5000;
  var POS = [], cluster = [];
  var HOLD_MS = 5000;

  /* Everything is timed on a play clock. It stands still while the explorer is
     off screen, and for five seconds after a visitor taps the map or the layers,
     so they can read before the story moves on. */
  function later(fn, ms) { queue.push({ due: clock + ms, fn: fn }); }
  function clear() {
    gen++;
    queue = [];
    anims = [];
    progress.classList.remove('is-running');
  }
  // Only once the tangle has resolved and the cards are plugged in
  function pause() {
    if (!stage.classList.contains('is-wired')) return;
    holdUntil = performance.now() + PAUSE_MS;
  }
  function resume() { holdUntil = 0; }
  var secsEl = root.querySelector('[data-fx-secs]'), shownSecs = -1;
  function showSecs(left) {
    var n = Math.max(1, Math.ceil(left / 1000));
    if (n === shownSecs) return;
    shownSecs = n;
    var tip = n + (n === 1 ? ' second' : ' seconds') + ' remaining';
    secsEl.textContent = n + 's';
    secsEl.setAttribute('data-tip', tip);
    secsEl.setAttribute('aria-label', tip);
  }
  function loop(t) {
    var now = performance.now(), paused = now < holdUntil;
    if (paused) showSecs(holdUntil - now); else shownSecs = -1;
    if (lastT !== null && visible && !paused) clock += Math.min(100, t - lastT);
    lastT = t;
    root.classList.toggle('is-paused', paused);
    var due = queue.filter(function (q) { return q.due <= clock; });
    queue = queue.filter(function (q) { return q.due > clock; });
    due.forEach(function (q) { q.fn(); });
    var running = anims;
    anims = [];
    running.forEach(function (a) { if (!a()) anims.push(a); });
    requestAnimationFrame(loop);
  }
  function esc(t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }
  function rnd(a, b) { return a + Math.random() * (b - a); }

  function art(a, label) {
    if (a.indexOf('zoho-') === 0) return '<img src="/Asset/zoho/' + a + '.svg" alt="" width="84" height="28">';
    return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ICONS[a] + '</svg><b>' + esc(label) + '</b>';
  }

  /* Serpentine layout: the first half of the cards above the layer, left to
     right; the rest (ending with the result) below it, right to left */
  function layout(count) {
    var top = Math.ceil(count / 2), bottom = count - top, out = [];
    function xs(n) {
      if (n === 1) return [50];
      var a = []; var pad = stage.clientWidth < 420 ? 19 : 15;
      for (var i = 0; i < n; i++) a.push(pad + i * (100 - 2 * pad) / (n - 1)); return a;
    }
    xs(top).forEach(function (x) { out.push([x, TOP_Y]); });
    xs(bottom).reverse().forEach(function (x) { out.push([x, BOTTOM_Y]); });
    return out;
  }

  /* ── Two pickers: the industry, then a problem within that industry ── */
  var industries = [], menus = [];
  S.forEach(function (s) { if (industries.indexOf(s.ind) < 0) industries.push(s.ind); });

  function menu(btn, ul, onPick) {
    var m = { btn: btn, ul: ul };
    function items() { return Array.prototype.slice.call(ul.querySelectorAll('[role="option"]')); }
    m.open = function () {
      menus.forEach(function (o) { if (o !== m && !o.ul.hidden) o.close(); });
      ul.hidden = false;
      btn.setAttribute('aria-expanded', 'true');
      btn.parentNode.classList.add('is-open');
      var sel = ul.querySelector('[aria-selected="true"]') || items()[0];
      sel.focus();
      sel.scrollIntoView({ block: 'nearest' });
    };
    m.close = function (focus) {
      ul.hidden = true;
      btn.setAttribute('aria-expanded', 'false');
      btn.parentNode.classList.remove('is-open');
      if (focus) btn.focus();
    };
    btn.addEventListener('click', function () { ul.hidden ? m.open() : m.close(); });
    ul.addEventListener('click', function (e) {
      var o = e.target.closest('[role="option"]');
      if (o) { m.close(true); onPick(o.getAttribute('data-v')); }
    });
    ul.addEventListener('keydown', function (e) {
      var all = items(), k = all.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); all[Math.min(all.length - 1, k + 1)].focus(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); all[Math.max(0, k - 1)].focus(); }
      else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); m.close(true); onPick(document.activeElement.getAttribute('data-v')); }
      else if (e.key === 'Escape' || e.key === 'Tab') { m.close(e.key === 'Escape'); }
    });
    menus.push(m);
  }
  document.addEventListener('click', function (e) {
    menus.forEach(function (m) { if (!m.ul.hidden && !m.btn.parentNode.contains(e.target)) m.close(); });
  });

  var indList = root.querySelector('.fx-ind-list');
  indList.innerHTML = industries.map(function (ind) {
    return '<li class="fx-option" role="option" tabindex="-1" data-v="' + esc(ind) + '">' + esc(ind) + '</li>';
  }).join('');
  // Picking an industry loads its first problem
  menu(root.querySelector('.fx-ind-trigger'), indList, function (ind) {
    for (var i = 0; i < S.length; i++) if (S[i].ind === ind) { choose(i); return; }
  });
  menu(trigger, list, function (v) { choose(+v); });

  // The problem list shows only the chosen industry
  function fillPickers() {
    var ind = S[current].ind;
    indLabel.textContent = ind;
    trigShort.textContent = S[current].short;
    indList.querySelectorAll('[role="option"]').forEach(function (o) {
      o.setAttribute('aria-selected', o.getAttribute('data-v') === ind ? 'true' : 'false');
    });
    list.innerHTML = '<li class="fx-group" role="presentation">' + esc(ind) + '</li>' + S.map(function (s, i) {
      return s.ind !== ind ? '' : '<li class="fx-option" role="option" tabindex="-1" data-v="' + i + '" aria-selected="' +
        (i === current) + '">' + esc(s.short) + '</li>';
    }).join('');
  }

  /* ── Geometry: the SVG uses the stage's pixel size so lines stay crisp ── */
  function size() { return { w: stage.clientWidth || 1, h: stage.clientHeight || 1 }; }
  function xy(pt, z) { return [pt[0] * z.w / 100, pt[1] * z.h / 100]; }
  function f(n) { return n.toFixed(1); }
  function edge(n, z) { return z.h * RAIL_Y / 100 + (POS[n][1] < RAIL_Y ? -RAIL : RAIL); }

  function plugD(n, z) {
    var p = xy(POS[n], z);
    return 'M' + f(p[0]) + ' ' + f(p[1]) + ' L' + f(p[0]) + ' ' + f(edge(n, z));
  }
  // Any card to any other: down to the layer, along it, and up into the other card
  function routeD(a, b, z) {
    var p = xy(POS[a], z), q = xy(POS[b], z), e = edge(a, z);
    if (Math.abs(p[0] - q[0]) < 1) return 'M' + f(p[0]) + ' ' + f(p[1]) + ' L' + f(q[0]) + ' ' + f(q[1]);
    return 'M' + f(p[0]) + ' ' + f(p[1]) + ' L' + f(p[0]) + ' ' + f(e) + ' L' + f(q[0]) + ' ' + f(e) + ' L' + f(q[0]) + ' ' + f(q[1]);
  }
  function knots(z) {
    var out = '', cx = z.w / 2, cy = z.h * 0.5;
    for (var k = 0; k < 12; k++) {
      var a = xy(cluster[k % cluster.length], z), b = xy(cluster[(k * 5 + 2) % cluster.length], z);
      var ang = rnd(0, Math.PI * 2), r1 = rnd(0.25, 0.5), r2 = rnd(0.25, 0.5);
      var c1 = [cx + Math.cos(ang) * r1 * z.w, cy + Math.sin(ang) * r1 * z.h];
      var c2 = [cx + Math.cos(ang + Math.PI * rnd(0.6, 1.4)) * r2 * z.w, cy + Math.sin(ang + Math.PI) * r2 * z.h];
      out += '<path class="fx-knot' + (k % 4 === 0 ? ' fx-knot--red' : '') + '" pathLength="1" style="animation-delay:' + (k * 30) + 'ms" d="M' +
        f(a[0]) + ' ' + f(a[1]) + ' C' + f(c1[0]) + ' ' + f(c1[1]) + ' ' + f(c2[0]) + ' ' + f(c2[1]) + ' ' + f(b[0]) + ' ' + f(b[1]) + '"/>';
    }
    return out;
  }

  function reroute() {
    var z = size();
    stage.querySelectorAll('.fx-svg').forEach(function (v) { v.setAttribute('viewBox', '0 0 ' + z.w + ' ' + z.h); });
    stage.querySelectorAll('.fx-plug').forEach(function (p, n) { p.setAttribute('d', plugD(n, z)); });
    stage.querySelectorAll('.fx-hop').forEach(function (p, n) { p.setAttribute('d', routeD(n, n + 1, z)); });
    stage.querySelectorAll('.fx-sync').forEach(function (p) {
      p.setAttribute('d', routeD(+p.getAttribute('data-from'), +p.getAttribute('data-to'), z));
    });
  }
  window.addEventListener('resize', reroute);

  /* ── Caption ── */
  function say(kind, label, text, note, noteKind) {
    caption.setAttribute('data-kind', kind);
    capLabel.textContent = label;
    capText.textContent = text;
    setNote(note, noteKind);
    caption.classList.remove('is-swap'); void caption.offsetWidth; caption.classList.add('is-swap');
  }
  function setNote(note, noteKind) {
    capNote.textContent = note || '';
    capNote.setAttribute('data-kind', noteKind || '');
  }
  function sayStep(n) {
    var s = S[current];
    if (n >= s.steps.length) { say('result', 'Result', s.result); return; }
    var st = s.steps[n];
    say(n === 0 ? 'trigger' : (st[0] === 'ai' ? 'ai' : 'step'),
      (n === 0 ? 'Trigger' : 'Step ' + (n + 1)) + ' · ' + st[1], st[2], st[0] === 'ai' ? AI_NOTE : '', 'ai');
  }

  function place(el, pt, rot) {
    el.style.left = pt[0] + '%';
    el.style.top = pt[1] + '%';
    el.style.setProperty('--r', (rot || 0) + 'deg');
  }

  /* ── One scenario ── */
  function render(i) {
    clear();
    current = (i + S.length) % S.length;
    var s = S[current], count = s.steps.length + 1;
    fillPickers();
    problemEl.textContent = s.problem;
    solutionEl.textContent = s.result;
    solutionRow.classList.remove('is-done');

    POS = layout(count);
    cluster = POS.map(function () { return [rnd(24, 76), rnd(22, 80)]; });

    var nodes = s.steps.map(function (st, n) {
      var kind = st[0] === 'ai' ? ' fx-node--ai' : (st[0].indexOf('zoho-') === 0 ? '' : ' fx-node--src');
      return '<button type="button" class="fx-node' + kind + '" data-n="' + n + '" ' +
        'aria-label="Step ' + (n + 1) + ': ' + esc(st[1]) + '. ' + esc(st[2]) + '">' +
        '<span class="fx-badge">' + (n + 1) + '</span>' + art(st[0], st[1]) + '</button>';
    }).join('') +
      '<button type="button" class="fx-node fx-node--result" data-n="' + (count - 1) + '" aria-label="Result: ' + esc(s.result) + '">' +
      '<span class="fx-badge">' + CHECK + '</span><b>Result</b></button>';

    var z = size(), hops = '';
    for (var h = 0; h < count - 1; h++) hops += '<path class="fx-hop" data-w="' + h + '" pathLength="1" d="' + routeD(h, h + 1, z) + '"/>';

    stage.className = 'fx-stage';
    stage.innerHTML =
      '<div class="fx-rail" aria-hidden="true"><span class="fx-rail-label"><b>Integration + AI layer</b>' +
      '<i> &middot; Deluge &middot; Zoho Flow &middot; APIs &middot; AI</i></span></div>' +
      '<svg class="fx-svg" viewBox="0 0 ' + z.w + ' ' + z.h + '" aria-hidden="true">' +
      '<g class="fx-knots">' + knots(z) + '</g>' +
      POS.map(function (p, n) { return '<path class="fx-plug" pathLength="1" d="' + plugD(n, z) + '"/>'; }).join('') +
      hops + '<g class="fx-syncs"></g></svg>' +
      '<span class="fx-packet" aria-hidden="true"></span><span class="fx-packet fx-packet--sync" aria-hidden="true"></span>' + nodes +
      '<svg class="fx-svg fx-svg--over" viewBox="0 0 ' + z.w + ' ' + z.h + '" aria-hidden="true"><g class="fx-knots">' + knots(z) + '</g></svg>';

    stage.querySelectorAll('.fx-node').forEach(function (el, n) {
      place(el, reducedMotion ? POS[n] : cluster[n], reducedMotion ? 0 : rnd(-14, 14));
      el.style.transitionDelay = (n * 55) + 'ms';
    });

    if (reducedMotion) {
      stage.classList.add('is-layer', 'is-sorted', 'is-wired', 'is-finished');
      solutionRow.classList.add('is-done');
      stage.querySelectorAll('.fx-hop').forEach(function (w) { w.style.strokeDashoffset = 0; });
      say('result', 'Result', s.result);
      return;
    }

    say('problem', 'Before', 'Every app is patched to the others by hand, so people copy, re-type and chase.');
    void stage.offsetWidth;
    later(function () { stage.classList.add('is-tangle'); }, 60);
    later(function () {
      stage.classList.add('is-layer');
      say('layer', 'The fix: one integration and AI layer',
        'Deluge, Zoho Flow and APIs connect every app, and AI reads, sorts and drafts in between, so each step hands over on its own.');
    }, 1500);
    later(function () {
      stage.classList.add('is-sorted');
      stage.querySelectorAll('.fx-node').forEach(function (el, n) { place(el, POS[n], 0); });
    }, 2300);
    later(function () { stage.classList.add('is-wired'); }, 3200);
    later(function () { activate(0); }, 3800);
  }

  function node(n) { return stage.querySelector('.fx-node[data-n="' + n + '"]'); }

  function activate(n) {
    var s = S[current], last = s.steps.length;
    stage.querySelectorAll('.fx-node.is-active').forEach(function (el) { el.classList.remove('is-active'); el.classList.add('is-done'); });
    node(n).classList.add('is-active');
    sayStep(n);
    if (n === last) {
      stage.classList.add('is-finished');
      solutionRow.classList.add('is-done');
      if (auto) hold();
      return;
    }
    var sync = s.steps[n][3];
    if (sync) {
      later(function () {
        syncBack(n, sync[0], function () { setNote('Synced back: ' + sync[1], 'sync'); });
      }, 1300);
      later(function () { travel(n, function () { activate(n + 1); }); }, 3300);
    } else {
      later(function () { travel(n, function () { activate(n + 1); }); }, 1500);
    }
  }

  // Moves a packet along a path on the play clock; returns true from the frame it finishes
  function run(path, packet, dur, step, done) {
    var t0 = clock, mine = gen;
    packet.classList.add('is-shown');
    anims.push(function () {
      if (mine !== gen) return true;
      var p = Math.min(1, (clock - t0) / dur), e = p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      var pt = path.getPointAtLength(e * path.getTotalLength()), z = size();
      step(e);
      packet.style.left = (pt.x / z.w * 100) + '%';
      packet.style.top = (pt.y / z.h * 100) + '%';
      if (p < 1) return false;
      packet.classList.remove('is-shown');
      done();
      return true;
    });
  }

  // Forward: the packet runs along the hop and leaves a dark trail
  function travel(n, done) {
    var hop = stage.querySelector('.fx-hop[data-w="' + n + '"]');
    run(hop, stage.querySelector('.fx-packet:not(.fx-packet--sync)'), 950,
      function (e) { hop.style.strokeDashoffset = 1 - e; }, done);
  }

  // Sync back: a green pulse runs back through the layer to an earlier app
  function syncBack(from, to, done) {
    var z = size(), g = stage.querySelector('.fx-syncs');
    var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('class', 'fx-sync');
    path.setAttribute('pathLength', '1');
    path.setAttribute('d', routeD(from, to, z));
    path.setAttribute('data-from', from);
    path.setAttribute('data-to', to);
    g.appendChild(path);
    run(path, stage.querySelector('.fx-packet--sync'), 1100,
      function (e) { path.style.strokeDashoffset = 1 - e; },
      function () {
        var target = node(to);
        target.classList.add('is-synced');
        path.classList.add('is-faded');
        later(function () { target.classList.remove('is-synced'); }, 1800);
        done();
      });
  }

  function hold() {
    progress.style.animationDuration = HOLD_MS + 'ms';
    progress.classList.remove('is-running'); void progress.offsetWidth; progress.classList.add('is-running');
    later(function () { render(current + 1); }, HOLD_MS);
  }

  function choose(i) {
    auto = false;
    root.classList.add('is-manual');
    render(i);
  }

  // Hovering or tapping a card shows what it does
  stage.addEventListener('mouseover', function (e) {
    var el = e.target.closest('.fx-node');
    if (!el || !stage.classList.contains('is-sorted')) return;
    sayStep(+el.getAttribute('data-n'));
  });
  stage.addEventListener('focusin', function (e) {
    var el = e.target.closest('.fx-node');
    if (el) el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }));
  });

  /* ── Drag any card: its wires re-route through the layer as it moves ── */
  var drag = null;
  stage.addEventListener('pointerdown', function (e) {
    var el = e.target.closest('.fx-node');
    if (!el || !stage.classList.contains('is-wired')) return;
    var r = stage.getBoundingClientRect(), n = +el.getAttribute('data-n');
    drag = { el: el, n: n, r: r, moved: false,
      dx: e.clientX - (r.left + POS[n][0] * r.width / 100), dy: e.clientY - (r.top + POS[n][1] * r.height / 100) };
    el.setPointerCapture(e.pointerId);
  });
  stage.addEventListener('pointermove', function (e) {
    if (!drag) return;
    var r = drag.r;
    var x = (e.clientX - drag.dx - r.left) / r.width * 100, y = (e.clientY - drag.dy - r.top) / r.height * 100;
    if (!drag.moved && Math.abs(x - POS[drag.n][0]) + Math.abs(y - POS[drag.n][1]) < 1.5) return;
    drag.moved = true;
    pause();
    drag.el.classList.add('is-dragging');
    x = Math.max(10, Math.min(90, x));
    y = Math.max(9, Math.min(91, y));
    if (Math.abs(y - RAIL_Y) < 13) y = y < RAIL_Y ? RAIL_Y - 13 : RAIL_Y + 13; // cards sit above or below the layer
    POS[drag.n] = [x, y];
    place(drag.el, POS[drag.n], 0);
    reroute();
  });
  function endDrag() {
    if (!drag) return;
    drag.el.classList.remove('is-dragging');
    drag = null;
  }
  stage.addEventListener('pointerup', endDrag);
  stage.addEventListener('pointercancel', endDrag);

  root.querySelectorAll('[data-dir]').forEach(function (b) {
    b.addEventListener('click', function () { choose(current + (+b.getAttribute('data-dir'))); });
  });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      root.classList.toggle('is-offscreen', !visible);
    }).observe(root);
  }

  // A tap on the map or the layers holds the story for five seconds
  stage.addEventListener('pointerdown', pause);
  root.querySelector('[data-fx-resume]').addEventListener('click', resume);
  root.querySelector('.fx-layers').addEventListener('pointerdown', pause);

  render(0);
  requestAnimationFrame(loop);
  }
})();
