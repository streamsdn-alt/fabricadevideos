"""Cenário ilustrado de Mata Atlântica, desenhado em código (sem gerar imagem).
Uso: python fundo_mata.py saida.png [largura] [altura] [semente]
"""
import sys, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def grad(w, h, top, bot):
    t = np.linspace(0, 1, h)[:, None, None]
    a = np.array(top)[None, None, :]; b = np.array(bot)[None, None, :]
    arr = (a * (1 - t) + b * t).repeat(w, axis=1)
    return Image.fromarray(arr.astype('uint8'), 'RGB').convert('RGBA')


def blob(d, cx, cy, r, fill, n=9, jit=0.35, rnd=random):
    pts = []
    for i in range(n * 3):
        a = 2 * math.pi * i / (n * 3)
        rr = r * (1 + jit * math.sin(a * n / 2 + rnd.random()) * rnd.random())
        pts.append((cx + rr * math.cos(a), cy + rr * 0.85 * math.sin(a)))
    d.polygon(pts, fill=fill)


def cloud(layer, cx, cy, s, rnd):
    d = ImageDraw.Draw(layer)
    parts = [(-1.0, 0.15, .55), (-.45, -.25, .75), (.2, -.35, .85), (.8, -.05, .6), (1.25, .2, .45), (0, .2, .7)]
    for dx, dy, r in parts:
        d.ellipse([cx + dx * s - r * s, cy + dy * s - r * s, cx + dx * s + r * s, cy + dy * s + r * s], fill=(255, 255, 255, 255))
    # sombra embaixo
    sh = Image.new('RGBA', layer.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    ds.ellipse([cx - 1.4 * s, cy + .05 * s, cx + 1.6 * s, cy + .75 * s], fill=(170, 200, 235, 150))
    return sh


def leaf(d, x, y, L, ang, col, vein=None):
    ca, sa = math.cos(ang), math.sin(ang)
    pts = []
    for i in range(21):
        t = i / 20
        w = math.sin(math.pi * t) * L * 0.28
        pts.append((t * L, w))
    for i in range(20, -1, -1):
        t = i / 20
        w = math.sin(math.pi * t) * L * 0.28
        pts.append((t * L, -w))
    pts = [(x + px * ca - py * sa, y + px * sa + py * ca) for px, py in pts]
    d.polygon(pts, fill=col)
    if vein:
        d.line([(x, y), (x + L * ca, y + L * sa)], fill=vein, width=max(2, int(L / 40)))


def frond(d, x, y, L, ang, col, rnd):
    """samambaia: haste com folíolos"""
    ca, sa = math.cos(ang), math.sin(ang)
    d.line([(x, y), (x + L * ca, y + L * sa)], fill=col, width=max(3, int(L / 60)))
    n = 14
    for i in range(1, n):
        t = i / n
        px, py = x + L * t * ca, y + L * t * sa
        ll = L * 0.32 * (1 - t * 0.8)
        for s in (-1, 1):
            leaf(d, px, py, ll, ang + s * 1.0, col)


def make(w=1300, h=2310, seed=7):
    rnd = random.Random(seed)
    img = grad(w, h, (64, 158, 235), (190, 228, 250))
    # sol
    sun = Image.new('RGBA', (w, h), (0, 0, 0, 0)); ds = ImageDraw.Draw(sun)
    for r, a in [(260, 40), (180, 70), (110, 255)]:
        ds.ellipse([w * .82 - r, h * .07 - r, w * .82 + r, h * .07 + r], fill=(255, 246, 190, a))
    img.alpha_composite(sun.filter(ImageFilter.GaussianBlur(6)))
    # nuvens
    cl = Image.new('RGBA', (w, h), (0, 0, 0, 0)); shadows = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    for cx, cy, s in [(w * .18, h * .09, 120), (w * .55, h * .15, 150), (w * .95, h * .22, 110), (w * .3, h * .24, 90)]:
        shadows.alpha_composite(cloud(cl, cx, cy, s, rnd))
    img.alpha_composite(shadows.filter(ImageFilter.GaussianBlur(14)))
    img.alpha_composite(cl.filter(ImageFilter.GaussianBlur(2)))
    # morros distantes (serra do mar)
    for k, (col, base, amp) in enumerate([((120, 178, 150), .36, 90), ((86, 156, 110), .41, 110), ((60, 135, 80), .46, 80)]):
        lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        pts = [(0, h)]
        ph = rnd.random() * 6
        for x in range(0, w + 20, 20):
            y = h * base - amp * (0.6 * math.sin(x / 210 + ph) + 0.4 * math.sin(x / 90 + ph * 2))
            pts.append((x, y))
        pts.append((w, h)); d.polygon(pts, fill=col + (255,))
        # copas pontilhando a crista
        for x in range(0, w, 34):
            y = h * base - amp * (0.6 * math.sin(x / 210 + ph) + 0.4 * math.sin(x / 90 + ph * 2))
            blob(d, x + rnd.randint(-8, 8), y + 6, 26 + rnd.randint(-6, 10), col + (255,), rnd=rnd)
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(3 - k)))
    # árvores do meio
    lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for tx in [-40, 170, 420, 760, 1010, 1260]:
        tx += rnd.randint(-40, 40)
        top = h * (.30 + rnd.random() * .06); bot = h * .66
        tw = 34 + rnd.randint(0, 22)
        d.polygon([(tx - tw, bot), (tx - tw * .55, top), (tx + tw * .55, top), (tx + tw, bot)], fill=(118, 82, 52, 255))
        d.line([(tx - tw * .2, bot), (tx - tw * .1, top)], fill=(150, 108, 70, 255), width=6)
        for j in range(16):
            cx = tx + rnd.randint(-170, 170); cy = top + rnd.randint(-120, 80)
            r = rnd.randint(70, 120)
            g = rnd.choice([(46, 122, 62), (58, 140, 70), (76, 158, 72), (40, 108, 58)])
            blob(d, cx, cy, r, g + (255,), rnd=rnd)
            blob(d, cx - r * .25, cy - r * .3, r * .45, (126, 196, 96, 255), rnd=rnd)
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.2)))
    # chão de folhas secas
    lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    gy = h * .62
    d.polygon([(0, gy + 40), (w * .3, gy), (w * .7, gy + 20), (w, gy - 10), (w, h), (0, h)], fill=(196, 134, 72, 255))
    ground = lay.copy()
    for i in range(900):
        y = gy + (h - gy) * (rnd.random() ** 0.8)
        x = rnd.random() * w
        sc = 0.4 + 1.2 * (y - gy) / (h - gy)
        col = rnd.choice([(214, 150, 70), (178, 104, 50), (232, 176, 86), (160, 92, 44), (204, 128, 58), (120, 150, 60)])
        leaf(d, x, y, 34 * sc + rnd.random() * 20 * sc, rnd.random() * 6.28, col + (255,), vein=(120, 70, 35, 255))
    img.alpha_composite(lay)
    # pedras
    lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for cx, cy, r in [(w * .12, h * .70, 120), (w * .9, h * .69, 140), (w * .55, h * .66, 70)]:
        d.ellipse([cx - r * 1.3, cy - r * .8, cx + r * 1.3, cy + r * .7], fill=(128, 120, 108, 255))
        d.ellipse([cx - r * 1.1, cy - r * .75, cx + r * .6, cy + r * .1], fill=(168, 160, 146, 255))
        d.ellipse([cx - r * .9, cy - r * .7, cx - r * .1, cy - r * .35], fill=(196, 190, 176, 255))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1)))
    # samambaias e bromélias nas laterais
    lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for side in (0, 1):
        bx = 0 if side == 0 else w
        for k in range(7):
            ang = (-0.9 - k * 0.22) if side == 0 else (math.pi + 0.9 + k * 0.22)
            ang = -ang if False else ang
            a2 = (-math.pi / 2 + 0.25 + k * 0.18) if side == 0 else (-math.pi / 2 - 0.25 - k * 0.18)
            frond(d, bx + (40 if side == 0 else -40), h * .74, 420 + rnd.randint(-60, 60), a2, rnd.choice([(52, 140, 66, 255), (70, 160, 70, 255), (40, 120, 60, 255)]), rnd)
    # bromélia
    for cx in (w * .2, w * .83):
        for k in range(9):
            a = -math.pi / 2 + (k - 4) * 0.28
            leaf(d, cx, h * .80, 230, a, (86, 170, 84, 255) if k % 2 == 0 else (60, 150, 80, 255), vein=(40, 110, 55, 255))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(0.6)))
    # luz: leve vinheta quente + textura
    arr = np.asarray(img.convert('RGB')).astype(np.float32)
    noise = np.random.default_rng(seed).normal(0, 4, arr.shape[:2])[:, :, None]
    arr = np.clip(arr + noise, 0, 255)
    out = Image.fromarray(arr.astype('uint8'))
    return out


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'fundo.png'
    w = int(sys.argv[2]) if len(sys.argv) > 2 else 1300
    h = int(sys.argv[3]) if len(sys.argv) > 3 else 2310
    s = int(sys.argv[4]) if len(sys.argv) > 4 else 7
    make(w, h, s).save(out)
