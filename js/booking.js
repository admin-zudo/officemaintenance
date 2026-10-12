/* ============================================================
   Zoho Bookings Dialog
   Opens #custom-bookings-modal from any [data-booking] link or
   button (links fall back to /contact/ without JavaScript), loads the Zoho Bookings embed script on first
   open only, closes on Escape or backdrop click,
   and returns focus to the button that opened it.
   ============================================================ */

(function () {
  'use strict';

  var EMBED_SRC = 'https://bookings.nimbuspop.com/assets/embed.js';
  var BOOKING_URL = 'https://zudocroporation.zohobookings.in/portal-embed#/471882000000032065';

  var modal = document.getElementById('custom-bookings-modal');
  var closeBtn = document.getElementById('close-bookings-modal');
  var triggers = document.querySelectorAll('[data-booking]');
  if (!modal || !triggers.length) return;

  var embedded = false;
  var scriptRequested = false;
  var lastTrigger = null;

  function embed() {
    if (embedded || typeof window.Bookings === 'undefined') return;
    window.Bookings.inlineEmbed({
      url: BOOKING_URL,
      parent: '#inline-container',
      height: '100%'
    });
    embedded = true;
  }

  function loadEmbedScript() {
    if (scriptRequested) return;
    scriptRequested = true;
    var s = document.createElement('script');
    s.src = EMBED_SRC;
    s.async = true;
    s.onload = embed;
    document.body.appendChild(s);
  }

  function open(e) {
    if (e) e.preventDefault();
    lastTrigger = e ? e.currentTarget : null;
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    if (window.dataLayer) window.dataLayer.push({ event: 'book_call_click', cta_location: lastTrigger ? (lastTrigger.closest('section, header, footer, .top-bar') || {}).id || lastTrigger.className : '' });
    if (typeof window.Bookings !== 'undefined') embed(); else loadEmbedScript();
    if (closeBtn) closeBtn.focus();
  }

  function close() {
    modal.hidden = true;
    document.body.style.overflow = '';
    if (lastTrigger) lastTrigger.focus();
  }

  triggers.forEach(function (btn) {
    btn.setAttribute('aria-haspopup', 'dialog');
    btn.addEventListener('click', open);
  });

  if (closeBtn) closeBtn.addEventListener('click', close);

  modal.addEventListener('click', function (e) {
    if (e.target === modal) close();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !modal.hidden) close();
  });
})();

/* ============================================================
   Project form dialog (lead form)
   Opens #project-form-modal from [data-project-form] and from every
   "/contact/#contact-form" link outside the Contact page (links still
   work without JavaScript). The Zoho Form loads on first open, tells
   us its height, and the frame grows to fit, so the form itself never
   shows a scroll bar.
   ============================================================ */

(function () {
  'use strict';

  var modal = document.getElementById('project-form-modal');
  if (!modal) return;
  var onContact = /^\/contact\/?$/.test(location.pathname);
  var triggers = document.querySelectorAll(onContact ? '[data-project-form]' :
    '[data-project-form], a[href$="/contact/#contact-form"]');
  if (!triggers.length) return;

  var frame = modal.querySelector('iframe');
  var closeBtn = document.getElementById('close-project-form');
  var formUrl = frame.getAttribute('data-src');
  var perma = formUrl.split('/formperma/')[1];
  var lastTrigger = null;

  // Zoho Forms posts "perma|height"; size the frame to the whole form
  window.addEventListener('message', function (e) {
    if (!/zohopublic\./.test(e.origin) || typeof e.data !== 'string') return;
    var parts = e.data.split('|');
    if (parts.length < 2 || parts[0].indexOf(perma) === -1) return;
    var h = parseInt(parts[1], 10);
    if (h > 0) frame.style.height = (h + 15) + 'px';
  });

  function open(e) {
    if (e) e.preventDefault();
    lastTrigger = e ? e.currentTarget : null;
    if (!frame.src) {
      // Tell the form which page the lead came from
      // zf_rszfm=1 asks Zoho Forms to post its height; referrername records the page the lead came from
      frame.src = formUrl + '?zf_rszfm=1&referrername=' + encodeURIComponent(location.href.split('?')[0].slice(0, 1800));
    }
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    if (window.dataLayer) {
      window.dataLayer.push({ event: 'project_form_open',
        cta_location: lastTrigger ? lastTrigger.getAttribute('data-cta') ||
          (lastTrigger.closest('section, header, footer') || {}).id || '' : '' });
    }
    closeBtn.focus();
  }

  function close() {
    modal.hidden = true;
    document.body.style.overflow = '';
    if (lastTrigger) lastTrigger.focus();
  }

  triggers.forEach(function (btn) {
    btn.setAttribute('aria-haspopup', 'dialog');
    btn.addEventListener('click', open);
  });
  closeBtn.addEventListener('click', close);
  modal.addEventListener('click', function (e) { if (e.target === modal) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !modal.hidden) close(); });
})();
