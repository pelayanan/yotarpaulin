#!/usr/bin/env python3
"""Rebuild og-default.jpg — latar putih, aksen biru & oranye, logo tidak tertutup."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
NAVY = (10, 49, 104)        # biru tua brand
ORANGE = (240, 101, 26)      # oranye aksen
SRC = "assets/images/logo.webp"
OUT = "assets/images/og/og-default.jpg"

def font(size, bold=True):
    p = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else \
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
    return ImageFont.truetype(p, size)

im = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(im)

# strip aksen: biru atas, oranye bawah
d.rectangle([0, 0, W, 14], fill=NAVY)
d.rectangle([0, H - 30, W, H], fill=ORANGE)
d.rectangle([0, H - 44, W, H - 30], fill=(255, 214, 0))

# panel logo: bidang putih dengan border biru — logo biru jelas terbaca
d.rounded_rectangle([90, 80, 620, 550], radius=24, fill=(244, 249, 255), outline=NAVY, width=5)
logo = Image.open(SRC).convert("RGBA")
lh = 330
lw = int(logo.width * lh / logo.height)
logo = logo.resize((lw, lh), Image.LANCZOS)
lx = 90 + (530 - lw) // 2
ly = 80 + (470 - lh) // 2
im.paste(logo, (lx, ly), logo)

# teks kanan — lebar diukur biar tidak kepotong tepi
tx = 650
f_title = font(64)
f_slogan = font(34)
f_sub0 = font(27, False)
f_sub1 = font(24, False)
f_hotline = font(28)

t1 = "YO TARPAULIN"
w1 = d.textlength(t1, font=f_title)
d.text((tx, 122), t1, font=f_title, fill=NAVY)

t2 = "SOLUSI TERPAL ANDA"
w2 = d.textlength(t2, font=f_slogan)
d.text((tx, 232), t2, font=f_slogan, fill=ORANGE)
d.rectangle([tx, 300, tx + min(w2, W - tx - 40), 306], fill=ORANGE)

t3 = "Produsen & Pemasok Terpal Nasional"
d.text((tx, 330), t3, font=f_sub0, fill=(70, 90, 120))
t4a = "Terpal PE & PVC · Paranet"
t4b = "Sarung Tangan Kerja"
d.text((tx, 372), t4a, font=f_sub1, fill=(70, 90, 120))
d.text((tx, 408), t4b, font=f_sub1, fill=(70, 90, 120))

# chip hotline oranye — lebar mengikuti teks, dipastikan muat
t5 = "WHATSAPP +62 812-2133-2929"
w5 = d.textlength(t5, font=f_hotline)
cw = int(w5) + 56
ch_top = 452
cw = min(cw, W - tx - 30)
d.rounded_rectangle([tx, ch_top, tx + cw, ch_top + 72], radius=14, fill=ORANGE)
d.text((tx + 28, ch_top + 16), t5, font=f_hotline, fill=(255, 255, 255))

d.text((tx, 546), "yoterpal.com", font=font(26, False), fill=(120, 140, 165))

im.save(OUT, "JPEG", quality=84, optimize=True, progressive=True)
print("saved", OUT, os.path.getsize(OUT))
