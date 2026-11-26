"""ONC-001 - etapa 8: montagem no estilo oficial da Onca Curiosa.

Regras medidas em referencias/ANALISE-ESTILO.md e agora no GUIA-ONCA.md:
  - UM cenario so, foto real clara e nitida, sem escurecer nem desfocar
  - bicho com 20 a 30% da altura, apoiado no terco inferior
  - contorno branco de adesivo em todo recorte
  - olho de desenho com anel amarelo na maior parte dos planos
  - 3 camadas de texto (topo palavra a palavra sem caixa / destaque gigante
    amarelo no meio / frase que acumula embaixo)
  - Oncometro como painel sobre a cena, com o nome do bicho
  - efeitos desenhados, nada de filtro
"""
import json, math, os, shutil, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

V = sys.argv[1]
W, H, FPS = 1080, 1920, 30
A = os.path.join(V, "assets")
TMP = os.path.join(V, "_render"); OUTF = os.path.join(TMP, "out")
shutil.rmtree(TMP, ignore_errors=True); os.makedirs(OUTF)

TL = json.load(open(os.path.join(V, "audio", "_timeline.json"), encoding="utf-8"))
FR = {f["n"]: f for f in TL["frases"]}
TOTAL = TL["total"]; FIM_FALA = TL["fim_fala"]
N = int(round(TOTAL * FPS))

F = "C:/Windows/Fonts/"
def fnt(n, s): return ImageFont.truetype(F + n, s)
L1   = fnt("ariblk.ttf", 66)    # legenda palavra a palavra
L1s  = fnt("ariblk.ttf", 54)
L2   = fnt("impact.ttf", 190)   # destaque gigante
L2s  = fnt("impact.ttf", 132)
L3   = fnt("ariblk.ttf", 60)    # frase que acumula
L3s  = fnt("ariblk.ttf", 48)
TAGF = fnt("ariblk.ttf", 44)
OMT  = fnt("ariblk.ttf", 44)
OML  = fnt("ariblk.ttf", 38)
OMN  = fnt("ariblk.ttf", 46)

AMARELO = (245, 221, 11)
BORDA_AM = (242, 229, 101)
PAINEL = (30, 29, 34)
TRILHA = (53, 59, 71)
VERM = (229, 57, 53)
VERDE = (60, 220, 120)

# ---------------------------------------------------------------- fundo unico
BGSRC = os.path.join(A, "fundos", "foto-9618231.jpg")
_bg = Image.open(BGSRC).convert("RGB")
_r = max(W / _bg.width, H / _bg.height)
_bg = _bg.resize((int(_bg.width * _r * 1.12), int(_bg.height * _r * 1.12)), Image.LANCZOS)
_bg = ImageEnhance.Color(_bg).enhance(1.12)
_bg = ImageEnhance.Contrast(_bg).enhance(1.05)

def fundo(p):
    """Ken Burns lento. Sem escurecer, sem desfocar."""
    z = 1.0 + 0.07 * p
    cw, ch = int(W / z * (_bg.width / W)), int(H / z * (_bg.height / H))
    cw = min(cw, _bg.width); ch = min(ch, _bg.height)
    x = (_bg.width - cw) // 2; y = int((_bg.height - ch) * 0.45)
    return _bg.crop((x, y, x + cw, y + ch)).resize((W, H), Image.LANCZOS).convert("RGBA")

# ------------------------------------------------------- recortes + adesivo
def sticker(im, esp=13):
    """contorno branco de adesivo em volta do recorte"""
    a = im.getchannel("A")
    g = a.filter(ImageFilter.GaussianBlur(esp * 0.55)).point(lambda v: 255 if v > 38 else 0)
    g = g.filter(ImageFilter.GaussianBlur(1.2))
    out = Image.new("RGBA", im.size, (0, 0, 0, 0))
    branco = Image.new("RGBA", im.size, (255, 255, 255, 255))
    out.paste(branco, (0, 0), g)
    out.alpha_composite(im)
    return out

def limpa_alfa(im, corte=150):
    """tira o alfa fantasma (corpo meio transparente) que vira mancha branca"""
    a = im.getchannel("A").point(lambda v: 255 if v > corte else 0)
    a = a.filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(0.8))
    out = im.copy(); out.putalpha(a)
    return out

def carregar(nome, corte=150):
    im = Image.open(os.path.join(A, nome)).convert("RGBA")
    im = limpa_alfa(im, corte)
    bb = im.getbbox()
    return im.crop(bb), bb

HA, bbA = carregar("inat-348275825-recorte.png")   # perfil p/ ESQUERDA
HB, bbB = carregar("inat-348275873-recorte.png")   # perfil p/ DIREITA
POSE_A = {"im": sticker(HA), "olho": (610 - bbA[0], 265 - bbA[1]),
          "pit": (610 - bbA[0], 310 - bbA[1]), "dir": -1}
POSE_A["olho"] = (790 - bbA[0], 265 - bbA[1])
POSE_B = {"im": sticker(HB), "olho": (395, 140), "pit": (265, 145), "dir": 1}

PILL, bbP = carregar("px-pills_medicine-8287535-recorte.png")
PILL = sticker(PILL)

ALT_BICHO = 500          # 26% de 1920 -> dentro de 20 a 30%
BASE_BICHO = 1830        # apoiado no terco inferior

def desenha_bicho(img, t, pose, escala=1.0, dx=0):
    p = pose
    alt = int(ALT_BICHO * escala)
    r = alt / p["im"].height
    sn = p["im"].resize((int(p["im"].width * r), alt), Image.LANCZOS)
    bal = math.sin(t * 2.3) * 9          # balanco suave: o bicho se mexe
    resp = 1 + 0.012 * math.sin(t * 3.1)
    sn = sn.resize((int(sn.width * resp), int(sn.height * resp)), Image.LANCZOS)
    ox = (W - sn.width) // 2 + dx + int(bal)
    oy = BASE_BICHO - sn.height + int(math.sin(t * 1.7) * 6)
    img.alpha_composite(sn, (ox, oy))
    sc = sn.width / p["im"].width
    return ox, oy, sc

def olho_cartoon(d, cx, cy, raio, t):
    """olho de desenho com anel amarelo - assinatura do canal"""
    pisca = (t * 1000 % 3100) < 160
    d.ellipse([cx - raio, cy - raio, cx + raio, cy + raio], fill=(250, 213, 11), outline=(20, 16, 8), width=5)
    ri = int(raio * 0.76)
    if pisca:
        d.ellipse([cx - ri, cy - ri, cx + ri, cy + ri], fill=(232, 220, 216))
        d.arc([cx - ri, cy - int(ri * 0.9), cx + ri, cy + int(ri * 1.1)], 200, 340, fill=(20, 16, 8), width=max(6, ri // 4))
        return
    d.ellipse([cx - ri, cy - ri, cx + ri, cy + ri], fill=(246, 240, 238), outline=(20, 16, 8), width=4)
    pr = int(ri * 0.52)
    px_, py_ = cx + int(ri * 0.10), cy + int(ri * 0.06)
    d.ellipse([px_ - pr, py_ - pr, px_ + pr, py_ + pr], fill=(18, 14, 10))
    br = max(4, pr // 3)
    d.ellipse([px_ - pr // 2 - br, py_ - pr // 2 - br, px_ - pr // 2 + br, py_ - pr // 2 + br], fill=(255, 255, 255))

# ---------------------------------------------------------------- textos
def contorno(d, xy, txt, f, fill, w, anchor="mm"):
    d.text(xy, txt, font=f, fill=fill, stroke_width=w, stroke_fill=(0, 0, 0), anchor=anchor)

CHAVE = {1: {"BURACO", "CALOR"}, 2: {"FOSSETA", "LORETAL", "LOREAL", "CALOR", "TÉRMICA"},
         3: {"VENENO", "PRESSÃO"}, 4: {"CAPTOPRIL", "OITENTA"}, 5: {"VENENO", "REMÉDIO"},
         6: {"ONÇÔMETRO"}, 7: {"CALOR", "REMÉDIO"}}

def palavras(n):
    fr = FR[n]; ws = fr["texto"].split()
    tot = sum(len(w) + 1 for w in ws)
    out, t = [], fr["ini"]
    for w in ws:
        dd = fr["dur"] * (len(w) + 1) / tot
        out.append((w, t, t + dd)); t += dd
    return out
WORDS = {n: palavras(n) for n in FR}

def legenda(img, t):
    """camada 1: topo, palavra a palavra, SEM caixa, chave em amarelo"""
    for n, ws in WORDS.items():
        for w, a, b in ws:
            if a <= t < b:
                limpa = w.upper().strip(":,.!?")
                cor = AMARELO if limpa in CHAVE.get(n, set()) else (255, 255, 255)
                d = ImageDraw.Draw(img)
                f = L1 if len(limpa) <= 11 else L1s
                contorno(d, (W // 2, 330), limpa, f, cor, 9)
                return

def destaque(img, txt, p_in, cor=AMARELO, y=720, f=None):
    """camada 2: destaque gigante amarelo, entra batendo"""
    d = ImageDraw.Draw(img)
    k = min(1.0, p_in * 5.0)
    s = 1 + 0.28 * (1 - k) ** 2
    ff = f or L2
    if s > 1.04:
        ff = ImageFont.truetype(F + ("impact.ttf" if ff in (L2, L2s) else "ariblk.ttf"),
                                max(30, int(ff.size / s)))
    contorno(d, (W // 2, y), txt, ff, cor, 15)

def frase_fica(img, linhas):
    """camada 3: frase que fica e acumula"""
    d = ImageDraw.Draw(img)
    y = 1150
    for txt in linhas:
        f = L3 if len(txt) <= 22 else L3s
        contorno(d, (W // 2, y), txt, f, (255, 255, 255), 10)
        y += 86

# ------------------------------------------------------- efeitos desenhados
def marcador_pit(d, px, py, r, t, cor=(250, 213, 11)):
    pr = int(r + 7 * math.sin(t * 7))
    d.ellipse([px - pr, py - pr, px + pr, py + pr], outline=cor, width=9)
    d.ellipse([px - pr - 9, py - pr - 9, px + pr + 9, py + pr + 9], outline=(0, 0, 0), width=4)

def cone_calor(img, px, py, t, dirx):
    """cone de calor saindo da fosseta - vetorial, nao filtro"""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    L = 680; ab = 205
    tip = (px + dirx * 40, py)
    far = (px + dirx * L, py)
    for i, (cor, f) in enumerate([((255, 90, 30, 112), 1.0), ((255, 170, 40, 124), 0.66), ((255, 240, 120, 150), 0.33)]):
        d.polygon([tip, (far[0], far[1] - int(ab * f)), (far[0], far[1] + int(ab * f))], fill=cor)
    for k in range(3):
        pts = []
        off = (k - 1) * 74
        for s in range(0, 22):
            x = px + dirx * (60 + s * 24)
            y = py + off + int(16 * math.sin(s * 0.7 + t * 6 + k))
            pts.append((x, y))
        d.line(pts, fill=(255, 245, 160, 235), width=10, joint="curve")
    img.alpha_composite(lay)

def carimbo(img, txt, cx, cy, t, ang=-11):
    lay = Image.new("RGBA", (760, 240), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([10, 10, 750, 230], 22, outline=VERM, width=12)
    d.text((380, 122), txt, font=fnt("impact.ttf", 128), fill=VERM, anchor="mm")
    lay = lay.rotate(ang, expand=True, resample=Image.BICUBIC)
    k = min(1.0, t * 6)
    s = 1 + 1.2 * (1 - k) ** 2
    lay = lay.resize((int(lay.width / s), int(lay.height / s)), Image.LANCZOS)
    img.alpha_composite(lay, (cx - lay.width // 2, cy - lay.height // 2))

def x_vermelho(d, cx, cy, s):
    for w, c in ((34, (0, 0, 0)), (22, VERM)):
        d.line([(cx - s, cy - s), (cx + s, cy + s)], fill=c, width=w)
        d.line([(cx + s, cy - s), (cx - s, cy + s)], fill=c, width=w)

def check_verde(d, cx, cy, s):
    pts = [(cx - s, cy), (cx - s // 4, cy + int(s * 0.7)), (cx + s, cy - int(s * 0.8))]
    d.line(pts, fill=(0, 0, 0), width=34, joint="curve")
    d.line(pts, fill=VERDE, width=22, joint="curve")

OM = [("VELOCIDADE", 6, (53, 163, 250)), ("FORÇA", 4, (240, 94, 57)),
      ("ESTRANHEZA", 10, (189, 89, 249)), ("PERIGO", 9, (245, 201, 8))]

def oncometro(img, p):
    """painel SOBRE a cena, com o nome do bicho. Nao e cena dedicada."""
    x0, x1, y0, y1 = 104, 980, 820, 1315
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([x0, y0, x1, y1], 42, fill=PAINEL + (238,), outline=BORDA_AM, width=6)
    cx = (x0 + x1) // 2
    d.rounded_rectangle([cx - 230, y0 - 38, cx + 230, y0 + 38], 38, fill=AMARELO)
    d.text((cx, y0), "ONÇÔMETRO", font=OMT, fill=(20, 16, 10), anchor="mm")
    d.text((cx, y0 + 92), "JARARACA", font=OMN, fill=(255, 255, 255), anchor="mm")
    ty0, ty1 = 487, 882
    for i, (nome, val, cor) in enumerate(OM):
        ap = max(0.0, min(1.0, (p - i * 0.15) / 0.17))
        y = y0 + 168 + i * 82
        d.text((x0 + 26, y), nome, font=OML, fill=(255, 255, 255), anchor="lm")
        d.rounded_rectangle([ty0, y - 22, ty1, y + 22], 22, fill=TRILHA)
        w = int((ty1 - ty0) * (val / 10) * ap)
        if w > 24:
            d.rounded_rectangle([ty0, y - 22, ty0 + w, y + 22], 22, fill=cor)
        if ap > 0.85:
            d.text((933, y), str(val), font=OMT, fill=cor, anchor="lm")
    img.alpha_composite(lay)

def cartela_final(img, p, t):
    """cartela de gancho para o proximo video, no padrao do canal"""
    d = ImageDraw.Draw(img)
    veu = Image.new("RGBA", (W, H), (12, 20, 10, int(165 * min(1.0, p * 4))))
    img.alpha_composite(veu)
    d = ImageDraw.Draw(img)
    contorno(d, (W // 2, 620), "PRÓXIMO:", L3, (255, 255, 255), 10)
    contorno(d, (W // 2, 810), "200 MILHÕES", L2s, AMARELO, 14)
    contorno(d, (W // 2, 950), "DELES", L2s, AMARELO, 14)
    # silhueta de cupinzeiro desenhada, estilo da referencia
    cx, base, hh = W // 2, 1560, 360
    pts = []
    for i in range(41):
        u = i / 40.0
        x = cx - 250 + u * 500
        y = base - int(hh * math.exp(-((u - 0.5) * 3.05) ** 2))
        pts.append((x, y))
    pts += [(cx + 250, base), (cx - 250, base)]
    d.polygon(pts, fill=(18, 22, 16))
    d.line(pts + [pts[0]], fill=AMARELO, width=10, joint="curve")
    for u in (0.32, 0.5, 0.68):
        x = cx - 250 + u * 500
        y = base - int(hh * math.exp(-((u - 0.5) * 3.05) ** 2))
        d.line([(x, y + 26), (x, base - 16)], fill=AMARELO, width=5)
    for i, (ox, oy) in enumerate([(-285, -250), (290, -200)]):
        contorno(d, (cx + ox, base + oy), "?", fnt("impact.ttf", 120), AMARELO, 10)
    contorno(d, (W // 2, 1690), "E A RAINHA? NINGUÉM ACHOU.", L3s, (255, 255, 255), 9)

# ---------------------------------------------------------------- beats
B = [dict(n=1, ini=FR[1]["ini"], fim=FR[1]["fim"], k="hook"),
     dict(n=2, ini=FR[2]["ini"], fim=FR[2]["fim"], k="pit"),
     dict(n=3, ini=FR[3]["ini"], fim=FR[3]["fim"], k="venom"),
     dict(n=4, ini=FR[4]["ini"], fim=FR[4]["fim"], k="year"),
     dict(n=5, ini=FR[5]["ini"], fim=FR[5]["fim"], k="nao"),
     dict(n=6, ini=FR[6]["ini"], fim=FR[6]["fim"], k="meter"),
     dict(n=7, ini=FR[7]["ini"], fim=FIM_FALA, k="close"),
     dict(n=8, ini=FIM_FALA, fim=TOTAL, k="card")]

def beat(t):
    for b in B:
        if b["ini"] <= t < b["fim"]:
            return b, (t - b["ini"]) / max(0.1, b["fim"] - b["ini"])
    return B[-1], 1.0

print("renderizando", N, "quadros |", round(TOTAL, 2), "s")
for i in range(N):
    t = i / FPS
    b, p = beat(t)
    img = fundo(t / TOTAL)
    d = ImageDraw.Draw(img)
    linhas = []

    if b["k"] == "card":
        cartela_final(img, p, t)
        img.convert("RGB").save(os.path.join(OUTF, f"{i:05d}.jpg"), quality=92)
        continue

    pose = POSE_B if b["k"] == "venom" else POSE_A
    esc = 1.06 if b["k"] in ("hook", "pit") else 1.0
    ox, oy, sc = desenha_bicho(img, t, pose, esc)
    d = ImageDraw.Draw(img)
    ex, ey = ox + int(pose["olho"][0] * sc), oy + int(pose["olho"][1] * sc)
    px, py = ox + int(pose["pit"][0] * sc), oy + int(pose["pit"][1] * sc)
    raio = int(86 * sc * (1.25 if b["k"] in ("hook", "pit") else 1.0))

    if b["k"] == "hook":
        marcador_pit(d, px, py, int(62 * sc), t)
        d.line([(px - pose["dir"] * 230, py - 210), (px - pose["dir"] * 60, py - 50)],
               fill=(0, 0, 0), width=16)
        d.line([(px - pose["dir"] * 230, py - 210), (px - pose["dir"] * 60, py - 50)],
               fill=AMARELO, width=9)
        destaque(img, "ESSE BURACO", p, AMARELO, 660, L2s)
        destaque(img, "VÊ CALOR", p, AMARELO, 800, L2)
    elif b["k"] == "pit":
        if t >= b["ini"] + 1.9:
            cone_calor(img, px, py, t, pose["dir"])
        d = ImageDraw.Draw(img)
        marcador_pit(d, px, py, int(58 * sc), t, AMARELO)
        destaque(img, "FOSSETA LOREAL", p, AMARELO, 700, L2s)
        if t >= b["ini"] + 2.4:
            linhas.append("ACHA A PRESA PELO CALOR")
        if t >= b["ini"] + 3.7:
            linhas.append("COMO CÂMERA TÉRMICA")
    elif b["k"] == "venom":
        carimbo(img, "VENENO", W // 2, 700, max(0.01, t - b["ini"]))
        if t >= b["ini"] + 1.4:
            linhas.append("DERRUBA A PRESSÃO")
    elif b["k"] == "year":
        pr = PILL.resize((620, int(PILL.height * 620 / PILL.width)), Image.LANCZOS)
        ent = min(1.0, p * 3.0); ease = 1 - (1 - ent) ** 3
        img.alpha_composite(pr, (int(W - 660 + (1 - ease) * 760), 1010))
        destaque(img, "1981", p, AMARELO, 700)
        linhas.append("VIROU REMÉDIO DE PRESSÃO")
    elif b["k"] == "nao":
        d2 = ImageDraw.Draw(img)
        pr = PILL.resize((470, int(PILL.height * 470 / PILL.width)), Image.LANCZOS)
        img.alpha_composite(pr, (W - 500, 1120))
        d2 = ImageDraw.Draw(img)
        if p > 0.18:
            x_vermelho(d2, 235, 1480, 118)
        if p > 0.52:
            check_verde(d2, W - 265, 1290, 108)
        linhas.append("NINGUÉM TOMA VENENO")
        if p > 0.45:
            linhas.append("O REMÉDIO FOI DESENHADO")
    elif b["k"] == "meter":
        oncometro(img, p)
    elif b["k"] == "close":
        destaque(img, "VÊ CALOR.", p, AMARELO, 700, L2s)
        if p > 0.35:
            linhas.append("E VIROU REMÉDIO.")

    if b["k"] != "meter":
        d = ImageDraw.Draw(img)
        olho_cartoon(d, ex, ey, raio, t)
    else:
        d = ImageDraw.Draw(img)
        olho_cartoon(d, ex, ey, int(86 * sc), t)

    if linhas:
        frase_fica(img, linhas)
    legenda(img, t)
    img.convert("RGB").save(os.path.join(OUTF, f"{i:05d}.jpg"), quality=92)
    if i % 150 == 0:
        print("  quadro", i, "/", N)

print("frames prontos:", N)
