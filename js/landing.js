/* ============================================================
   Campaign landing pages (css/landing.css)
   1. The example job in the hero moves through its stages.
   2. On phones, a bar with the two actions appears once the
      hero form has scrolled away, and hides while a form is on
      screen.
   3. The hero eyebrow alternates between two descriptions.
   4. "Download the PDF or PPT" leads to the hero form.
   ============================================================ */

(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1. Example job: each stage turns green in turn, then the next job starts
  var route = document.querySelector('[data-lp-route]');
  if (route) {
    var steps = route.querySelectorAll('li');
    var at = 0;
    var paint = function () {
      for (var i = 0; i < steps.length; i++) {
        steps[i].classList.toggle('is-done', i < at);
        steps[i].classList.toggle('is-now', i === at);
      }
    };
    if (reduced) {
      at = steps.length;
      paint();
    } else {
      paint();
      setInterval(function () {
        if (document.hidden) return;
        at = at >= steps.length ? 0 : at + 1;
        paint();
      }, 1100);
    }
  }

  // 3. Eyebrow: the two descriptions take turns
  var rot = document.querySelector('[data-lp-rotate]');
  if (rot && !reduced) {
    var words = rot.children, cur = 0;
    setInterval(function () {
      if (document.hidden) return;
      var next = (cur + 1) % words.length;
      words[cur].classList.remove('is-on');
      words[cur].classList.add('is-out');
      words[next].classList.remove('is-out');
      words[next].classList.add('is-on');
      words[cur].setAttribute('aria-hidden', 'true');
      words[next].removeAttribute('aria-hidden');
      cur = next;
    }, 3200);
  }

  // 4. "Download the PDF or PPT": go to the hero form, where name and email unlock the files
  document.querySelectorAll('[data-lp-download]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var card = document.getElementById('enquiry');
      var form = card && card.querySelector('[data-lead-form]');
      if (!form || form.hidden) return;
      e.preventDefault();
      card.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'center' });
      var status = form.querySelector('.lead-form-status');
      status.textContent = 'Enter your name and email, then choose PDF brochure or PPT deck.';
      setTimeout(function () { form.elements.SingleLine.focus({ preventScroll: true }); }, reduced ? 0 : 450);
    });
  });

  // 2. Phone action bar
  var bar = document.querySelector('[data-lp-bar]');
  var cards = document.querySelectorAll('.lp-form-card');
  if (!bar || !cards.length || !('IntersectionObserver' in window)) return;

  var showing = 0, passedHero = false;
  var links = bar.querySelectorAll('a');
  var update = function () {
    var on = passedHero && showing === 0;
    bar.classList.toggle('is-on', on);
    bar.setAttribute('aria-hidden', on ? 'false' : 'true');
    for (var i = 0; i < links.length; i++) links[i].tabIndex = on ? 0 : -1;
  };

  var seen = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      showing += e.isIntersecting ? 1 : (e.target._lpSeen ? -1 : 0);
      e.target._lpSeen = e.isIntersecting;
      if (e.target === cards[0] && !e.isIntersecting) {
        passedHero = e.boundingClientRect.top < 0;
      }
    });
    showing = Math.max(0, showing);
    update();
  }, { threshold: 0.15 });

  Array.prototype.forEach.call(cards, function (c) { seen.observe(c); });
})();
