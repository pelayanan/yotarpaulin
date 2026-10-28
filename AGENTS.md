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

- Live URL: https://pelayanan.github.io/yotarpaulin/ (GitHub Pages, build otomatis dari branch main, baseurl `/yotarpaulin`)
- Halaman live: `/` (beranda), `/produk.html`, `/tentang.html`, `/kontak.html`, `/404.html`, `/sitemap.xml`, `/robots.txt`
- Kode sumber: https://github.com/pelayanan/yotarpaulin (public)
- Kontak brand di website: hotline/WhatsApp +62 812-2133-2929 (wa.me/6281221332929)

## Cara kerja yang sudah terbukti

- Edit di `/mnt/f/buildapk/website-yotarpaulin/` (FOLDER INI) → commit → push ke `main` → GitHub Pages build otomatis (cek status: `GET /repos/pelayanan/yotarpaulin/pages/builds/latest` dengan token di atas).
- Jangan build lokal (tidak ada Ruby/Jekyll di mesin ini). Untuk preview/screenshot pakai `chromium --headless=new --screenshot=... --window-size=1440,<tinggi>` terhadap URL live.
- Ketersediaan domain dicek via RDAP: Verisign `https://rdap.verisign.com/com/v1/domain/<domain>` untuk .com/.net, PANDI `https://rdap.pandi.id/rdap/domain/<domain>` untuk .id/.co.id/.web.id. 404 = tersedia, 200 = terdaftar. Per 28 Okt 2026 semua varian yotarpaulin (.com/.net/.co/.id/.co.id/.web.id/.biz/.store) masih tersedia.