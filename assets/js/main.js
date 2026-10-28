/* YO TARPAULIN — interactions */
(function () {
  "use strict";

  /* Sticky header shadow */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Close mobile nav when a link is clicked */
  var toggle = document.getElementById("nav-toggle");
  if (toggle) {
    document.querySelectorAll(".nav a").forEach(function (a) {
      a.addEventListener("click", function () { toggle.checked = false; });
    });
  }

  /* Scroll reveal */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("is-visible");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* Animated counters */
  function animateCount(el) {
    var target = parseInt(el.getAttribute("data-count"), 10) || 0;
    var suffix = el.getAttribute("data-suffix") || "";
    var dur = 1400;
    var start = null;
    function tick(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var counters = document.querySelectorAll(".stat__num[data-count]");
  if ("IntersectionObserver" in window && counters.length) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          animateCount(e.target);
          cio.unobserve(e.target);
        }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* WhatsApp order form */
  var form = document.getElementById("wa-form");
  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var fd = new FormData(form);
      var lines = [
        "Halo YO TARPAULIN, saya ingin bertanya tentang terpal/sarung tangan.",
        "",
        "Nama: " + (fd.get("nama") || "-"),
        "Kebutuhan: " + (fd.get("kebutuhan") || "-"),
        "Jumlah: " + (fd.get("jumlah") || "-"),
        "Lokasi Kirim: " + (fd.get("lokasi") || "-"),
        "Detail: " + (fd.get("pesan") || "-")
      ];
      var url = "https://wa.me/6281221332929?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
    });
  }

  /* Footer year fallback (Jekyll date is build time) */
  var yearEl = document.querySelector(".footer__bottom span");
  if (yearEl) {
    var now = new Date().getFullYear();
    yearEl.textContent = yearEl.textContent.replace(/\d{4}/, now);
  }
})();
