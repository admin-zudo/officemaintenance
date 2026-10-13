/* ============================================================
   Project enquiry form ([data-lead-form])
   Checks the fields, then posts to Zoho Forms through a hidden
   frame so the visitor stays on the page and sees a thank-you.
   Without JavaScript the form posts normally and Zoho redirects
   to /thank-you/. Also fills the referrer (the page the lead came
   from), the Google Ads click id, and a sensible service area.
   The brochure downloads beside the submit button need a valid
   name and email; a download also sends the enquiry, noting
   which file was taken.
   ============================================================ */

(function () {
  'use strict';

  var forms = document.querySelectorAll('[data-lead-form]');
  if (!forms.length) return;

  var EMAIL = /^[\w]([\w\-.+&'/]*)@([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,22}$/;
  var PHONE = /^[+]{0,1}[()0-9-. ]+$/;
  var FILES = { brochure_pdf: 'PDF brochure', deck_pptx: 'PowerPoint deck' };

  // Google Ads click id, kept for the session so a later enquiry still carries it.
  // The first page a visitor landed on with campaign tags (utm_*, gclid, fbclid) is kept too, so an
  // enquiry sent from another page still shows which ad brought them.
  var gclid = '', landing = '';
  try {
    var m = location.search.match(/[?&]gclid=([^&]+)/);
    if (m) sessionStorage.setItem('zw_gclid', decodeURIComponent(m[1]));
    gclid = sessionStorage.getItem('zw_gclid') || '';
    // Untagged links (an ad whose URL can't be edited, a post, an email) still show the site they came from
    var ref = document.referrer;
    var fromOutside = ref && ref.indexOf(location.origin) !== 0;
    var tagged = /[?&](utm_[a-z]+|gclid|fbclid|msclkid)=/.test(location.search);
    if ((tagged || fromOutside) && !sessionStorage.getItem('zw_landing')) {
      sessionStorage.setItem('zw_landing', location.href.split('#')[0] + (fromOutside ? ' (from ' + ref.split('/').slice(0, 3).join('/') + ')' : ''));
    }
    landing = sessionStorage.getItem('zw_landing') || '';
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

  // Checks the given fields, shows their errors and focuses the first bad one
  function valid(fields) {
    var firstBad = null;
    fields.forEach(function (f) {
      var bad = !check(f);
      showError(f, bad);
      if (bad && !firstBad) firstBad = f;
    });
    if (firstBad) firstBad.focus();
    return !firstBad;
  }

  function track(a) {
    if (window.dataLayer) window.dataLayer.push({ event: 'brochure_download', file_name: a.getAttribute('data-download'), form_location: location.pathname });
  }

  // Downloads in the thank-you message (outside a form) are always allowed
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-download]');
    if (a && !a.closest('[data-lead-form]')) track(a);
  });

  forms.forEach(function (form, i) {
    var success = form.nextElementSibling;
    var submit = form.querySelector('.lead-submit');
    var status = form.querySelector('.lead-form-status');
    var fields = Array.prototype.slice.call(form.querySelectorAll('[data-check]'));
    var needed = [form.elements.SingleLine, form.elements.Email];

    var here = location.href.split('#')[0];
    form.elements.zf_referrer_name.value = (landing && landing !== here ? here + ' | landed on: ' + landing : here).slice(0, 1800);
    form.elements.zc_gad.value = gclid;
    var select = form.elements.Dropdown;
    for (var k = 0; k < SERVICE.length; k++) {
      if (SERVICE[k][0].test(location.pathname)) { select.value = SERVICE[k][1]; break; }
    }

    fields.forEach(function (f) {
      f.addEventListener('blur', function () { if (f.value) showError(f, !check(f)); });
      f.addEventListener('input', function () {
        if (f.closest('.lead-field').classList.contains('is-invalid')) showError(f, !check(f));
        if (!sent && status.textContent && needed.every(check)) status.textContent = '';
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
      // Ad pixels (only present when cookie rules allow them): tell Meta and ChatGPT ads which visits became enquiries
      if (window.fbq) window.fbq('track', 'Lead', { content_name: location.pathname });
      // The conversion set up in OpenAI Ads Manager (Tools > Conversions) uses this event
      if (window.oaiq) window.oaiq('measure', 'registration_completed', { type: 'customer_action' });
    });

    function sending() {
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
    }

    form.addEventListener('submit', function (e) {
      if (!valid(fields)) {
        e.preventDefault();
        return;
      }
      sending();
    });

    // Brochure downloads: name and email first; then the file starts and the enquiry is sent with a note
    form.querySelectorAll('[data-download]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var file = FILES[a.getAttribute('data-download')];
        if (sent) return;
        if (!valid(needed)) {
          e.preventDefault();
          status.textContent = 'Please enter your name and email to download the ' + file + '.';
          return;
        }
        if (!valid(fields)) {
          e.preventDefault();
          return;
        }
        var note = form.elements.MultiLine;
        var line = '[Downloaded the ' + file + ']';
        if (note.value.indexOf(line) < 0) note.value = (note.value ? note.value + '\n\n' : '') + line;
        track(a);
        // Let the browser start the download first, then post the enquiry
        setTimeout(function () { sending(); form.submit(); }, 50);
      });
    });
  });
})();
