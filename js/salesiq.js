/* ============================================================
   Zoho SalesIQ Loader
   Loads the chat widget on the visitor's first interaction or
   after 6 seconds, so it never competes with the first render.
   ============================================================ */

(function () {
  'use strict';

  var WIDGET_SRC = 'https://salesiq.zohopublic.in/widget?wc=siq41d5faa948254fbe80c22c34c3b718451e4896b7c5f3c1a47f09184669bc09db';
  var EVENTS = ['pointerdown', 'keydown', 'scroll', 'touchstart'];
  var loaded = false;

  function load() {
    if (loaded) return;
    loaded = true;
    EVENTS.forEach(function (evt) { window.removeEventListener(evt, load); });

    window.$zoho = window.$zoho || {};
    window.$zoho.salesiq = window.$zoho.salesiq || { ready: function () { } };

    var s = document.createElement('script');
    s.id = 'zsiqscript';
    s.src = WIDGET_SRC;
    s.defer = true;
    document.body.appendChild(s);
  }

  EVENTS.forEach(function (evt) {
    window.addEventListener(evt, load, { once: true, passive: true });
  });
  window.addEventListener('load', function () { setTimeout(load, 6000); });
})();
