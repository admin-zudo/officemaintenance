/* ============================================================
   Cookie Consent Banner — JS
   Stores preference in localStorage for 365 days.
   "Accept" = analytics allowed. "Decline" = essential only.
   ============================================================ */

(function () {
  'use strict';

  var COOKIE_KEY = 'zudo_cookie_consent';
  var COOKIE_EXPIRY_DAYS = 365;

  function getConsent() {
    return localStorage.getItem(COOKIE_KEY);
  }

  function setConsent(value) {
    localStorage.setItem(COOKIE_KEY, value);
    // Also store the date so you can re-prompt after expiry if needed
    localStorage.setItem(COOKIE_KEY + '_date', Date.now().toString());
  }

  function hasConsentExpired() {
    var storedDate = localStorage.getItem(COOKIE_KEY + '_date');
    if (!storedDate) return false;
    var daysSince = (Date.now() - parseInt(storedDate, 10)) / (1000 * 60 * 60 * 24);
    return daysSince > COOKIE_EXPIRY_DAYS;
  }

  function hideBanner(banner) {
    banner.classList.remove('visible');
    setTimeout(function () {
      banner.remove();
    }, 500);
  }

  function initCookieBanner() {
    // Don't show if already consented and not expired
    if (getConsent() && !hasConsentExpired()) return;

    // Create banner HTML
    var banner = document.createElement('div');
    banner.id = 'cookie-consent';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-live', 'polite');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.innerHTML = [
      '<div class="cookie-inner">',
      '  <div class="cookie-icon" aria-hidden="true">🍪</div>',
      '  <div class="cookie-text">',
      '    <p>We use essential cookies to make our website work. With your permission, we may also use analytics cookies to understand how you use our site and improve your experience. See our <a href="/privacy-policy.html">Privacy Policy</a> and <a href="/terms-of-service.html">Terms of Service</a> for details.</p>',
      '  </div>',
      '  <div class="cookie-actions">',
      '    <button id="cookie-accept" aria-label="Accept all cookies">Accept All</button>',
      '    <button id="cookie-decline" aria-label="Use essential cookies only">Essential Only</button>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(banner);

    // Trigger slide-in after short delay (allows paint)
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        banner.classList.add('visible');
      });
    });

    // Button handlers
    document.getElementById('cookie-accept').addEventListener('click', function () {
      setConsent('accepted');
      hideBanner(banner);
    });

    document.getElementById('cookie-decline').addEventListener('click', function () {
      setConsent('declined');
      hideBanner(banner);
    });
  }

  // Run after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCookieBanner);
  } else {
    initCookieBanner();
  }

})();
