"""Generate 10 badge design variations for the 'I am a Copilot Agent Builder' signature badge."""
import math
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT_DIR = r"C:\Dev\FOI_Webinar\assets\img\badge-designs"
os.makedirs(OUT_DIR, exist_ok=True)

# Brand palette
BLUE = (31, 78, 216)
BLUE_DARK = (15, 47, 150)
INK = (15, 30, 70)
CREAM = (253, 233, 176)
GOLD = (210, 165, 50)
GOLD_HI = (245, 213, 110)
MINT = (201, 239, 210)
ICE = (224, 235, 252)
WHITE = (255, 255, 255)

FONT_BOLD = [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf"]
FONT_BLACK = [r"C:\Windows\Fonts\seguibl.ttf", r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf"]
FONT_REG = [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"]
FONT_MONO = [r"C:\Windows\Fonts\consola.ttf", r"C:\Windows\Fonts\consolab.ttf"]


def fnt(paths, size):
    for f in paths:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def sparkle(d, cx, cy, r_long, r_short, color, rot=0):
    """Four-point Copilot-style sparkle."""
    pts = []
    for i in range(8):
        a = math.radians(rot + i * 45)
        rr = r_long if i % 2 == 0 else r_short
        pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    d.polygon(pts, fill=color)


# Copilot brand rainbow gradient stops (cyan -> blue -> purple -> pink -> orange)
COPILOT_GRADIENT = [
    (0.00, (45, 217, 193)),   # cyan / teal
    (0.25, (32, 101, 242)),   # blue
    (0.50, (107, 43, 229)),   # purple
    (0.75, (232, 30, 151)),   # magenta / pink
    (1.00, (248, 155, 58)),   # orange
]


def gradient_at(stops, t):
    """Sample an N-stop gradient at position t in [0,1]; returns (r,g,b)."""
    if t <= stops[0][0]:
        return stops[0][1]
    if t >= stops[-1][0]:
        return stops[-1][1]
    for i in range(len(stops) - 1):
        p1, c1 = stops[i]
        p2, c2 = stops[i + 1]
        if p1 <= t <= p2:
            local = (t - p1) / (p2 - p1) if p2 > p1 else 0
            return (int(c1[0] * (1 - local) + c2[0] * local),
                    int(c1[1] * (1 - local) + c2[1] * local),
                    int(c1[2] * (1 - local) + c2[2] * local))
    return stops[-1][1]


def copilot_logo(height):
    """Load and resize the Copilot color logo to a given height (px)."""
    src = r"C:\Dev\FOI_Webinar\assets\img\copilot-color.png"
    logo = Image.open(src).convert("RGBA")
    w = int(logo.width * height / logo.height)
    return logo.resize((w, height), Image.LANCZOS)


def save(im, name):
    p = os.path.join(OUT_DIR, name)
    im.save(p, optimize=True)
    print("saved", p, im.size)


# ---------- 1. Rosette Pill (refined version of current) ----------
def design_01_rosette_pill():
    W, H = 1600, 480
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # shadow
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([24, 36, W - 24, H - 12], radius=180, fill=(15, 30, 70, 90))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    im.alpha_composite(shadow)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([16, 16, W - 16, H - 28], radius=180, fill=WHITE)
    d.rounded_rectangle([16, 16, W - 16, H - 28], radius=180, outline=BLUE, width=3)
    cx, cy = 230, H // 2 - 6
    outer_r, inner_r = 150, 105
    # ribbons
    d.polygon([(cx - 50, cy + 70), (cx - 12, cy + 70), (cx - 30, cy + 200),
               (cx - 80, cy + 170), (cx - 55, cy + 135)], fill=BLUE_DARK)
    d.polygon([(cx + 12, cy + 70), (cx + 50, cy + 70), (cx + 55, cy + 135),
               (cx + 80, cy + 170), (cx + 30, cy + 200)], fill=BLUE_DARK)
    # pleated teeth
    teeth = 16
    for i in range(teeth):
        a0 = (i / teeth) * 2 * math.pi
        a1 = ((i + 1) / teeth) * 2 * math.pi
        mid = (a0 + a1) / 2
        po = (cx + math.cos(mid) * (outer_r + 16), cy + math.sin(mid) * (outer_r + 16))
        pa = (cx + math.cos(a0) * (outer_r - 6), cy + math.sin(a0) * (outer_r - 6))
        pb = (cx + math.cos(a1) * (outer_r - 6), cy + math.sin(a1) * (outer_r - 6))
        d.polygon([pa, po, pb], fill=BLUE)
    d.ellipse([cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r], fill=BLUE)
    d.ellipse([cx - outer_r + 8, cy - outer_r + 8, cx + outer_r - 8, cy + outer_r - 8], fill=(247, 250, 255))
    d.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r], fill=CREAM)
    d.ellipse([cx - inner_r + 5, cy - inner_r + 5, cx + inner_r - 5, cy + inner_r - 5], outline=BLUE, width=3)
    sparkle(d, cx, cy, 70, 18, BLUE_DARK)
    sparkle(d, cx + 55, cy - 50, 22, 6, BLUE_DARK)
    sparkle(d, cx - 50, cy + 55, 18, 5, BLUE_DARK)
    # text
    d.text((470, cy - 150), "I  A M  A", font=fnt(FONT_BOLD, 38), fill=BLUE)
    d.text((470, cy - 100), "Copilot", font=fnt(FONT_BLACK, 108), fill=INK)
    d.text((470, cy + 20), "Agent Builder", font=fnt(FONT_BOLD, 64), fill=BLUE)
    save(im, "badge-01-rosette-pill.png")


# ---------- 2. Round Medallion ----------
def design_02_round_medallion():
    S = 900
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    # shadow
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    sdr = ImageDraw.Draw(sh)
    sdr.ellipse([30, 50, S - 30, S - 10], fill=(15, 30, 70, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    cx, cy = S // 2, S // 2
    # outer ring
    d.ellipse([20, 20, S - 20, S - 20], fill=BLUE)
    d.ellipse([55, 55, S - 55, S - 55], fill=WHITE)
    d.ellipse([55, 55, S - 55, S - 55], outline=BLUE, width=3)
    # inner ring
    d.ellipse([85, 85, S - 85, S - 85], outline=BLUE, width=2)
    # sparkle top
    sparkle(d, cx, cy - 200, 50, 14, BLUE)
    sparkle(d, cx - 70, cy - 170, 18, 5, BLUE)
    sparkle(d, cx + 70, cy - 170, 18, 5, BLUE)
    # text
    title_font = fnt(FONT_BLACK, 78)
    sub_font = fnt(FONT_BOLD, 50)
    eb_font = fnt(FONT_BOLD, 32)
    eb = "I  A M  A"
    tb = d.textbbox((0, 0), eb, font=eb_font)
    d.text((cx - (tb[2] - tb[0]) // 2, cy - 80), eb, font=eb_font, fill=BLUE)
    t1 = "Copilot"
    tb1 = d.textbbox((0, 0), t1, font=title_font)
    d.text((cx - (tb1[2] - tb1[0]) // 2, cy - 30), t1, font=title_font, fill=INK)
    t2 = "Agent Builder"
    tb2 = d.textbbox((0, 0), t2, font=sub_font)
    d.text((cx - (tb2[2] - tb2[0]) // 2, cy + 60), t2, font=sub_font, fill=BLUE)
    # arc text dots at bottom
    for i in range(7):
        a = math.radians(70 + i * 7)
        x = cx + math.cos(a) * 320
        y = cy + math.sin(a) * 320
        d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=BLUE)
    save(im, "badge-02-round-medallion.png")


# ---------- 3. Shield / Crest ----------
def design_03_shield():
    W, H = 800, 960
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # shadow
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdr = ImageDraw.Draw(sh)
    pts = [(80, 80), (W - 80, 80), (W - 80, 600), (W // 2, H - 40), (80, 600)]
    sdr.polygon([(x + 8, y + 16) for x, y in pts], fill=(15, 30, 70, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(20))
    im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    # shield body
    d.polygon(pts, fill=BLUE)
    # inner shield
    inner = [(115, 110), (W - 115, 110), (W - 115, 590), (W // 2, H - 90), (115, 590)]
    d.polygon(inner, fill=WHITE)
    d.polygon(inner, outline=BLUE, width=4)
    # ribbon banner across the top
    ribbon = [(40, 220), (W - 40, 220), (W - 90, 290), (W - 40, 360), (40, 360), (90, 290)]
    d.polygon(ribbon, fill=BLUE_DARK)
    d.text((W // 2 - 110, 250), "CERTIFIED", font=fnt(FONT_BLACK, 48), fill=WHITE)
    # sparkle in centre
    cx, cy = W // 2, 510
    sparkle(d, cx, cy, 80, 22, BLUE)
    sparkle(d, cx - 95, cy - 55, 22, 6, BLUE)
    sparkle(d, cx + 95, cy - 55, 22, 6, BLUE)
    # text
    f1 = fnt(FONT_BLACK, 64)
    f2 = fnt(FONT_BOLD, 44)
    tb = d.textbbox((0, 0), "Copilot", font=f1)
    d.text((W // 2 - (tb[2] - tb[0]) // 2, cy + 80), "Copilot", font=f1, fill=INK)
    tb = d.textbbox((0, 0), "Agent Builder", font=f2)
    d.text((W // 2 - (tb[2] - tb[0]) // 2, cy + 160), "Agent Builder", font=f2, fill=BLUE)
    save(im, "badge-03-shield.png")


# ---------- 4. Hexagonal tech badge ----------
def design_04_hex():
    W, H = 900, 780
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cx, cy = W // 2, H // 2
    r = 360
    pts = [(cx + math.cos(math.radians(60 * i - 30)) * r,
            cy + math.sin(math.radians(60 * i - 30)) * r) for i in range(6)]
    # shadow
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdr = ImageDraw.Draw(sh)
    sdr.polygon([(x + 8, y + 16) for x, y in pts], fill=(15, 30, 70, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    # outer hex
    d.polygon(pts, fill=BLUE)
    # inner hex
    r2 = r - 30
    pts2 = [(cx + math.cos(math.radians(60 * i - 30)) * r2,
             cy + math.sin(math.radians(60 * i - 30)) * r2) for i in range(6)]
    d.polygon(pts2, fill=WHITE)
    r3 = r - 50
    pts3 = [(cx + math.cos(math.radians(60 * i - 30)) * r3,
             cy + math.sin(math.radians(60 * i - 30)) * r3) for i in range(6)]
    d.polygon(pts3, outline=BLUE, width=3)
    # sparkle
    sparkle(d, cx, cy - 130, 56, 16, BLUE)
    sparkle(d, cx + 65, cy - 80, 18, 5, BLUE)
    sparkle(d, cx - 65, cy - 80, 18, 5, BLUE)
    # text
    eb = fnt(FONT_MONO, 26)
    d.text((cx - 78, cy - 5), "// I AM A", font=eb, fill=BLUE)
    f1 = fnt(FONT_BLACK, 72)
    tb = d.textbbox((0, 0), "Copilot", font=f1)
    d.text((cx - (tb[2] - tb[0]) // 2, cy + 40), "Copilot", font=f1, fill=INK)
    f2 = fnt(FONT_BOLD, 46)
    tb = d.textbbox((0, 0), "Agent Builder", font=f2)
    d.text((cx - (tb[2] - tb[0]) // 2, cy + 130), "Agent Builder", font=f2, fill=BLUE)
    save(im, "badge-04-hex.png")


# ---------- 5. Sun-burst rays ----------
def design_05_sunburst():
    W, H = 1600, 480
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # rays radiating from left-centre
    cx, cy = 230, H // 2
    R = 720
    for i in range(36):
        a0 = math.radians(i * 10 - 2.5)
        a1 = math.radians(i * 10 + 2.5)
        p1 = (cx + math.cos(a0) * 180, cy + math.sin(a0) * 180)
        p2 = (cx + math.cos(a0) * R, cy + math.sin(a0) * R)
        p3 = (cx + math.cos(a1) * R, cy + math.sin(a1) * R)
        p4 = (cx + math.cos(a1) * 180, cy + math.sin(a1) * 180)
        col = (224, 235, 252, 255) if i % 2 == 0 else (200, 220, 250, 255)
        d.polygon([p1, p2, p3, p4], fill=col)
    # central disc
    d.ellipse([cx - 180, cy - 180, cx + 180, cy + 180], fill=BLUE)
    d.ellipse([cx - 160, cy - 160, cx + 160, cy + 160], fill=WHITE)
    d.ellipse([cx - 160, cy - 160, cx + 160, cy + 160], outline=BLUE, width=3)
    sparkle(d, cx, cy, 86, 22, BLUE)
    sparkle(d, cx + 70, cy - 70, 22, 6, BLUE)
    sparkle(d, cx - 70, cy + 70, 22, 6, BLUE)
    # text horizontal band
    d.rectangle([520, cy - 120, W - 60, cy + 120], fill=WHITE)
    d.rectangle([520, cy - 120, W - 60, cy + 120], outline=BLUE, width=3)
    d.text((550, cy - 110), "I  A M  A", font=fnt(FONT_BOLD, 32), fill=BLUE)
    d.text((550, cy - 70), "Copilot", font=fnt(FONT_BLACK, 96), fill=INK)
    d.text((550, cy + 40), "Agent Builder", font=fnt(FONT_BOLD, 56), fill=BLUE)
    save(im, "badge-05-sunburst.png")


# ---------- 6. Ribbon banner ----------
def design_06_ribbon():
    W, H = 1600, 380
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # ribbon shape
    pts = [
        (40, 90), (W - 200, 90),
        (W - 90, H // 2), (W - 200, H - 90),
        (40, H - 90), (150, H // 2)
    ]
    # shadow
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdr = ImageDraw.Draw(sh)
    sdr.polygon([(x + 6, y + 14) for x, y in pts], fill=(15, 30, 70, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    d.polygon(pts, fill=BLUE)
    # inner stripe
    inner_pts = [
        (60, 110), (W - 220, 110),
        (W - 115, H // 2), (W - 220, H - 110),
        (60, H - 110), (170, H // 2)
    ]
    d.polygon(inner_pts, outline=(255, 255, 255, 180), width=3)
    # sparkle on left
    sparkle(d, 230, H // 2, 64, 18, WHITE)
    sparkle(d, 300, H // 2 - 60, 20, 6, WHITE)
    sparkle(d, 300, H // 2 + 60, 20, 6, WHITE)
    # text
    eb = fnt(FONT_BOLD, 34)
    f1 = fnt(FONT_BLACK, 96)
    d.text((430, H // 2 - 100), "I  A M  A", font=eb, fill=(220, 230, 255))
    d.text((430, H // 2 - 60), "Copilot Agent Builder", font=f1, fill=WHITE)
    save(im, "badge-06-ribbon.png")


# ---------- 7. Certified square (Microsoft-style) ----------
def design_07_certified_square():
    S = 900
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # shadow
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    sdr = ImageDraw.Draw(sh)
    sdr.rounded_rectangle([30, 50, S - 30, S - 10], radius=40, fill=(15, 30, 70, 100))
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    # outer card
    d.rounded_rectangle([30, 30, S - 30, S - 30], radius=40, fill=WHITE)
    d.rounded_rectangle([30, 30, S - 30, S - 30], radius=40, outline=BLUE, width=4)
    # top blue band
    d.rectangle([30, 30, S - 30, 200], fill=BLUE)
    # round corners patch on band
    d.rounded_rectangle([30, 30, S - 30, 240], radius=40, fill=BLUE)
    d.rectangle([30, 180, S - 30, 240], fill=BLUE)
    d.text((S // 2 - 130, 80), "CERTIFIED", font=fnt(FONT_BLACK, 48), fill=WHITE)
    # sparkle large
    sparkle(d, S // 2, 380, 70, 20, BLUE)
    sparkle(d, S // 2 - 80, 330, 20, 6, BLUE)
    sparkle(d, S // 2 + 80, 330, 20, 6, BLUE)
    # text
    f0 = fnt(FONT_BOLD, 30)
    tb = d.textbbox((0, 0), "I AM A", font=f0)
    d.text((S // 2 - (tb[2] - tb[0]) // 2, 490), "I AM A", font=f0, fill=BLUE)
    f1 = fnt(FONT_BLACK, 76)
    tb = d.textbbox((0, 0), "Copilot", font=f1)
    d.text((S // 2 - (tb[2] - tb[0]) // 2, 540), "Copilot", font=f1, fill=INK)
    f2 = fnt(FONT_BOLD, 50)
    tb = d.textbbox((0, 0), "Agent Builder", font=f2)
    d.text((S // 2 - (tb[2] - tb[0]) // 2, 640), "Agent Builder", font=f2, fill=BLUE)
    # rule + year
    d.line([(180, 740), (S - 180, 740)], fill=BLUE, width=2)
    f3 = fnt(FONT_BOLD, 28)
    tb = d.textbbox((0, 0), "2026", font=f3)
    d.text((S // 2 - (tb[2] - tb[0]) // 2, 760), "2026", font=f3, fill=BLUE)
    save(im, "badge-07-certified-square.png")


# ---------- 8. Minimal wordmark ----------
def design_08_minimal():
    W, H = 1600, 360
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # subtle background pill - very light
    d.rounded_rectangle([20, 60, W - 20, H - 40], radius=160, fill=(247, 250, 255, 255))
    d.rounded_rectangle([20, 60, W - 20, H - 40], radius=160, outline=BLUE, width=2)
    # left sparkle, slightly larger
    cx, cy = 160, H // 2
    sparkle(d, cx, cy, 60, 16, BLUE)
    sparkle(d, cx + 55, cy - 50, 18, 5, BLUE)
    sparkle(d, cx - 50, cy + 55, 18, 5, BLUE)
    # text: eyebrow + headline horizontal
    eb = fnt(FONT_BOLD, 34)
    d.text((280, cy - 80), "I AM A", font=eb, fill=BLUE)
    f1 = fnt(FONT_BLACK, 84)
    d.text((280, cy - 40), "Copilot Agent Builder", font=f1, fill=INK)
    save(im, "badge-08-minimal.png")


# ---------- 9. Copilot rainbow gradient pill ----------
def design_09_gradient_pill():
    W, H = 1600, 420
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # Build horizontal Copilot rainbow gradient
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(g)
    for x in range(W):
        col = gradient_at(COPILOT_GRADIENT, x / W)
        gd.line([(x, 0), (x, H)], fill=col + (255,))
    # Mask to rounded pill
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([30, 30, W - 30, H - 30], radius=180, fill=255)
    im.paste(g, (0, 0), mask)
    # Soft shadow under
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdr = ImageDraw.Draw(sh)
    sdr.rounded_rectangle([40, 50, W - 40, H - 10], radius=180, fill=(15, 30, 70, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out.alpha_composite(sh)
    out.alpha_composite(im)
    d = ImageDraw.Draw(out)
    # Copilot logo on the left
    logo = copilot_logo(220)
    logo_x = 90
    logo_y = (H - 220) // 2
    out.alpha_composite(logo, (logo_x, logo_y))
    # Text — single line: "I am a Copilot Agent Builder"
    d = ImageDraw.Draw(out)
    text_x = logo_x + logo.width + 50
    cy = H // 2
    text = "I am a Copilot Agent Builder"
    # Auto-fit: shrink size until the text fits the available width
    avail = (W - 90) - text_x
    size = 92
    while size > 36:
        f = fnt(FONT_BLACK, size)
        tb = d.textbbox((0, 0), text, font=f)
        tw, th = tb[2] - tb[0], tb[3] - tb[1]
        if tw <= avail:
            break
        size -= 2
    f = fnt(FONT_BLACK, size)
    tb = d.textbbox((0, 0), text, font=f)
    th = tb[3] - tb[1]
    d.text((text_x, cy - th // 2 - tb[1]), text, font=f, fill=WHITE)
    save(out, "badge-09-gradient-pill.png")


# ---------- 10. Coin / Medal with Copilot rainbow ring ----------
def design_10_coin():
    S = 900
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    # Soft drop shadow
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    sdr = ImageDraw.Draw(sh)
    sdr.ellipse([30, 50, S - 30, S - 10], fill=(15, 30, 70, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    cx, cy = S // 2, S // 2
    R = (S - 60) // 2

    # Copilot rainbow ring via angular wedges
    steps = 360
    for i in range(steps):
        t = i / steps
        col = gradient_at(COPILOT_GRADIENT, t) + (255,)
        # Pie-slice from the centre — we'll cut out the inner disc later
        d.pieslice([cx - R, cy - R, cx + R, cy + R],
                   i - 90 - 1, i - 90 + 2, fill=col)

    # Inner navy disc (covers the centre of the pieslices, leaving the rainbow ring)
    inner = R - 80
    d.ellipse([cx - inner, cy - inner, cx + inner, cy + inner], fill=INK)
    # subtle inner highlight outline (slightly desaturated white)
    d.ellipse([cx - inner, cy - inner, cx + inner, cy + inner],
              outline=(255, 255, 255, 60), width=3)

    # Copilot logo at the top of the navy face
    logo = copilot_logo(180)
    logo_x = cx - logo.width // 2
    logo_y = cy - 270
    im.alpha_composite(logo, (logo_x, logo_y))

    # text under logo
    d = ImageDraw.Draw(im)
    eb = fnt(FONT_BOLD, 40)
    tb = d.textbbox((0, 0), "I AM A", font=eb)
    d.text((cx - (tb[2] - tb[0]) // 2, cy - 60), "I AM A", font=eb, fill=GOLD_HI)
    f1 = fnt(FONT_BLACK, 102)
    tb = d.textbbox((0, 0), "Copilot", font=f1)
    d.text((cx - (tb[2] - tb[0]) // 2, cy - 10), "Copilot", font=f1, fill=WHITE)
    f2 = fnt(FONT_BOLD, 60)
    tb = d.textbbox((0, 0), "Agent Builder", font=f2)
    d.text((cx - (tb[2] - tb[0]) // 2, cy + 115), "Agent Builder", font=f2, fill=GOLD_HI)
    save(im, "badge-10-coin.png")


for f in (design_01_rosette_pill, design_02_round_medallion, design_03_shield,
          design_04_hex, design_05_sunburst, design_06_ribbon,
          design_07_certified_square, design_08_minimal,
          design_09_gradient_pill, design_10_coin):
    f()

print("done")
