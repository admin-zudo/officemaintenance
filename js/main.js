/* ============================================================
   Main JavaScript   Navbar, Mobile Menu, Smooth Scroll,
   FAQ Accordion, Roadmap Scroll
   ============================================================ */

(function () {
  'use strict';

  // -- Navbar scroll behavior --------------------------------
  const navbar = document.querySelector('.navbar');

  function handleNavbarScroll() {
    if (!navbar) return;
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleNavbarScroll, { passive: true });
  handleNavbarScroll(); // initial check

  // -- Mobile menu toggle ------------------------------------
  const toggle = document.querySelector('.navbar-toggle');
  const mobileNav = document.querySelector('.navbar-nav');

  if (toggle && mobileNav) {
    function setMenu(open) {
      toggle.classList.toggle('open', open);
      mobileNav.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
      document.body.style.overflow = open ? 'hidden' : '';
    }

    toggle.addEventListener('click', function () {
      setMenu(!toggle.classList.contains('open'));
    });

    // Close when any menu link (including the CTA) is used
    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { setMenu(false); });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.classList.contains('open')) {
        setMenu(false);
        toggle.focus();
      }
    });

    // Leaving the mobile layout with the menu open would leave the page scroll-locked
    window.matchMedia('(min-width: 1100px)').addEventListener('change', function (e) {
      if (e.matches) setMenu(false);
    });
  }

  // -- Smooth scroll for anchor links ------------------------
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // -- FAQ Accordion Toggle -------------------------------
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-question');
    if (!faqItems.length) return;

    faqItems.forEach(function (btn, i) {
      var item = btn.closest('.faq-item');
      var answer = item && item.querySelector('.faq-answer');
      if (answer) {
        if (!answer.id) answer.id = 'faq-answer-' + (i + 1);
        btn.setAttribute('aria-controls', answer.id);
      }
      btn.setAttribute('aria-expanded', item && item.classList.contains('active') ? 'true' : 'false');

      // Native <button> already handles Enter and Space
      btn.addEventListener('click', function () {
        var isOpen = item.classList.toggle('active');
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        if (answer) {
          answer.style.display = isOpen ? 'block' : 'none';
        }
      });
    });
  }

  initFaqAccordion();

  // -- Roadmap Scroll Indicators ------------------------------
  function initRoadmapScroll() {
    const roadmapWrapper = document.querySelector('.roadmap-wrapper');
    const scrollLeftBtn = document.querySelector('.roadmap-scroll-indicator.left');
    const scrollRightBtn = document.querySelector('.roadmap-scroll-indicator.right');

    if (roadmapWrapper && (scrollLeftBtn || scrollRightBtn)) {
      if (scrollLeftBtn) {
        scrollLeftBtn.addEventListener('click', function () {
          roadmapWrapper.scrollBy({ left: -250, behavior: 'smooth' });
        });
      }
      if (scrollRightBtn) {
        scrollRightBtn.addEventListener('click', function () {
          roadmapWrapper.scrollBy({ left: 250, behavior: 'smooth' });
        });
      }

      // Hide arrows if reached start or end
      const updateArrows = () => {
        if (scrollLeftBtn) {
          scrollLeftBtn.style.opacity = roadmapWrapper.scrollLeft > 10 ? '1' : '0.2';
          scrollLeftBtn.style.pointerEvents = roadmapWrapper.scrollLeft > 10 ? 'auto' : 'none';
        }
        if (scrollRightBtn) {
          const maxScroll = roadmapWrapper.scrollWidth - roadmapWrapper.clientWidth;
          scrollRightBtn.style.opacity = roadmapWrapper.scrollLeft < maxScroll - 10 ? '1' : '0.2';
          scrollRightBtn.style.pointerEvents = roadmapWrapper.scrollLeft < maxScroll - 10 ? 'auto' : 'none';
        }
      };

      roadmapWrapper.addEventListener('scroll', updateArrows, { passive: true });
      window.addEventListener('resize', updateArrows, { passive: true });
      setTimeout(updateArrows, 150);
    }
  }

  initRoadmapScroll();

})();
