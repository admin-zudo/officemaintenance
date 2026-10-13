/* ============================================================
   Brochure reader (#brochure-viewer in tools/partials/footer.html)
   Opens from any [data-brochure-view] and shows the brochure page
   images made by tools/brochure/make_brochure.py, one page at a
   time, with thumbnails, arrow keys and swipe. Reading is open to
   everyone; downloading the files needs a name and email (see
   js/leadform.js).
   ============================================================ */

(function () {
  'use strict';

  var dlg = document.getElementById('brochure-viewer');
  if (!dlg) return;

  var total = parseInt(dlg.getAttribute('data-pages'), 10) || 1;
  var img = dlg.querySelector('[data-bv-img]');
  var count = dlg.querySelector('[data-bv-count]');
  var thumbs = dlg.querySelector('[data-bv-thumbs]');
  var at = 0, built = false, opener = null;

  function src(i) { return '/Asset/brochure/pages/page-' + (i < 9 ? '0' : '') + (i + 1) + '.webp'; }

  function build() {
    if (built) return;
    built = true;
    for (var i = 0; i < total; i++) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'bv-thumb';
      b.setAttribute('aria-label', 'Page ' + (i + 1));
      b.innerHTML = '<img src="' + src(i) + '" alt="" width="110" height="156" loading="lazy" decoding="async">';
      b.addEventListener('click', go.bind(null, i));
      thumbs.appendChild(b);
    }
  }

  function go(i) {
    at = Math.max(0, Math.min(total - 1, i));
    img.src = src(at);
    img.alt = 'Brochure page ' + (at + 1) + ' of ' + total;
    count.textContent = 'Page ' + (at + 1) + ' of ' + total;
    dlg.querySelector('.bv-nav--prev').disabled = at === 0;
    dlg.querySelector('.bv-nav--next').disabled = at === total - 1;
    var t = thumbs.children;
    for (var k = 0; k < t.length; k++) t[k].classList.toggle('is-on', k === at);
    if (t[at] && t[at].scrollIntoView) t[at].scrollIntoView({ block: 'nearest', inline: 'center' });
    // Load the next page early so turning feels instant
    if (at + 1 < total) (new Image()).src = src(at + 1);
  }

  function open(e) {
    e.preventDefault();
    opener = e.currentTarget || document.activeElement;
    build();
    dlg.hidden = false;
    document.body.style.overflow = 'hidden';
    document.body.classList.add('bv-open');
    go(0);
    dlg.querySelector('.bv-close').focus();
    if (window.dataLayer) window.dataLayer.push({ event: 'brochure_read', form_location: location.pathname });
  }

  function close() {
    if (dlg.hidden) return;
    dlg.hidden = true;
    document.body.classList.remove('bv-open');
    // Leave scrolling locked if the project form dialog is still open underneath
    var other = document.getElementById('project-form-modal');
    if (!other || other.hidden) document.body.style.overflow = '';
    if (opener && opener.focus && !opener.closest('[hidden]')) opener.focus();
  }

  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-brochure-view]');
    if (t) open({ preventDefault: function () { e.preventDefault(); }, currentTarget: t });
  });

  dlg.querySelectorAll('[data-bv-close]').forEach(function (b) { b.addEventListener('click', close); });
  dlg.querySelectorAll('[data-bv-dir]').forEach(function (b) {
    b.addEventListener('click', function () { go(at + parseInt(b.getAttribute('data-bv-dir'), 10)); });
  });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) close(); });
  document.addEventListener('keydown', function (e) {
    if (dlg.hidden) return;
    if (e.key === 'Escape') { e.stopPropagation(); close(); }
    else if (e.key === 'ArrowRight') go(at + 1);
    else if (e.key === 'ArrowLeft') go(at - 1);
  }, true);

  // Swipe between pages on touch screens
  var x0 = null;
  img.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  img.addEventListener('touchend', function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) go(at + (dx < 0 ? 1 : -1));
    x0 = null;
  });
})();
