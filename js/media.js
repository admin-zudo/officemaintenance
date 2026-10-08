/* ============================================================
   Media: image lightbox and click-to-play YouTube
   - <a href="big.webp" data-lightbox="Caption"> opens the image
     full size in a dialog; Escape, the close button or a click
     on the backdrop closes it and returns focus.
   - <button data-youtube="VIDEO_ID"> swaps itself for a
     youtube-nocookie player only when clicked, so nothing from
     YouTube loads until the visitor asks for it.
   ============================================================ */

(function () {
  'use strict';

  var dialog, img, caption, lastTrigger;

  function buildDialog() {
    dialog = document.createElement('div');
    dialog.className = 'lightbox';
    dialog.setAttribute('role', 'dialog');
    dialog.setAttribute('aria-modal', 'true');
    dialog.setAttribute('aria-label', 'Image viewer');
    dialog.hidden = true;
    dialog.innerHTML =
      '<figure class="lightbox-figure">' +
      '<button type="button" class="lightbox-close" aria-label="Close image">&times;</button>' +
      '<img alt="">' +
      '<figcaption></figcaption>' +
      '</figure>';
    document.body.appendChild(dialog);
    img = dialog.querySelector('img');
    caption = dialog.querySelector('figcaption');
    dialog.addEventListener('click', function (e) {
      if (e.target === dialog || e.target.classList.contains('lightbox-close')) close();
    });
  }

  function open(trigger) {
    if (!dialog) buildDialog();
    lastTrigger = trigger;
    var thumb = trigger.querySelector('img');
    img.src = trigger.getAttribute('href');
    img.alt = thumb ? thumb.alt : '';
    caption.textContent = trigger.getAttribute('data-lightbox') || '';
    dialog.hidden = false;
    document.body.style.overflow = 'hidden';
    dialog.querySelector('.lightbox-close').focus();
  }

  function close() {
    dialog.hidden = true;
    document.body.style.overflow = '';
    if (lastTrigger) lastTrigger.focus();
  }

  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('a[data-lightbox]');
    if (t) {
      e.preventDefault();
      open(t);
      return;
    }
    var yt = e.target.closest && e.target.closest('button[data-youtube]');
    if (yt) {
      var frame = document.createElement('iframe');
      frame.src = 'https://www.youtube-nocookie.com/embed/' + yt.getAttribute('data-youtube') + '?autoplay=1&rel=0';
      frame.title = yt.getAttribute('aria-label') || 'YouTube video';
      frame.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      frame.allowFullscreen = true;
      frame.className = 'video-frame';
      yt.replaceWith(frame);
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && dialog && !dialog.hidden) close();
  });
})();
