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

- Sambutan Owner (30 Okt 2026): seksi "Sambutan Owner — Salam Hangat dari Pendiri Kami" di tentang.html (setelah Profil Perusahaan, sebelum Nilai Kami): foto `assets/images/owner-yoke-albertin.webp` (820×1231, konversi dari resources/owner/yoke-albertin-owner.png, q82) + 3 paragraf sambutan + signature "Yoke Albertin — Owner — CV. Yo Terpal Nusantara Raya". CSS `.owner__*` dekat blok `.brand-grid` di styles.scss. Nav topbar kini teks **YO TERPAL NUSANTARA RAYA** (commit `427f71a`) — nama panjang: `.site-header .brand__text strong` nowrap + media ≤1250px mengecilkan brand/ font/ pengenturan nav__link agar muat.
- Seksi "Merek Kami" jadi include `_includes/merek.html` (commit `765e5a9`), dipakai beranda (index.html, sebelum banner client) + tentang.html; tombol "Kenali Profil Pabrik Kami" menuju tentang.html.
- Footer kontak: dua baris "WhatsApp 1 / WhatsApp 2" klik ke wa.me (commit `f47d055`); baris tel: dihapus dari footer (tel masih di topbar & kontak.html).

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
- Anti-cache CDN: `<link>` CSS & `<script>` JS memakai `?v={{ site.time | date: '%Y%m%d%H%M' }}` — berubah tiap build, update tak tertahan cache Cloudflare. Gambar tak pakai version query (cache CF expired sendiri ±10 menit).- Nav desktop dirapikan via submenu (29 Okt 2026, commit `700a473`): menu top-level kini 5 (Beranda, Tentang, Produk, Informasi, Kontak). `_data/navigation.yml` kini mendukung `children:` — header merender panel `.nav__dd-panel` generik; `dropdown: true` khusus Produk tetap baca products.yml dan panel ditutup tautan `.nav__dd-all` "Lihat Semua Produk →" (CSS di blok dropdown). Tentang ▾ = Profil/Sambutan Owner (`tentang.html#owner`)/Galeri/Merek (`tentang.html#merek`, id ditambahkan ke section owner & include merek.html); Informasi ▾ = Keunggulan/Aplikasi/Cara Pemesanan (`/#proses`). Mobile ≤860 otomatis inline karena panel memakai class yang sama.
- Nav update (29 Okt 2026, commit `357fec9`): submenu Informasi DIHAPUS. Keunggulan & Aplikasi masuk submenu Tentang (kini 6: Profil, Sambutan Owner, Galeri, Merek #merek, Keunggulan, Aplikasi). "Cara Pemesanan" pindah ke panel Produk via field `extra:` baru di navigation.yml (dirender header.html sebelum tautan "Lihat Semua Produk"). Top-level kini 4: Beranda, Tentang ▾, Produk ▾, Kontak.
- Proposal Rev. 2 (30 Okt 2026, commit `eac8d77`): [proposal-website.txt](proposal-website.txt) diperbarui — daftar halaman live lengkap (20 URL, semua HTTP 200 verifikasi curl, hal. tas-spunbond belum live tidak dimasukkan) + seksi "BIAYA TAHUNAN": Rp 1.500.000/tahun aktif mulai 1 November 2026 (s.d. 31 Okt 2027), dibayar ulang 1 November 2027 sebesar Rp 1.500.000. PDF baru dibuat dari [proposal-website.html](proposal-website.html) (4 halaman A4, style burgundy/stempel Aksisoft sama seperti kwitansi DP, print Chrome headless) → `Proposal-Penawaran-Website-YO-Tarpaulin-Aksisoft-Rev2.pdf`; PDF lama Rev. 1 TIDAK diganti. Keduanya live di yoterpal.com — file ini TIDAK masuk exclude _config (berbeda dari PDF/txt lama yang disembunyikan).
- Kwitansi pelunasan (30 Okt 2026): [kwitansi-pelunasan.html](kwitansi-pelunasan.html) + `Kwitansi-Pelunasan-50persen-Website-YO-Tarpaulin-Aksisoft.pdf` (No. 002/KWT/AKS/X/2026, Rp 2.500.000, tanggal 30 Okt 2026). Template & styling identik kwitansi DP (No. 001). Fix khusus: `html{overflow:hidden}` + body height 148.4mm agar print tidak memunculkan halaman-2 kosong. Keduanya live di yoterpal.com root.
- Company profile (30 Okt 2026): [compro-yoterpal.html](compro-yoterpal.html) + `compro-yoterpal.pdf` (11 halaman A4, ±4,8 MB) live di yoterpal.com root. Isi = seluruh konten website: cover navy, tentang+nilai, sambutan owner, keunggulan+kurasi foto produksi, katalog terpal PE (6 kartu, hal. 5) + PVC/roll/TAS (hal. 6), paranet+tabel varian K50–K100 (hal. 7), 10 aplikasi, 4 langkah pemesanan+ready stock, 6 merek produksi, kontak (WA1/WA2/IG/Threads/email/alamat). Alur build PDF: gambar .webp di assets/images → JPEG q80 ≤1100px di `$TEMP/comproimg/` → `$TEMP/compro-build.html` (replace path) → Chrome headless print. HTML repo tetap referensi assets/images. Catatan: Chromium GRID sering digeser seutuhnya ke halaman berikut bila total tinggi baris melebihi area — pakai modifier `.prodgrid.tight` (.im 27mm) agar 6 kartu muat 1 halaman.
- Tas Spunbond (29 Okt–Nov 2026, commit `c7d684f): produk ke-11 — entry di `_data/products.yml` (category "Tas & Non-Woven", gallery 3 foto, specs/desc baru) + stub `produk/tas-spunbond.html` + baris tambahan di tabel spesifikasi produk.html. LIVE di https://yoterpal.com/produk/tas-spunbond.html (HTTP 200, verifikasi curl). 4 gambar AI-generated via pollinations.ai (model sana, seed fix): `prod-tas-spunbond.webp` (kartu 640, tote krem+navy), `tas-detail-bahan.webp` (makro bahan), `tas-stok-gudang.webp` (rak gudang), `tas-jahit.webp` (mesin jahit navy) — masing-masing di-crop 30px bawah untuk buang watermark pollinations, konversi webp q80. CATATAN PENTING: gambar ini INTERIM/AI, bukan foto asli produk & bukan dari meta.ai — CDP 9222 tab meta.ai tidak terjangkau dari environment agent (Chrome remote debugging tidak berjalan di server saat itu). Jika owner punya foto asli tas spunbond atau maupun gambar meta.ai, replace file webp di atas dengan nama sama. Karena itu proposal Rev2 (txt+PDF) belum mengupdate daftar 20 URL → informasikan owner bahwa kini URL sudah 21. Layout product.html otomatis skip seksi "Merek Produksi" untuk kategori non-Terpal/Paranet — tas spunbond seperti sarung tangan tidak menampilkan merek grid (normal). Rate limit pollinations: 1 gambar/45 dtk per IP (HTTP 402/api FREE_LIMIT saat 40x lebih cepat).
