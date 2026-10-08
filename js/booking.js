/* ============================================================
   Zoho Bookings Dialog
   Opens #custom-bookings-modal from any [aria-haspopup="dialog"]
   booking button, loads the Zoho Bookings embed script on first
   open only, closes on Escape or backdrop click,
   and returns focus to the button that opened it.
   ============================================================ */

(function () {
  'use strict';

  var EMBED_SRC = 'https://bookings.nimbuspop.com/assets/embed.js';
  var BOOKING_URL = 'https://zudocroporation.zohobookings.in/portal-embed#/471882000000032065';

  var modal = document.getElementById('custom-bookings-modal');
  var closeBtn = document.getElementById('close-bookings-modal');
  var triggers = document.querySelectorAll('#booking-link, #booking-link-2');
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
    if (window.dataLayer) window.dataLayer.push({ event: 'book_call_click', cta_location: lastTrigger ? lastTrigger.id : '' });
    if (typeof window.Bookings !== 'undefined') embed(); else loadEmbedScript();
    if (closeBtn) closeBtn.focus();
  }

  function close() {
    modal.hidden = true;
    document.body.style.overflow = '';
    if (lastTrigger) lastTrigger.focus();
  }

  triggers.forEach(function (btn) {
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
