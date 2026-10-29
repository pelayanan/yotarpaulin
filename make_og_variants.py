#!/usr/bin/env python3
"""Buat 3 varian og-default (v1/v2/v3) — biru & oranye, nama CV. YO TERPAL NUSANTARA RAYA."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
NAVY = (10, 49, 104)
NAVY2 = (16, 68, 140)
ORANGE = (240, 101, 26)
GOLD = (255, 214, 0)
SRC = "assets/images/logo.webp"
OUTDIR = "assets/images/og"

def font(size, bold=True):
    p = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else \
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
    return ImageFont.truetype(p, size)

logo = Image.open(SRC).convert("RGBA")

def logo_h(h):
    im = logo.copy()
    w = int(im.width * h / im.height)
    return im.resize((w, h), Image.LANCZOS)

def chip(d, x, y, text, f, fill=ORANGE, fg=(255, 255, 255), pad=28, hgt=64):
    w = int(d.textlength(text, font=f)) + pad * 2
    d.rounded_rectangle([x, y, x + w, y + hgt], radius=12, fill=fill)
    d.text((x + pad, y + (hgt - (f.size + 6)) // 2), text, font=f, fill=fg)
    return w

# ============ V1 — latar putih, panel logo kiri, right text (evolusi desain lama) ============
im = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 14], fill=NAVY)
d.rectangle([0, H - 30, W, H], fill=ORANGE)
d.rectangle([0, H - 44, W, H - 30], fill=GOLD)
d.rounded_rectangle([90, 80, 620, 550], radius=24, fill=(244, 249, 255), outline=NAVY, width=5)
lg = logo_h(330)
im.paste(lg, (90 + (530 - lg.width) // 2, 80 + (470 - 330) // 2), lg)
tx = 650
d.text((tx, 110), "YO TARPAULIN", font=font(62), fill=NAVY)
d.text((tx, 205), "SOLUSI TERPAL ANDA", font=font(32), fill=ORANGE)
w2 = d.textlength("SOLUSI TERPAL ANDA", font=font(32))
d.rectangle([tx, 268, tx + min(w2, W - tx - 40), 274], fill=ORANGE)
d.text((tx, 296), "CV. YO TERPAL NUSANTARA RAYA", font=font(30), fill=NAVY2)
d.text((tx, 344), "Produsen & Pemasok Terpal Nasional", font=font(25, False), fill=(70, 90, 120))
d.text((tx, 380), "Terpal PE & PVC · Paranet", font=font(23, False), fill=(70, 90, 120))
chip(d, tx, 432, "WHATSAPP +62 822-13-8889", font(27))
d.text((tx, 546), "yoterpal.com", font=font(26, False), fill=(120, 140, 165))
im.save(f"{OUTDIR}/og-default-v1.jpg", "JPEG", quality=84, optimize=True, progressive=True)

# ============ V2 — full navy, logo panel putih, teks putih + aksen oranye ============
im = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 14], fill=ORANGE)
d.rectangle([0, H - 30, W, H], fill=ORANGE)
d.rectangle([0, H - 36, W, H - 30], fill=GOLD)
# garis diagonal halus dekoratif pojok kanan-bawah (bebas dari zona teks)
for i in range(5):
    x0 = 1035 + i * 30
    d.line([x0, H, x0 + 70, H - 160], fill=(255, 255, 255), width=2)
d.rounded_rectangle([80, 80, 560, 550], radius=24, fill=(255, 255, 255))
lg = logo_h(340)
im.paste(lg, (80 + (480 - lg.width) // 2, 80 + (470 - 340) // 2), lg)
tx = 620
d.text((tx, 108), "YO TARPAULIN", font=font(62), fill=(255, 255, 255))
d.text((tx, 202), "SOLUSI TERPAL ANDA", font=font(32), fill=ORANGE)
d.text((tx, 296), "CV. YO TERPAL NUSANTARA RAYA", font=font(30), fill=GOLD)
d.text((tx, 356), "Produsen & Pemasok Terpal Nasional", font=font(25, False), fill=(214, 226, 244))
d.text((tx, 392), "Terpal PE & PVC · Paranet", font=font(23, False), fill=(214, 226, 244))
chip(d, tx, 448, "WHATSAPP +62 822-13-8889", font(27), fill=ORANGE)
d.text((tx, 546), "yoterpal.com", font=font(26, False), fill=(178, 196, 222))
im.save(f"{OUTDIR}/og-default-v2.jpg", "JPEG", quality=84, optimize=True, progressive=True)

# ============ V3 — center: biru atas / putih bawah, logo tengah, banner split ============
im = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 300], fill=NAVY)
d.rectangle([0, 292, W, 308], fill=ORANGE)
d.rectangle([0, 0, W, 14], fill=ORANGE)
d.rectangle([0, H - 26, W, H], fill=NAVY)
# logo besar di bidang split (putih kotak di atas strip)
lg = logo_h(280)
lx = (W - lg.width) // 2
ly = 300 - 280 // 2 - 40
d.rectangle([lx - 36, ly - 30, lx + lg.width + 36, ly + lg.height + 30], fill=(255, 255, 255))
im.paste(lg, (lx, ly), lg)
def center_text(d, y, text, f, fill, sep_gap=None):
    w = int(d.textlength(text, font=f))
    d.text(((W - w) // 2, y), text, font=f, fill=fill)
    return w

f_v3t = font(66)
f_v3s = font(24, False)
f_v3c = font(28)
center_text(d, 356, "YO TARPAULIN", f_v3t, NAVY)
center_text(d, 440, "SOLUSI TERPAL ANDA  ·  PRODUSEN & PEMASOK TERPAL NASIONAL", f_v3s, (70, 90, 120))
center_text(d, 478, "CV. YO TERPAL NUSANTARA RAYA", f_v3c, ORANGE)
f_hl = font(26)
t5 = "WHATSAPP +62 822-13-8889   ·   yoterpal.com"
w5 = int(d.textlength(t5, font=f_hl))
chip(d, (W - w5) // 2, 528, t5, f_hl, hgt=56, pad=30)
im.save(f"{OUTDIR}/og-default-v3.jpg", "JPEG", quality=84, optimize=True, progressive=True)

for v in ("v1", "v2", "v3"):
    p = f"{OUTDIR}/og-default-{v}.jpg"
    print("saved", p, os.path.getsize(p))
