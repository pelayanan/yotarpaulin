/* YO TERPAL NUSANTARA RAYA — interactions */
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
        "Halo YO TERPAL NUSANTARA RAYA, saya ingin bertanya tentang terpal.",
        "",
        "Nama: " + (fd.get("nama") || "-"),
        "Kebutuhan: " + (fd.get("kebutuhan") || "-"),
        "Jumlah: " + (fd.get("jumlah") || "-"),
        "Lokasi Kirim: " + (fd.get("lokasi") || "-"),
        "Detail: " + (fd.get("pesan") || "-")
      ];
      var url = "https://wa.me/62822138889?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
    });
  }

  /* Lightbox galeri — klik gambar untuk zoom, navigasi kiri/kanan */
  (function () {
    var targets = document.querySelectorAll(
      ".app img, .split__media img, .banner-wide img"
    );
    if (!targets.length) return;

    var list = Array.prototype.slice.call(targets);

    var overlay = document.createElement("div");
    overlay.className = "lightbox";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Galeri foto");
    overlay.innerHTML =
      '<div class="lightbox__backdrop"></div>' +
      '<div class="lightbox__stage"><img class="lightbox__img" alt="" draggable="false"></div>' +
      '<button type="button" class="lightbox__btn lightbox__prev" aria-label="Gambar sebelumnya">&#10094;</button>' +
      '<button type="button" class="lightbox__btn lightbox__next" aria-label="Gambar berikutnya">&#10095;</button>' +
      '<button type="button" class="lightbox__btn lightbox__close" aria-label="Tutup">&times;</button>' +
      '<div class="lightbox__cap"></div>';
    document.body.appendChild(overlay);

    var img = overlay.querySelector(".lightbox__img");
    var cap = overlay.querySelector(".lightbox__cap");
    var idx = 0, zoom = 1, panX = 0, panY = 0;

    function apply() {
      img.style.transform = "translate(" + panX + "px, " + panY + "px) scale(" + zoom + ")";
      img.classList.toggle("is-zoomed", zoom > 1.01);
    }
    function capText(el) {
      var fig = el.closest("figure");
      var strong = fig && fig.querySelector("figcaption strong");
      return (strong && strong.textContent) || el.alt || "";
    }
    function show(i) {
      idx = (i + list.length) % list.length;
      zoom = 1; panX = 0; panY = 0;
      var src = list[idx];
      img.src = src.currentSrc || src.src;
      img.alt = src.alt || "";
      cap.textContent = capText(src);
      overlay.classList.add("is-open");
      document.body.classList.add("has-lightbox");
      apply();
    }
    function hide() {
      overlay.classList.remove("is-open");
      document.body.classList.remove("has-lightbox");
    }
    function nav(d) { show(idx + d); }

    list.forEach(function (el) {
      el.addEventListener("click", function () {
        show(list.indexOf(el));
      });
    });

    overlay.querySelector(".lightbox__prev").addEventListener("click", function () { nav(-1); });
    overlay.querySelector(".lightbox__next").addEventListener("click", function () { nav(1); });
    overlay.querySelector(".lightbox__close").addEventListener("click", hide);
    overlay.querySelector(".lightbox__backdrop").addEventListener("click", hide);

    document.addEventListener("keydown", function (ev) {
      if (!overlay.classList.contains("is-open")) return;
      if (ev.key === "Escape") hide();
      else if (ev.key === "ArrowLeft") nav(-1);
      else if (ev.key === "ArrowRight") nav(1);
    });

    /* zoom dengan roda mouse, pan dengan drag saat zoom */
    var stage = overlay.querySelector(".lightbox__stage");
    stage.addEventListener("wheel", function (ev) {
      ev.preventDefault();
      zoom = Math.min(4, Math.max(1, zoom + (ev.deltaY < 0 ? 0.25 : -0.25)));
      if (zoom === 1) { panX = 0; panY = 0; }
      apply();
    }, { passive: false });

    function clampPan() {
      var mx = (img.clientWidth * (zoom - 1)) / 2, my = (img.clientHeight * (zoom - 1)) / 2;
      panX = Math.max(-mx, Math.min(mx, panX));
      panY = Math.max(-my, Math.min(my, panY));
    }
    var drag = null;
    img.addEventListener("pointerdown", function (ev) {
      if (zoom <= 1) return;
      drag = { x: ev.clientX, y: ev.clientY, px: panX, py: panY };
      img.setPointerCapture(ev.pointerId);
      ev.preventDefault();
    });
    img.addEventListener("pointermove", function (ev) {
      if (!drag) return;
      panX = drag.px + (ev.clientX - drag.x);
      panY = drag.py + (ev.clientY - drag.y);
      clampPan();
      apply();
    });
    img.addEventListener("pointerup", function () { drag = null; });
    img.addEventListener("pointercancel", function () { drag = null; });
    img.addEventListener("dblclick", function () {
      if (zoom > 1) { zoom = 1; panX = 0; panY = 0; } else { zoom = 2; panX = 0; panY = 0; }
      apply();
    });
  })();

  /* Footer year fallback (Jekyll date is build time) */
  var yearEl = document.querySelector(".footer__bottom span");
  if (yearEl) {
    var now = new Date().getFullYear();
    yearEl.textContent = yearEl.textContent.replace(/\d{4}/, now);
  }
})();
