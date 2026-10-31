// BLV Projects - small site behaviours (no dependencies)
(function () {
  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // YouTube: load the real player only when the visitor clicks (faster pages)
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.yt-play');
    if (!btn) return;
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + btn.dataset.id + '?autoplay=1&rel=0';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
    iframe.allowFullscreen = true;
    iframe.title = btn.getAttribute('aria-label') || 'YouTube video';
    btn.replaceWith(iframe);
  });

  // Keep the active project tab visible on small screens
  var active = document.querySelector('.tabs a.active');
  if (active && active.scrollIntoView) {
    var bar = active.parentElement;
    bar.scrollLeft = active.offsetLeft - (bar.clientWidth - active.clientWidth) / 2;
  }
})();

// Gallery lightbox
document.addEventListener('click', function (e) {
  var img = e.target.closest('.gallery img');
  if (img && !img.closest('a')) {
    var box = document.createElement('div');
    box.className = 'lightbox';
    var big = document.createElement('img');
    big.src = img.currentSrc || img.src;
    big.alt = img.alt;
    box.appendChild(big);
    box.addEventListener('click', function () { box.remove(); });
    document.body.appendChild(box);
    return;
  }
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') { var b = document.querySelector('.lightbox'); if (b) b.remove(); }
});
