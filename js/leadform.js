/* ============================================================
   Project enquiry form ([data-lead-form])
   Checks the fields, then posts to Zoho Forms through a hidden
   frame so the visitor stays on the page and sees a thank-you.
   Without JavaScript the form posts normally and Zoho redirects
   to /thank-you/. Also fills the referrer (the page the lead came
   from), the Google Ads click id, and a sensible service area.
   ============================================================ */

(function () {
  'use strict';

  var forms = document.querySelectorAll('[data-lead-form]');
  if (!forms.length) return;

  var EMAIL = /^[\w]([\w\-.+&'/]*)@([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,22}$/;
  var PHONE = /^[+]{0,1}[()0-9-. ]+$/;

  // Google Ads click id, kept for the session so a later enquiry still carries it
  var gclid = '';
  try {
    var m = location.search.match(/[?&]gclid=([^&]+)/);
    if (m) sessionStorage.setItem('zw_gclid', decodeURIComponent(m[1]));
    gclid = sessionStorage.getItem('zw_gclid') || '';
  } catch (e) { }

  // Pre-select the service area from the page the visitor is on
  var SERVICE = [
    [/custom-software/, 'Custom Software Development'],
    [/zoho-integrations|solutions/, 'System Integrations'],
    [/business-process-automation|deluge/, 'Business Automation'],
    [/support-maintenance/, 'Ongoing Support & Maintenance'],
    [/zoho-creator|zoho-crm|zoho-development|manufacturing|locations/, 'Zoho Implementation']
  ];

  function check(field) {
    var kind = field.getAttribute('data-check');
    var v = field.value.trim();
    if (!kind) return true;
    if (field.required && !v) return false;
    if (kind === 'email' && v && !EMAIL.test(v)) return false;
    if (kind === 'phone' && v && !PHONE.test(v)) return false;
    return true;
  }

  function showError(field, bad) {
    var wrap = field.closest('.lead-field');
    var msg = wrap.querySelector('.lead-error');
    wrap.classList.toggle('is-invalid', bad);
    field.setAttribute('aria-invalid', bad ? 'true' : 'false');
    msg.textContent = bad ? msg.getAttribute('data-msg') || '' : '';
  }

  forms.forEach(function (form, i) {
    var success = form.nextElementSibling;
    var submit = form.querySelector('.lead-submit');
    var status = form.querySelector('.lead-form-status');
    var fields = Array.prototype.slice.call(form.querySelectorAll('[data-check]'));

    form.elements.zf_referrer_name.value = location.href.split('#')[0].slice(0, 1800);
    form.elements.zc_gad.value = gclid;
    var select = form.elements.Dropdown;
    for (var k = 0; k < SERVICE.length; k++) {
      if (SERVICE[k][0].test(location.pathname)) { select.value = SERVICE[k][1]; break; }
    }

    fields.forEach(function (f) {
      f.addEventListener('blur', function () { if (f.value) showError(f, !check(f)); });
      f.addEventListener('input', function () {
        if (f.closest('.lead-field').classList.contains('is-invalid')) showError(f, !check(f));
      });
    });

    // Posts go into a hidden frame; its load after a submit means Zoho has the record
    var sink = document.createElement('iframe');
    sink.name = 'lead-sink-' + i;
    sink.title = 'Form submission';
    sink.hidden = true;
    sink.setAttribute('aria-hidden', 'true');
    document.body.appendChild(sink);
    form.target = sink.name;
    var sent = false;

    sink.addEventListener('load', function () {
      if (!sent) return;
      sent = false;
      form.hidden = true;
      success.hidden = false;
      success.setAttribute('tabindex', '-1');
      success.focus();
      if (window.dataLayer) window.dataLayer.push({ event: 'generate_lead', form_location: location.pathname });
    });

    form.addEventListener('submit', function (e) {
      var firstBad = null;
      fields.forEach(function (f) {
        var bad = !check(f);
        showError(f, bad);
        if (bad && !firstBad) firstBad = f;
      });
      if (firstBad) {
        e.preventDefault();
        firstBad.focus();
        return;
      }
      sent = true;
      submit.disabled = true;
      submit.classList.add('is-sending');
      submit.querySelector('.lead-submit-text').textContent = 'Sending…';
      status.textContent = 'Sending your details…';
      // If the network fails, let the visitor try again
      setTimeout(function () {
        if (!sent) return;
        sent = false;
        submit.disabled = false;
        submit.classList.remove('is-sending');
        submit.querySelector('.lead-submit-text').textContent = 'Submit';
        status.textContent = 'That took too long. Please try again, or email admin@zudoworks.com.';
      }, 20000);
    });
  });
})();
