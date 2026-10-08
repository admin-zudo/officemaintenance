/* ============================================================
   Main JavaScript   Navbar, Mobile Menu, Smooth Scroll,
   Scroll Progress, FAQ Accordion, Roadmap Scroll
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

  // -- Scroll Progress Bar -----------------------------------
  const progressBar = document.getElementById('scrollProgress');

  function updateScrollProgress() {
    if (!progressBar) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (docHeight <= 0) return;
    const scrollPercent = (scrollTop / docHeight) * 100;
    progressBar.style.width = scrollPercent + '%';
  }

  window.addEventListener('scroll', updateScrollProgress, { passive: true });
  updateScrollProgress();

  // -- Mobile menu toggle ------------------------------------
  const toggle = document.querySelector('.navbar-toggle');
  const mobileNav = document.querySelector('.navbar-nav');

  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      const isOpen = toggle.classList.toggle('open');
      mobileNav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close mobile menu when a link is clicked
    mobileNav.querySelectorAll('.navbar-link').forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.classList.remove('open');
        mobileNav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    // Close on escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.classList.contains('open')) {
        toggle.classList.remove('open');
        mobileNav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
        toggle.focus();
      }
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
