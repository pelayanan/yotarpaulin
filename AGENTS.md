bisa login ke repo ku pelayanan token github :: /mnt/f/pelayanan-token.txt atau di window F:/pelayanan-token.txt

cari REPO https://github.com/pelayanan/yotarpaulin
ini adalah project anda.

Baca dulu repo.

ini adalah website yang akan dibuild menggunakan jekyll.
pakai jekyll template bisa pakai ini. 
https://github.com/MichaelCurrin/themeless-jekyll-quickstart/tree/master

karena ini website compro public jadi website public / repo public

replika website ini : https://www.heshengplasticindustry.com/

rebranding ke " Yo Tarpaulin "
Logo pakai yo tarpaulin : https://cd1.edir.workers.dev/b7718968b8-yo-tarpaulin-logo.png (download dan serve lokal jangan pakai cdn, misalnya image/logo.png)

Hotline no telp : +62 812-2133-2929

short description : YO Terpaulin merupakan perusahaan yang bergerak di bidang Produksi & Penyediaan Terpal,Sarung Tangan yang berkualitas tinggi untuk kebutuhan industri pertambangan dan proyek infrastruktur skala besar

Gunakan resources di folder resources
Template rekomendasi di resources\Yo Tarpaulin_ Quality Covers for Every Journey.png

jangan build lokal, build pakai github repo. kalau github repo limit, stop dulu gapapa. saya cari solusi lain.

jika halaman kurang panjang, panjangkan sesuai dengan resources yang ada, gapapa.
kalau butuh png, remove background putih dari /resources.

kebutuhan gambar ada di folder resources

penting. convert gambar supaya lebih cepat di load di website, biasanya .webp

push lalu cek github online url.

---

# CATATAN LOKASI PROJECT (WAJIB DIBACA AGENT BERIKUTNYA)

Website SUDAH jadi dan live. Struktur folder saat ini:

## Lokasi penting (di luar & di dalam folder project ini)

- **Repo website (working copy git)**: FOLDER INI, `/mnt/f/buildapk/website-yotarpaulin/` (window: `F:/buildapk/website-yotarpaulin/`).
  - Sejak 28 Okt 2026 working copy git repo https://github.com/pelayanan/yotarpaulin (branch main) berada di folder ini, lengkap dengan `.git`.
  - Semua perubahan website & konten dilakukan di FOLDER INI, lalu `git push origin main`.
  - Struktur repo: `_config.yml`, `_data/` (navigation, products, advantages, applications, steps), `_includes/`, `_layouts/default.html`, `index.html`, `produk.html`, `tentang.html`, `kontak.html`, `404.html`, `assets/css/styles.scss`, `assets/js/main.js`, `assets/images/` (semua .webp + favicon.png) + file lokal di bawah ini yang sengaja ikut di-commit atas keputusan pemilik.
- **Backup repo lama**: `/mnt/f/buildapk/repo-yotarpaulin/` — salinan working copy SEBELUM dipindah (masih punya `.git`). Hanya backup, JANGAN diedit/dipush dari sini.
- **Template referensi (clone)**: `/mnt/f/buildapk/template-quickstart/` — salinan themeless-jekyll-quickstart, hanya referensi, tidak perlu diubah.
- **File lokal di folder ini (sudah di-commit ke repo publik atas keputusan pemilik, 28 Okt 2026)**:
  - `resources/` — sumber gambar asli (logo, banner, foto produk, ikon 3D). Jangan dihapus.
  - `screenshoot/` — screenshot JPEG semua halaman live (01-halaman-beranda.jpg s/d 06-tampilan-mobile.jpg) untuk dikirim ke customer.
  - `Proposal-Penawaran-Website-YO-Tarpaulin-Aksisoft.pdf` — proposal penawaran jasa pembuatan website dari Aksisoft Media (aksisoft.web.id, WA 0813-3520-6389), Rp 5.000.000 nego. 12 halaman: cover, tentang, ruang lingkup + daftar URL live, pratinjau, rekomendasi domain (semua cek RDAP: tersedia), investasi & TTD, lampiran A–F screenshot. PEMILIK SADAR & MENGAJINKAN file ini ter-publish di repo publik.
  - `proposal-website.txt` — versi teks proposal (berisi harga & kontak) juga ter-publish, sama seperti di atas.
  - `AGENTS.md` — file ini.
  - Catatan: file token GitHub TIDAK di dalam repo. Token tetap di `F:/pelayanan-token.txt` (di luar repo, jangan pernah disalin ke dalam repo).

## Status website

- Live URL: https://yoterpal.com/ (domain kustom atas keputusan pemilik, 28 Okt 2026; CNAME file di root repo, `url: https://yoterpal.com`, `baseurl: ""`). URL lama https://pelayanan.github.io/yotarpaulin/ otomatis redirect ke domain baru.
- Catatan domain (28 Okt 2026): DNS apex via Cloudflare PROXY (orange). HTTPS pengunjung memakai sertifikat Cloudflare — sudah berfungsi. Sertifikat GitHub untuk yoterpal.com belum ter-terbit (proxy Cloudflare menghalangi validasi LE; normal jika proxy dipakai). `https_enforced` di GitHub tetap False — OK, jangan dipaksa. **http://yoterpal.com/ masih 200 (belum redirect ke https)** → aktifkan "Always Use HTTPS" di dashboard Cloudflare. Subdomain `www.yoterpal.com` BELUM ada DNS record — tambahkan CNAME `www` → `pelayanan.github.io` (atau → yoterpal.com) agar www juga jalan.
- Halaman live: `/` (beranda), `/produk.html`, `/tentang.html`, `/galeri.html`, `/keunggulan.html`, `/aplikasi.html`, `/kontak.html`, `/404.html`, `/sitemap.xml`, `/robots.txt` + **halaman detail per produk `/produk/<slug>.html` (10 halaman)**. Halaman `/keunggulan.html` & `/aplikasi.html` dibuat 29 Okt 2026 (commit `ed2c104`) untuk SEO — konten unik (intro merek, note-grid standar kerja, FAQ mutu; panduan pemilihan GSM/pemasangan/ukuran); seksi beranda `#keunggulan` & `#aplikasi` tetap ada sebagai teaser + tombol menuju halaman dedicated; nav & footer kini link ke halaman dedicated, bukan anchor beranda.
- Kode sumber: https://github.com/pelayanan/yotarpaulin (public)
- Kontak brand di website: hotline/WhatsApp +62 812-2133-2929 (wa.me/6281221332929)

## Cara kerja yang sudah terbukti

- Edit di `/mnt/f/buildapk/website-yotarpaulin/` (FOLDER INI) → commit → push ke `main` → GitHub Pages build otomatis (cek status: `GET /repos/pelayanan/yotarpaulin/pages/builds/latest` dengan token di atas).
- Jangan build lokal (tidak ada Ruby/Jekyll di mesin ini). Untuk preview/screenshot pakai `chromium --headless=new --screenshot=... --window-size=1440,<tinggi>` terhadap URL live.
- Ketersediaan domain dicek via RDAP: Verisign `https://rdap.verisign.com/com/v1/domain/<domain>` untuk .com/.net, PANDI `https://rdap.pandi.id/rdap/domain/<domain>` untuk .id/.co.id/.web.id. 404 = tersedia, 200 = terdaftar. Per 28 Okt 2026 semua varian yotarpaulin (.com/.net/.co/.id/.co.id/.web.id/.biz/.store) masih tersedia.

## Produk & halaman detail (28 Okt 2026)

- Katalog = `_data/products.yml` (10 produk; tiap entri punya `slug`, `detail`, `uses`; paranet punya `banner` + `gallery`).
- Halaman detail: layout `_layouts/product.html` + stub `produk/<slug>.html` (front matter: layout/slug/permalink/title/description). Data-driven — konten produk cukup diedit di products.yml.
- Foto paranet: `assets/images/prod-paranet.webp` (kartu 640), `paranet-loom.webp` (banner), `paranet-tenun.webp`, `paranet-k100..k50.webp` (varian kerapatan 50–100% dengan label ukuran/berat asli dari foto stok). Sumber: `resources/product-paranet/`.
- Logo merek produksi (29 Okt 2026, commit `9d6549a`): `assets/images/brand-yo-terpaulin.png` (merah 900×627), `brand-saffron-a20.png` (900×245), `brand-perkasa-terpal.png` (900×758), `brand-yo-terpauline-a20.png` (varian hitam vektor, belum dipakai di halaman). Tampil sebagai seksi "Merek Kami — Logo yang Tercetak di Produk Kami" di BAWAH halaman tentang.html (setelah Komitmen, sebelum CTA) + CSS `.brand-grid/.brand-card` di akhir styles.scss. Semua PNG transparan; tulisan/tagline di bawah logo di-crop sesuai permintaan pemilik (YO & Saffron tagline ter-crop, Perkasa label UKURAN/TYPE + garis diagonal ter-crop). Sumber mentah: `resources/terpal-sublogo/` (2 JPEG + 2 PDF, masih untracked). Trik proses: PDF vektor dirender pymupdf lalu alpha=255−L; JPEG pakai flood-fill putih dari tepi (numpy, tanpa scipy); garis diagonal Perkasa di-erase via mask warna merah x≥1160/y≤520 + filter speck 7×7 zona pojok — JANGAN erase merah x≥1185 semua-y karena bawah-terpal-merah elang sampai x≈1239.
- Logo merek paranet (29 Okt 2026, commit `e93e16e`): `assets/images/brand-surya-paranet.png` (900×517), `brand-nusantara-net.png` (541×498), `brand-perkasa-paranet.png` (900×210) — seksi "Merek Kami" tentang.html kini 6 kartu (2×3). Sumber: `resources/logo-paranet/` (3 JPEG WhatsApp, masih untracked). Proses: SURYA crop y≤860 (tagline 876–930 buang) + median filter 5 (latar 240, anti-noise); NUSANTARA crop rect (200,218,742,716) = kolom kiri label (ilustrasi+wordmark; badge 736–811 & kotak UKURAN/SHADING kanan & border hijau x158–164/1440–1446 terbuang); PERKASA erase badge (383,130–940,206) + SHAFA (840,240–1066,290) lalu crop (28,38,1038,280). Alpha = mapping global L→alpha (putih→transparan TANPA flood; lubang jaring ikut transparan — aman di kartu putih) + despeckle tetangga. Lockup PERKASA PARANET lebar (900×210) tampil ±74px tinggi via object-fit contain — normal, jangan dianggap bug.
- Nomor kontak ganda (29 Okt 2026, commit `6820b52`): nomor utama tetap `+62 812-2133-2929` (dipakai SEMUA CTA: header "Hubungi Kami", wa-float, form WA, CTA produk). Nomor alternatif `+62 822-13-8889` (wa.me/62822138889) HANYA tampil di: kartu "WhatsApp Alternatif" kontak.html (6 kartu, ikon ic-konsultasi) + baris kedua di footer Kontak. Variabel: `phone2_display/phone2_raw/whatsapp2` di _config.yml. Hati-hati cache Cloudflare/Chrome saat verifikasi HTML (bukan CSS) — pakai cache-buster `?v=<commit>` di URL.
- Ikon sosial (29 Okt 2026, commit `869468b` + `0ac0c6b`): Instagram & Threads (username sama `pabrik_plastik_termurah`) — ikon SVG inline (sprite `#i-ig`/`#i-threads` di header.html, path simple-icons). Tampil: 2 tombol bulat `.nav__soc` di main nav (dalam `.nav__socs`, `display:contents` desktop / flex row di panel mobile ≤860) + `.footer__social` 3 tombol bulat (IG, Threads, WA) di kolom kiri footer. URL via `site.instagram` / `site.threads` + `site.social.links` (JSON-LD sameAs). Mobile nav diuji via CDP `mobile-test.mjs` (emulasi viewport HARUS satu sesi WS — setDeviceMetricsOverride hilang kalau sesi ditutup; klien `cdp.mjs` stateless per perintah). Screenshot headless 1024px menampilkan overlap palsu (artefak font-loading race) — verifikasi via CDP emulasi asli. Media query: ≤1150 nav__link padding 9px; 951–1150 nav__cta nowrap.
- Embed Google Maps (29 Okt 2026, commit `c18add0`): halaman kontak.html punya blok `.map-box` ("Lokasi Kami") — iframe embed RESMI gratis tanpa API key dari dialog Bagikan → Sematkan peta (place "Amesta Living", pin `-7.3398223, 112.8104044`, plus code MRM45+V9P, place token `0x2dd7fbd94f29ca71:0xf45a7d82e6e8dfbc`). Link "Buka di Google Maps" ke URL place lengkap. JANGAN buka URL embed langsung (muncul "must be used in an iframe") — itu normal. CSS `.map-box` di akhir styles.scss. Chrome CDP user port 4006 dipakai untuk ambil embed (klien minimal: `Temp\opencode\cdp.mjs`). Screenshot headless sering membiarkan iframe lazy-load kosong — verifikasi via CDP browser asli.
- Hati-hati: sebagian foto WhatsApp punya **bar hitam sisi tertanam** — selalu trim bar hitam (cek kecerahan kolom < 22) sebelum crop.
- CSS: kartu produk berlink detail (`.product__links`), breadcrumb `.crumb`, grid varian portrait `.apps--tall` (rasio 3/4), tombol ghost untuk latar terang `.btn--ghost--light`. `.apps--3` WAJIB ditulis SETELAH `.apps` (urutan cascade) agar grid 3 kolom tidak tertimpa 5 kolom.
- Anti-cache CDN: `<link>` CSS & `<script>` JS memakai `?v={{ site.time | date: '%Y%m%d%H%M' }}` — berubah tiap build, update tak tertahan cache Cloudflare. Gambar tak pakai version query (cache CF expired sendiri ±10 menit).