/* ============================================================
   Cookie Consent Banner — JS
   Stores the visitor's choice in localStorage for 365 days and
   applies it to Google Consent Mode v2 (defaults are set inline
   in each page <head>).
   Zoho PageSense (enquiry and visit analytics) and the Meta Pixel
   (measuring our Meta ads; js/leadform.js sends its Lead event) load:
   - after "Accept", everywhere;
   - before any choice, only outside the UK/EEA/Switzerland
     (detected from the device time zone), mirroring the
     Consent Mode defaults;
   - never after "Essential only".
   ============================================================ */

(function () {
  'use strict';

  var COOKIE_KEY = 'zudo_cookie_consent';
  var COOKIE_EXPIRY_DAYS = 365;
  var PAGESENSE_SRC = 'https://cdn-in.pagesense.io/js/zudoworks/a082c937db01490eb591882d194fbe5a.js';
  var META_PIXEL_ID = '1664899591891953';

  function read(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }

  function write(key, value) {
    try { localStorage.setItem(key, value); } catch (e) { }
  }

  // UK, EEA and Swiss visitors must opt in before analytics run
  function needsOptIn() {
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      return /^(Europe|Atlantic\/(Reykjavik|Canary|Madeira|Azores|Faroe))\//.test(tz);
    } catch (e) {
      return true;
    }
  }

  function getConsent() {
    return read(COOKIE_KEY);
  }

  function hasConsentExpired() {
    var storedDate = read(COOKIE_KEY + '_date');
    if (!storedDate) return false;
    var daysSince = (Date.now() - parseInt(storedDate, 10)) / (1000 * 60 * 60 * 24);
    return daysSince > COOKIE_EXPIRY_DAYS;
  }

  function loadPageSense() {
    if (document.getElementById('pagesense-script')) return;
    var s = document.createElement('script');
    s.id = 'pagesense-script';
    s.async = true;
    s.src = PAGESENSE_SRC;
    document.head.appendChild(s);
  }

  // Meta's standard pixel snippet, run only when the rules above allow it
  function loadMetaPixel() {
    if (window.fbq) {
      window.fbq('consent', 'grant');
      return;
    }
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0;
      t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', META_PIXEL_ID);
    window.fbq('track', 'PageView');
  }

  function loadTrackers() {
    loadPageSense();
    loadMetaPixel();
  }

  function applyConsent(value) {
    var granted = value === 'accepted';
    var state = granted ? 'granted' : 'denied';
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', { ad_storage: state, ad_user_data: state, ad_personalization: state, analytics_storage: state });
    }
    if (granted) loadTrackers();
    else if (window.fbq) window.fbq('consent', 'revoke');
  }

  function setConsent(value) {
    write(COOKIE_KEY, value);
    write(COOKIE_KEY + '_date', Date.now().toString());
    applyConsent(value);
  }

  function hideBanner(banner) {
    banner.classList.remove('visible');
    setTimeout(function () {
      banner.remove();
    }, 500);
  }

  function showBanner() {
    if (document.getElementById('cookie-consent')) return;

    var banner = document.createElement('div');
    banner.id = 'cookie-consent';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', 'Cookie preferences');
    banner.innerHTML = [
      '<div class="cookie-inner">',
      '  <div class="cookie-icon" aria-hidden="true">🍪</div>',
      '  <div class="cookie-actions">',
      '    <button type="button" id="cookie-accept">Accept All</button>',
      '    <button type="button" id="cookie-decline">Essential Only</button>',
      '  </div>',
      '  <div class="cookie-text">',
      '    <p>We use essential cookies to run this site. With your consent we also use analytics and advertising cookies (Google Analytics, Zoho PageSense and the Meta Pixel) to understand how the site is used and to measure our ads. Where the law requires it, they stay off until you accept. See our <a href="/privacy/">Privacy Policy</a>.</p>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(banner);

    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        banner.classList.add('visible');
      });
    });

    document.getElementById('cookie-accept').addEventListener('click', function () {
      setConsent('accepted');
      hideBanner(banner);
    });

    document.getElementById('cookie-decline').addEventListener('click', function () {
      setConsent('declined');
      hideBanner(banner);
    });
  }

  // Lets a "Cookie settings" link reopen the banner: onclick="zudoCookieSettings()"
  window.zudoCookieSettings = showBanner;

  function init() {
    var consent = getConsent();
    if (consent && !hasConsentExpired()) {
      if (consent === 'accepted') loadTrackers();
      return;
    }
    if (!needsOptIn()) loadTrackers();
    showBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
