#!/usr/bin/env python3
"""Buat kartu OG 1200x630 JPEG untuk semua halaman yoterpal.com (og:image)."""
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

SRC = "assets/images"
OUT = os.path.join(SRC, "og")
os.makedirs(OUT, exist_ok=True)
W, H = 1200, 630
Q = 82
NAVY = (10, 49, 104)


def cover(src, dst, bg=(255, 255, 255)):
    """Center-crop cover ke 1200x630, simpan JPEG q82."""
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    if im.mode in ("RGBA", "LA", "P"):
        base = Image.new("RGB", im.size, bg)
        base.paste(im, mask=im.convert("RGBA").split()[-1])
        im = base
    else:
        im = im.convert("RGB")
    # cover: crop tengah rasio 1200:630
    target = W / H
    ratio = im.width / im.height
    if ratio > target:  # terlalu lebar -> crop kiri/kanan
        nw = int(im.height * target)
        x = (im.width - nw) // 2
        im = im.crop((x, 0, x + nw, im.height))
    else:  # terlalu tinggi -> crop atas/tengah (unduh offset 35% dari atas)
        nh = int(im.width / target)
        y = min(int((im.height - nh) * 0.35), im.height - nh)
        im = im.crop((0, y, im.width, y + nh))
    im = im.resize((W, H), Image.LANCZOS)
    im.save(dst, "JPEG", quality=Q, optimize=True, progressive=True)
    print(dst, os.path.getsize(dst))


def font(size, bold=True):
    path = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else \
           "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
    return ImageFont.truetype(path, size)


def brand_card(dst):
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    # strip aksen
    d.rectangle([0, 0, 90, H], fill=(0, 65, 141))
    d.rectangle([0, H - 26, W, H], fill=(255, 214, 0))
    # logo tengah-kiri
    logo = Image.open(os.path.join(SRC, "logo.webp")).convert("RGBA")
    lh = 300
    lw = int(logo.width * lh / logo.height)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    ox, oy = 160, (H - lh) // 2
    # kertas putih belakang logo biar menonjol
    im.paste(logo, (ox, oy), logo)
    # teks kanan
    tx = ox + lw + 70
    d.text((tx, 190), "YO TARPAULIN", font=font(64), fill=(255, 255, 255))
    d.text((tx, 290), "Solusi Terpal Anda", font=font(40, False), fill=(255, 214, 0))
    d.text((tx, 400), "Produsen & Pemasok Terpal Nasional", font=font(28, False), fill=(214, 228, 252))
    d.text((tx, 450), "Hotline: +62 812-2133-2929   ·   yoterpal.com", font=font(28, False), fill=(214, 228, 252))
    im.save(dst, "JPEG", quality=Q, optimize=True, progressive=True)
    print(dst, os.path.getsize(dst))


brand_card(os.path.join(OUT, "og-default.jpg"))

MAP = {
    "og-produk.jpg": "banner-hero.webp",
    "og-tentang.jpg": "banner-struktur.webp",
    "og-galeri.jpg": "galeri-hero.webp",
    "og-keunggulan.jpg": "banner-kenapa.webp",
    "og-aplikasi.jpg": "app-equipment.webp",
    "og-terpal-biru-premium.jpg": "prod-biru-premium.webp",
    "og-terpal-navy.jpg": "prod-navy.webp",
    "og-terpal-kuning-gold.jpg": "prod-kuning.webp",
    "og-terpal-hijau.jpg": "prod-hijau.webp",
    "og-terpal-oranye.jpg": "prod-oranye.webp",
    "og-terpal-pvc-transparan.jpg": "prod-pvc.webp",
    "og-terpal-roll.jpg": "rolls-colorful.webp",
    "og-paranet-bangunan.jpg": "paranet-loom.webp",
    "og-terpal-biru-muda.jpg": "prod-biru-muda.webp",
    "og-tas-spunbond.jpg": "prod-tas-spunbond.webp",
}
for dst, src in MAP.items():
    cover(os.path.join(SRC, src), os.path.join(OUT, dst))
print("DONE")
