"""ONC-001 - montagem por camadas (etapa 8).  Python + ffmpeg, local e gratis."""
import json, math, os, shutil, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

V = sys.argv[1]
W, H, FPS = 1080, 1920, 30
A = os.path.join(V, "assets")
TMP = os.path.join(V, "_render")
BG = os.path.join(TMP, "bg")
OUTF = os.path.join(TMP, "out")
for d in (BG, OUTF):
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)

TL = json.load(open(os.path.join(V, "audio", "_timeline.json"), encoding="utf-8"))
FR = {f["n"]: f for f in TL["frases"]}
TOTAL = TL["total"]
NFRAMES = int(round(TOTAL * FPS))

F = "C:/Windows/Fonts/"
def font(name, size):
    return ImageFont.truetype(F + name, size)
CAP = font("ariblk.ttf", 66)       # legenda
CAPS = font("ariblk.ttf", 54)
BIG = font("impact.ttf", 230)      # numeros gigantes
TAG = font("ariblk.ttf", 52)       # rotulos
OM = font("ariblk.ttf", 46)        # oncometro
HOOK = font("impact.ttf", 118)     # texto-gancho

# ---------------------------------------------------------------- cenas
SC = [
    dict(n=1, ini=0.00, fim=2.58, kind="hook",    bg=("vid", "px-jungle_leaves-183638.mp4", 1.0)),
    dict(n=2, ini=2.61, fim=5.05, kind="label",   bg=("vid", "px-jungle_leaves-183638.mp4", 4.0)),
    dict(n=3, ini=5.05, fim=7.48, kind="thermal", bg=("vid", "px-forest_night-11721.mp4", 2.0)),
    dict(n=4, ini=7.51, fim=10.35, kind="venom",  bg=("vid", "px-rainforest_floor-23.mp4", 1.0)),
    dict(n=5, ini=10.37, fim=12.60, kind="year",  bg=("img", "px-pills_medicine-1539191.jpg", 0)),
    dict(n=6, ini=12.60, fim=14.75, kind="press", bg=("img", "px-blood_pressure_monitor-1584223.jpg", 0)),
    dict(n=7, ini=14.77, fim=17.96, kind="split", bg=("vid", "px-rainforest_floor-23.mp4", 5.0)),
    dict(n=8, ini=17.99, fim=22.88, kind="meter", bg=("grad", None, 0)),
    dict(n=9, ini=22.90, fim=26.52, kind="close", bg=("vid", "px-jungle_leaves-183638.mp4", 7.0)),
]
for s in SC:
    s["f0"] = int(round(s["ini"] * FPS))
    s["f1"] = int(round(s["fim"] * FPS))

# ------------------------------------------------- fundos: extrai com ffmpeg
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        print("ffmpeg erro:", " ".join(c)[:160], r.stderr[-400:]); sys.exit(1)

for s in SC:
    kind, src, off = s["bg"]
    n = s["f1"] - s["f0"] + 2
    d = os.path.join(BG, f"s{s['n']}")
    os.makedirs(d, exist_ok=True)
    if kind == "vid":
        vf = ("scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
              "eq=brightness=-0.16:saturation=0.75,gblur=sigma=5")
        run(["ffmpeg", "-y", "-v", "error", "-stream_loop", "3", "-ss", str(off),
             "-i", os.path.join(A, src), "-vf", vf, "-r", str(FPS), "-frames:v", str(n),
             "-q:v", "3", os.path.join(d, "%04d.jpg")])
    elif kind == "img":
        im = Image.open(os.path.join(A, src)).convert("RGB")
        for i in range(n):          # Ken Burns em PIL
            z = 1.0 + 0.10 * i / max(1, n - 1)
            cw, ch = int(im.width / z), int(im.height / z)
            x = (im.width - cw) // 2; y = (im.height - ch) // 2
            c = im.crop((x, y, x + cw, y + ch))
            r = min(W / c.width, H / c.height)
            c = c.resize((max(W, int(c.width * r * 1.02)), max(H, int(c.height * r * 1.02))), Image.LANCZOS)
            cx = (c.width - W) // 2; cy = (c.height - H) // 2
            c = c.crop((cx, cy, cx + W, cy + H))
            c = ImageEnhance.Brightness(c).enhance(0.62)
            c.filter(ImageFilter.GaussianBlur(2)).save(os.path.join(d, f"{i+1:04d}.jpg"), quality=88)
    else:                            # gradiente escuro
        g = Image.new("RGB", (W, H))
        dr = ImageDraw.Draw(g)
        for y in range(H):
            t = y / H
            dr.line([(0, y), (W, y)], fill=(int(14 + 26 * t), int(10 + 16 * t), int(8 + 10 * t)))
        for i in range(n):
            g.save(os.path.join(d, f"{i+1:04d}.jpg"), quality=88)
print("fundos extraidos")

# ------------------------------------------------------------- recortes
def load(p):
    return Image.open(os.path.join(A, p)).convert("RGBA")

HEAD = load("inat-348275825-recorte.png")     # perfil, olhar p/ esquerda
HEAD2 = load("inat-348275850-recorte.png")
COIL = load("inat-348275890-recorte.png")
HEAD3 = load("inat-348275873-recorte.png")
COILC = COIL.crop(COIL.getbbox())
HEADC = HEAD2.crop(HEAD2.getbbox())
PILL = Image.open(os.path.join(A, "px-pills_medicine-8287535.jpg")).convert("RGB")

PIT = (610, 310)      # fosseta loreal no recorte 1400x933
EYE = (790, 265)

def fit(im, w):
    r = w / im.width
    return im.resize((w, int(im.height * r)), Image.LANCZOS)

def ironbow(im):
    """falsa-cor termica a partir da luminancia"""
    g = im.convert("L")
    stops = [(0, (6, 0, 38)), (60, (108, 0, 120)), (120, (210, 60, 40)),
             (180, (255, 160, 20)), (230, (255, 240, 140)), (255, (255, 255, 255))]
    lut = []
    for v in range(256):
        for i in range(len(stops) - 1):
            a, ca = stops[i]; b, cb = stops[i + 1]
            if a <= v <= b:
                t = (v - a) / (b - a)
                lut.append(tuple(int(ca[k] + (cb[k] - ca[k]) * t) for k in range(3))); break
    out = Image.new("RGB", g.size)
    out.putdata([lut[p] for p in g.getdata()])
    out = out.convert("RGBA"); out.putalpha(im.getchannel("A"))
    return out

THERM = ironbow(HEAD2)

# ------------------------------------------------------------- texto
def outlined(d, xy, txt, f, fill=(255, 255, 255), stroke=(0, 0, 0), w=7, anchor="mm"):
    d.text(xy, txt, font=f, fill=fill, stroke_width=w, stroke_fill=stroke, anchor=anchor)

def words_of(n):
    """tempos palavra a palavra, proporcionais ao tamanho da palavra"""
    fr = FR[n]; ws = fr["texto"].split()
    tot = sum(len(w) + 1 for w in ws)
    out, t = [], fr["ini"]
    for w in ws:
        d = fr["dur"] * (len(w) + 1) / tot
        out.append((w, t, t + d)); t += d
    return out

WORDS = {n: words_of(n) for n in FR}
SC_FRASE = {1: 1, 2: 2, 3: 2, 4: 3, 5: 4, 6: 4, 7: 5, 8: 6, 9: 7}

def draw_caption(img, t, sc):
    """legenda palavra por palavra no topo, dentro da area segura"""
    n = SC_FRASE[sc["n"]]
    cur = [w for w in WORDS[n] if w[1] <= t < w[2]]
    if not cur:
        return
    word = cur[0][0].upper().strip(":,.!")
    d = ImageDraw.Draw(img)
    f = CAP if len(word) <= 11 else CAPS
    bb = d.textbbox((W // 2, 300), word, font=f, anchor="mm", stroke_width=8)
    pad = 26
    box = Image.new("RGBA", (bb[2] - bb[0] + pad * 2, bb[3] - bb[1] + pad), (0, 0, 0, 155))
    img.alpha_composite(box, (bb[0] - pad, bb[1] - pad // 2))
    outlined(d, (W // 2, 300), word, f, w=8)

# ------------------------------------------------------------- cenas
def scene_hook(img, p, t):
    d = ImageDraw.Draw(img)
    z = 1.0 + 0.055 * math.sin(p * math.pi)            # zoom de impacto
    sn = fit(HEAD, int(1180 * z))
    sc = sn.width / HEAD.width
    ox, oy = (W - sn.width) // 2, 760 - int(40 * p)
    img.alpha_composite(sn, (ox, oy))
    px, py = ox + int(PIT[0] * sc), oy + int(PIT[1] * sc)
    r = int((62 + 16 * math.sin(p * 13)) * sc)          # circulo pulsando
    for k, wd in ((0, 9), (10, 5)):
        d.ellipse([px - r - k, py - r - k, px + r + k, py + r + k],
                  outline=(255, 40, 40, 255), width=wd)
    d.line([(px - r - 160, py - 150), (px - r - 20, py - 20)], fill=(255, 40, 40), width=9)
    if True:
        outlined(d, (W // 2, 1585), "ESSE BURACO", HOOK, (255, 232, 60), w=10)
        outlined(d, (W // 2, 1700), "VÊ CALOR", HOOK, (255, 232, 60), w=10)

def cartoon_eye(d, cx, cy, rx, ry, blink):
    if blink:
        d.line([(cx - rx, cy), (cx + rx, cy)], fill=(12, 10, 8), width=max(8, ry // 3))
        return
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(255, 255, 255), outline=(12, 10, 8), width=8)
    d.ellipse([cx - rx // 3, cy - ry // 2, cx + rx // 2, cy + ry], fill=(12, 10, 8))
    d.ellipse([cx - rx // 4, cy - ry // 3, cx + rx // 12, cy], fill=(255, 255, 255))

def scene_label(img, p, t):
    d = ImageDraw.Draw(img)
    sn = fit(HEAD2, 1150); sc = sn.width / HEAD2.width
    ox, oy = (W - sn.width) // 2, 800
    img.alpha_composite(sn, (ox, oy))
    ex, ey = ox + int(EYE[0] * sc), oy + int(EYE[1] * sc)
    blink = (t * 1000 % 2600) < 150                      # pisca
    cartoon_eye(d, ex, ey, int(78 * sc), int(66 * sc), blink)
    px, py = ox + int(PIT[0] * sc), oy + int(PIT[1] * sc)
    d.ellipse([px - 52, py - 52, px + 52, py + 52], outline=(255, 215, 0), width=8)
    slide = int(420 * max(0.0, 1 - p * 4))               # rotulo entra deslizando
    lx = 120 - slide
    d.line([(px - 40, py + 40), (lx + 330, 1560)], fill=(255, 215, 0), width=7)
    d.rounded_rectangle([lx, 1500, lx + 700, 1600], 18, fill=(255, 215, 0))
    d.text((lx + 350, 1550), "FOSSETA LOREAL", font=TAG, fill=(20, 16, 10), anchor="mm")

def scene_thermal(img, p, t):
    d = ImageDraw.Draw(img)
    sn = fit(THERM, 1150)
    img.alpha_composite(sn, ((W - sn.width) // 2, 790))
    y = int(480 + (1500 - 480) * ((t * 0.9) % 1.0))      # varredura
    d.line([(0, y), (W, y)], fill=(120, 255, 210, 180), width=5)
    for yy in range(480, 1500, 7):
        d.line([(0, yy), (W, yy)], fill=(0, 0, 0, 60), width=1)
    d.rounded_rectangle([150, 1520, 930, 1625], 18, fill=(10, 220, 180))
    d.text((540, 1572), "CÂMERA TÉRMICA", font=TAG, fill=(6, 30, 26), anchor="mm")

def scene_venom(img, p, t):
    d = ImageDraw.Draw(img)
    sn = fit(HEADC, 1240)
    ent = min(1.0, p * 2.6)
    ease = 1 - (1 - ent) ** 3
    x = int((W - sn.width) // 2 - (1 - ease) * 1150)
    bob = int(16 * math.sin(t * 7))                      # balanco de passo
    img.alpha_composite(sn, (x, 880 + bob))
    if p > 0.45:
        k = (p - 0.45) / 0.55
        sh = int(16 * math.sin(k * 40) * (1 - k))        # tremida
        outlined(d, (W // 2 + sh, 1600), "VENENO", BIG, (235, 40, 40), w=12)

def scene_year(img, p, t):
    d = ImageDraw.Draw(img)
    k = min(1.0, p * 3.5)
    s = 1 + 2.2 * (1 - k) ** 2                           # numero batendo
    f = ImageFont.truetype(F + "impact.ttf", max(40, int(230 / s)))
    outlined(d, (W // 2, 1040), "1981", f, (255, 232, 60), w=11)
    outlined(d, (W // 2, 1330), "CAPTOPRIL", TAG, (255, 255, 255), w=7)

def scene_press(img, p, t):
    d = ImageDraw.Draw(img)
    y = int(900 + 300 * min(1.0, p * 1.6))               # seta caindo
    d.polygon([(W // 2 - 90, y - 150), (W // 2 + 90, y - 150), (W // 2 + 90, y),
               (W // 2 + 170, y), (W // 2, y + 170), (W // 2 - 170, y), (W // 2 - 90, y)],
              fill=(60, 220, 120))
    outlined(d, (W // 2, 1560), "PRESSÃO", TAG, (255, 255, 255), w=7)

def scene_split(img, p, t):
    d = ImageDraw.Draw(img)
    top, bot = 560, 1420
    sn = fit(HEADC, 700)
    img.alpha_composite(sn, (-80, top + 240))
    pl = PILL.copy(); r = 560 / pl.width
    pl = pl.resize((560, int(pl.height * r)), Image.LANCZOS).crop((0, 0, 560, min(860, int(pl.height * r))))
    img.paste(pl, (540, top + 120))
    d.line([(W // 2, top), (W // 2, bot)], fill=(255, 255, 255), width=8)
    if p > 0.25:
        cx, cy, s = 270, top + 430, 150                  # X vermelho
        d.line([(cx - s, cy - s), (cx + s, cy + s)], fill=(235, 40, 40), width=30)
        d.line([(cx + s, cy - s), (cx - s, cy + s)], fill=(235, 40, 40), width=30)
    if p > 0.5:
        cx, cy = 810, top + 430                          # check verde
        d.line([(cx - 110, cy), (cx - 20, cy + 95)], fill=(60, 220, 120), width=30)
        d.line([(cx - 20, cy + 95), (cx + 125, cy - 105)], fill=(60, 220, 120), width=30)
    outlined(d, (270, 1530), "VENENO", TAG, (235, 90, 90), w=7)
    outlined(d, (810, 1530), "REMÉDIO", TAG, (120, 230, 160), w=7)

METER = [("VELOCIDADE", 6, (90, 190, 255)), ("FORÇA", 4, (255, 170, 60)),
         ("ESTRANHEZA", 10, (200, 120, 255)), ("PERIGO", 9, (235, 70, 70))]

def scene_meter(img, p, t):
    d = ImageDraw.Draw(img)
    sil = fit(HEAD3, 1000)
    sh = Image.new("RGBA", sil.size, (0, 0, 0, 0))
    sh.putalpha(sil.getchannel("A").point(lambda a: int(a * 0.30)))
    img.alpha_composite(sh, ((W - sil.width) // 2, 980))
    y0 = 560
    for i, (nome, val, cor) in enumerate(METER):
        ap = max(0.0, min(1.0, (p - i * 0.17) / 0.20))   # uma barra a cada ~1,2 s
        y = y0 + i * 190
        d.text((110, y), nome, font=OM, fill=(255, 255, 255))
        d.rounded_rectangle([110, y + 62, 970, y + 124], 14, fill=(255, 255, 255, 45))
        w = int(860 * (val / 10) * ap)
        if w > 14:
            d.rounded_rectangle([110, y + 62, 110 + w, y + 124], 14, fill=cor)
        if ap > 0.9:
            outlined(d, (930, y + 30), str(val), OM, cor, w=6)

def scene_close(img, p, t):
    d = ImageDraw.Draw(img)
    sn = fit(HEAD3, int(1120 * (1 + 0.05 * p)))
    img.alpha_composite(sn, ((W - sn.width) // 2, 740))
    if p < 0.12:                                          # flash
        fl = Image.new("RGBA", (W, H), (255, 255, 255, int(190 * (1 - p / 0.12))))
        img.alpha_composite(fl)
    import random
    rnd = random.Random(7)
    for i in range(60):                                   # confete
        cx = rnd.randrange(0, W)
        cy = int((rnd.randrange(300, 1700) + t * 320 * (0.6 + rnd.random())) % 1750) + 170
        c = [(255, 232, 60), (235, 70, 70), (120, 230, 160), (90, 190, 255)][i % 4]
        d.rectangle([cx, cy, cx + 13, cy + 22], fill=c)
    outlined(d, (W // 2, 1600), "VÊ CALOR.", HOOK, (255, 232, 60), w=10)
    outlined(d, (W // 2, 1716), "VIROU REMÉDIO.", TAG, (255, 255, 255), w=7)

DRAW = dict(hook=scene_hook, label=scene_label, thermal=scene_thermal, venom=scene_venom,
            year=scene_year, press=scene_press, split=scene_split, meter=scene_meter, close=scene_close)

# ------------------------------------------------------------- render
for i in range(NFRAMES):
    t = i / FPS
    sc = next((s for s in SC if s["f0"] <= i <= s["f1"]), SC[-1])
    p = (i - sc["f0"]) / max(1, sc["f1"] - sc["f0"])
    bgf = os.path.join(BG, f"s{sc['n']}", f"{i - sc['f0'] + 1:04d}.jpg")
    if not os.path.exists(bgf):
        bgf = sorted(os.listdir(os.path.join(BG, f"s{sc['n']}")))[-1]
        bgf = os.path.join(BG, f"s{sc['n']}", bgf)
    img = Image.open(bgf).convert("RGBA")
    DRAW[sc["kind"]](img, p, t)
    draw_caption(img, t, sc)
    img.convert("RGB").save(os.path.join(OUTF, f"{i:05d}.jpg"), quality=92)
    if i % 120 == 0:
        print("frame", i, "/", NFRAMES)

print("frames prontos:", NFRAMES)
