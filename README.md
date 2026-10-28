# Yo Tarpaulin — Company Profile Website

Website company profile untuk **YO TARPAULIN** — produsen & pemasok terpal dan sarung
tangan berkualitas tinggi untuk industri pertambangan dan proyek infrastruktur skala besar.

**Live:** https://pelayanan.github.io/yotarpaulin/

## Stack

- [Jekyll](https://jekyllrb.com) (themeless — layout & styling sendiri, pola dari
  [themeless-jekyll-quickstart](https://github.com/MichaelCurrin/themeless-jekyll-quickstart))
- Build otomatis oleh **GitHub Pages** dari branch `main`
- Aset gambar dikonversi ke **WebP** untuk kecepatan muat
- Single-page landing (`index.html`) + halaman `produk.html`, `tentang.html`, `kontak.html`

## Struktur

```
_config.yml          # metadata situs, kontak brand, plugin
_data/               # navigation, products, advantages, applications, steps (YAML)
_includes/           # hero, stats, tentang, keunggulan, produk, aplikasi, proses, ...
_layouts/default.html
assets/css/styles.scss
assets/js/main.js    # nav, reveal, counter, form WhatsApp
assets/images/       # logo, ikon 3D (bg transparan), foto, banner (semua .webp)
```

## Kontak brand

- Hotline / WhatsApp: **+62 812-2133-2929**
- Layanan & pengiriman 24/7, kirim ke seluruh Indonesia
