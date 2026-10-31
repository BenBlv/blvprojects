// YouTube videos load only when clicked (faster pages, no tracking until play)
document.addEventListener("click", function (e) {
  var btn = e.target.closest(".yt-play");
  if (!btn) return;
  var iframe = document.createElement("iframe");
  iframe.src = "https://www.youtube-nocookie.com/embed/" + btn.dataset.id + "?autoplay=1&rel=0";
  iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
  iframe.allowFullscreen = true;
  iframe.title = btn.getAttribute("aria-label") || "YouTube video";
  btn.replaceWith(iframe);
});
