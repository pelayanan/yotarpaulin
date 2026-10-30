# AGENTS.md — Website YO TERPAL NUSANTARA RAYA (yoterpal.com)

Repo: https://github.com/pelayanan/yotarpaulin (public) · branch `main` · working copy = folder ini (git user sudah diset: pelayanan / yonusantararaya@gmail.com).
Live: https://yoterpal.com (GitHub Pages + Cloudflare proxy, CNAME di root). **JANGAN build lokal** (tidak ada Ruby/Jekyll/Chrome) — push ke main, GitHub Pages yang build.
**Token GitHub TIDAK BOLEH di dalam repo** (ambil dari remote URL git).

## Identitas & kontak (state kini)
- Brand teks: **YO TERPAL NUSANTARA RAYA** (bukan "YO Tarpaulin"). Dioperasikan CV. Yo Terpal Nusantara Raya. Owner: **Yoke Albertin Sumayow**, peran hanya "Owner" — kata "Pendiri" tidak boleh muncul.
- WA/telepon UTAMA (semua CTA): **+62 822-13-8889** (wa.me/62822138889); alternatif (kontak saja): +62 812-2133-2929. Email yonusantararaya@gmail.com. IG/Threads/TikTok @pabrik_plastik_termurah. Alamat: Amesta Living, Gunung Anyar Tambak, Surabaya.
- Warna: navy --blue-950 #041630 … --blue-500 #2079e0; aksen ORANYE (`--yellow: #ff8a1f` — nama var memang kuning, JANGAN rename). Font: Barlow Condensed + Plus Jakarta Sans (Google Fonts).
- customer-facing material tidak boleh menyebut "merek dagang / gratisan / GitHub".

## URL (semua permalink folder-style, tanpa .html)
- ID (10 produk): / /produk/ /tentang/ /galeri/ /keunggulan/ /aplikasi/ /kontak/ /404.html /produk/<slug>/ ×10. Slug: terpal-biru-premium, terpal-navy, terpal-kuning-gold, terpal-hijau, terpal-oranye, terpal-pvc-transparan, terpal-roll, paranet-bangunan, terpal-biru-muda, tas-spunbond. Plus /compro-yoterpal/ (HTML 11 hal) & dokumen /proposal-website/ /kwitansi-dp/ /kwitansi-pelunasan/.
- EN: /en/ /en/products/ /en/about/ /en/gallery/ /en/advantages/ /en/applications/ /en/contact/ /en/products/<slug-en>/ ×10. Padanan 1:1: blue-premium-tarpaulin, navy-tarpaulin, gold-yellow-tarpaulin, green-tarpaulin, orange-tarpaulin, transparent-pvc-tarpaulin, industrial-tarpaulin-roll, light-blue-tarpaulin, construction-shade-net, spunbond-bag.
- Setiap halaman WAJIB punya front matter `lang: id|en` + `lang_other: <url pasangannya>` (eksplisit, bukan auto). hreflang id/en/x-default otomatis dari head.html saat page.lang & page.lang_other. Switcher bahasa berbendera (🇮🇩/🇺🇸) di kedua header + footer.

## Struktur & data
- Katalog: `_data/products.yml` (ID) + `products_en.yml` (EN) — struktur sama, image SHARED, slug beda. Halaman produk = stub front matter (layout `product`/`product_en`) + layout baca data by `page.slug`; konten cukup edit di YAML.
- Data EN lain: navigation_en / advantages_en / applications_en / steps_en. Include EN: `_includes/en/*` (banner-promo di-reuse dari ID). Layout EN: `_layouts/default_en.html` (lang="en") + `product_en.html`.
- Form WA (`#wa-form`) dibaca main.js — bilingual otomatis dari `document.documentElement.lang`. Field name template: nama/kebutuhan/jumlah/lokasi/pesan (dipakai kedua bahasa).

## Workflow rilis & verifikasi
1. Edit → commit per topik → push main. 2. ±60 dtk → cek `GET /repos/pelayanan/yotarpaulin/pages/builds/latest` (token dari remote URL) → status "built" + commit cocok. 3. Verifikasi live: curl + cache-buster `?v=$(date +%s)` (HTTP kode, grep elemen, ukuran file vs repo). Screenshot via Playwright — cek build "built" dulu (bisa dapat CSS lama). 4. Update AGENTS.md tiap perubahan → commit terpisah.

## Gotcha terbukti (jangan diulang)
- og:image = JPEG (WhatsApp/FB) — KECUALI og-default.webp kini og:image utama (fallback og-default.jpg tersedia). `og-default` = desain owner — **DILARANG rebuild dari make_og*_ ** (script menimpa desain; `make_og.py` utuh juga menghancurkan og-default via brand_card; regen kartu per-banner manual via fungsi cover()).
- Ganti gambar beda rasio → WAJIB update atribut `width`/`height` HTML (CSS width:100% tanpa height:auto → stretch). Ganti file gambar nama sama → naikkan `?v=N` manual di SEMUA ref (banner kini `?v=2`); build_compro.py sudah auto-strip `?v=`.
- Edit/batch front matter: LINE-BASED pada baris fence penutup (`lines.index("---",1)`) — offset karakter sudah 2× bikin file rusak (fm hilang, leak teks ke body).
- `git rm` multi-pathspec itu ATOMIK — satu path typo = tidak ada yang terhapus (pernah bikin stub produk lolos live).
- Hati-hati bar hitam tertanam di foto WhatsApp (trim sebelum crop). `.apps--3` wajib ditulis SETELAH `.apps` (cascade). 404.html tetap `permalink: /404.html` (kebutuhan GH Pages).
- PDF env: WeasyPrint 61.1 + **pydyf==0.8.0** wajib (`pip3 install --break-system-packages`), tanpa grid/gap/flex-gap (shim table), emoji dihindari, fixed page height untuk multi-halaman; verifikasi pdfinfo/pdftoppm/pdftotext.
- Cache Cloudflare ±10 mnt: file lama bisa tayang setelah build — pakai cache-buster; sebaliknya pages-build status wajib "built" dulu.

## Tool & script (server agent, /root/opencode — hilang saat restart, cara rebuild ada di log AGENTS lama/git history)
- `fix_og_chip.py` — patch chip nomor og-default (referensi). `build_compro.py` — regen compro PDF 11 hal via WeasyPrint (saat ini TIDAK dipakai, lihat backlog).
- Verifikasi visual: PIL 11.3 + numpy, poppler-utils, Playwright chromium (apt chromium = snap stub rusak, jangan).

## Backlog / hal terbuka (menunggu owner)
- og:image halaman EN masih kartu versi ID (teks Indonesia) — bisa regen EN-specific bila diminta.
- /compro-yoterpal/ (HTML 11 hal) masih live terpisah dari compro-yoterpal.pdf = file "blue" milik owner (4 hal, md5 d0174f5a…; di dalamnya masih "Yoke Albertin" tanpa Sumayow) — sinkron/hapus tunggu keputusan owner.
- /kwitansi-pelunasan/ (No. 002) masih live padahal pelunasan belum dibayar.
- DNS: www.yoterpal.com belum ada record; http→https belum redirect (Always Use HTTPS di Cloudflare kalau owner setuju).
- Caption "YO Terpaulin" sengaja tetap (merujuk logo fisik produk) — jangan diganti tanpa perintah.
- banner-payment.webp belum di-branding baru — tanyakan owner.

---
# LOG PERUBAHAN (ringkas, terbaru dulu)
- 30 Okt `a0eb438`: banner-client.webp ganti desain baru owner ("Apa Kata Mereka?", testimoni 5 bintang Pak Budi Pengusaha Logistik, wajah customer biru-oranye, chip WA 0822138889) — native 1280x831 (rasio beda dari lama 1200x779), ?v=3 di 5 ref (index, en/index, kontak, en/contact, compro), 147 KB; terverifikasi built + render live.
- 30 Okt `c3dce35`: banner-struktur.webp ganti desain baru owner ("Struktur & Ketebalan Terpal Berkualitas", diagram 5 lapisan multi-layer, jangka sorong) — native 1280x720 (16:9, align dari 1200x676), ?v=3 di 3 ref (includes distribusi ID+EN, compro), 154 KB; terverifikasi built + render live.
- 30 Okt `fecc298`: banner-distribusi.webp ganti desain baru owner ("Jaringan Distribusi Nasional", peta Indonesia bergaya digital, 3 badge 34+ provinsi/ratusan mitra/armada) — native 1280x477 (dimensi align, rasio NYARIS sama dengan lama 1200x447), ?v=3 di 5 ref (includes distribusi ID+EN, tentang, en/about, compro), 115 KB; terverifikasi built + render live.
- 30 Okt `cab1ae6`: banner-custom.webp ganti desain baru owner ("Butuh Terpal dengan Ukuran Custom?", roll terpal warna, ikon 3 benefit, CTA kuning) — native 1280x915 (rasio beda dari lama 1200x859, width/height 2 ref include proses ID+EN di-update), ?v=3 di 3 ref (termasuk compro-yoterpal.html), 178 KB; tampil di / dan /en/; terverifikasi built + render live.
- 30 Okt `dbf3053`: banner-promo.webp ganti desain baru owner (promo diskon s.d. 30% terpal heavy duty, truk terpal biru, chip WA 0822138889) — native 1280x426 (rasio beda dari lama 1200x387, width/height 1 ref include banner-promo di-update), ?v=3, 119 KB; tampil di / dan /en/; terverifikasi built + render live.
- 30 Okt `f243eeb`: banner-kenapa.webp ganti desain baru owner (6 kartu keunggulan, navy+oranye, chip WA 0822138889) — native 1280x426 (rasio beda dari lama 1200x332, width/height semua 4 ref di-update), ?v=3, 89,8 KB; terverifikasi built + render live tanpa stretch.
- 31 Okt `af266cf`+`686a03b`: FIX leak front matter (`lang: id lang_other: /en/` tampil di body 17 hal ID — offset script salah; line-based fix).
- 31 Okt `374fd4f`+`2f78e75`: SITUS EN /en/ penuh (17 hal, data _en, includes en/, layout default_en/product_en, switcher berbendera, hreflang, form WA bilingual, brand_slogan_en).
- 31 Okt `6752d2a`(foto galeri-hero di seksi Tentang beranda) `6235bac`(banner ?v=2 + fix width/height dimensi) `b91f512`(7 banner rebrand dari koleksi owner + og-produk/tentang/keunggulan regen + compro rebuild) `0d37a38`(og-default webp 76KB + fallback jpg) `6305729`(swap nomor utama/alternatif di config/js/include/compro) `0e3db8f`(compro PDF = versi blue owner 4 hal, teks ±3,4 MB) `880bb42`(nama owner Sumayow + role Owner, guard .exp-badge).
- 30 Okt: Cancelar produk sarung tangan, og card redesign putih-biru-oranye, invoice/QRIS, cleanup "merek dagang/gratisan", compro clickable, kwitansi 002, proposal Rev2.
- 29 Okt: redesign oranye + biru gelap, rebrand teks semua → YO TERPAL NUSANTARA RAYA, logo merek 6 buah, nav dropdown/Tentang, ikon sosial, Maps embed, clean URL, og cards semua halaman, keunggulan.html & aplikasi.html.
- 28 Okt: domain kustom, repo pindah ke working copy, dokumen/invoice/proposal di-commit atas keputusan owner.
