"""Modelo de montagem da Onça Curiosa (Fábrica de vídeos).

Monta um Short 1080x1920 a 30 fps no estilo do canal:
  - um cenário só, claro, com câmera que muda de enquadramento (cortes);
  - bicho recortado com contorno branco de adesivo, olho de desenho que pisca;
  - 3 camadas de texto: legenda palavra a palavra no topo (palavra-chave amarela),
    destaque gigante amarelo no meio, frases que ficam e acumulam;
  - Onçômetro como painel sobre a cena, barras enchendo uma a uma;
  - efeitos desenhados (anel, seta, ondas de calor, gotas, manômetro, X, check, raios).

Uso: python onca_render.py roteiro.json saida.mp4 [--quadros pasta] [--ate SEG]
O roteiro.json descreve tudo (ver exemplo ONC-001.json). Nada aqui é específico da jararaca.
"""
import json, math, subprocess, sys, os, argparse, random
from functools import lru_cache
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(AQUI, 'fontes', 'Montserrat-Black.ttf')
AMARELO = (245, 221, 11)
ANEL = (250, 213, 11)
VERMELHO = (230, 50, 45)
VERDE = (60, 200, 90)
BARRAS = {'VELOCIDADE': (53, 163, 250), 'FORÇA': (240, 94, 57), 'ESTRANHEZA': (189, 89, 249), 'PERIGO': (245, 201, 8)}


# ---------------------------------------------------------------- utilidades
def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def back(t):  # entrada com leve passada (pop)
    t = max(0.0, min(1.0, t))
    c = 1.70158
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2


@lru_cache(maxsize=64)
def fonte(tam):
    return ImageFont.truetype(FONTE, tam)


@lru_cache(maxsize=512)
def texto_img(txt, tam, cor, contorno, cor_contorno=(0, 0, 0)):
    f = fonte(tam)
    linhas = txt.split('\n')
    bbs = [f.getbbox(l, stroke_width=contorno) for l in linhas]
    lw = max(b[2] - b[0] for b in bbs)
    lh = int(tam * 1.08)
    im = Image.new('RGBA', (lw + contorno * 2 + 8, lh * len(linhas) + contorno * 2 + 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, (l, b) in enumerate(zip(linhas, bbs)):
        x = (im.width - (b[2] - b[0])) // 2 - b[0]
        d.text((x, contorno + 4 + i * lh - b[1] // 2), l, font=f, fill=cor, stroke_width=contorno, stroke_fill=cor_contorno)
    return im


def colar(base, im, cx, cy, escala=1.0, rot=0.0, alfa=1.0):
    if im is None or escala <= 0.01 or alfa <= 0.01:
        return
    if escala != 1.0:
        im = im.resize((max(1, int(im.width * escala)), max(1, int(im.height * escala))), Image.BICUBIC)
    if rot:
        im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    if alfa < 1:
        a = im.getchannel('A').point(lambda v: int(v * alfa))
        im = im.copy(); im.putalpha(a)
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))


# ---------------------------------------------------------------- bicho (adesivo)
def limpar_alfa(rgba):
    a = np.array(rgba.getchannel('A'))
    a = np.where(a < 110, 0, a).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats((a > 0).astype(np.uint8))
    if n > 1:
        maior = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
        a = np.where(lab == maior, a, 0).astype(np.uint8)
    out = rgba.copy(); out.putalpha(Image.fromarray(a))
    return out


def adesivo(caminho, largura, borda=13, recorte_lado=None):
    """Recorte -> adesivo com contorno branco e sombra. recorte_lado: lado onde a foto
    foi cortada ('esq'/'dir'); nesse lado não desenha contorno (o bicho 'sai' da tela)."""
    im = limpar_alfa(Image.open(caminho).convert('RGBA'))
    bb = im.getbbox(); im = im.crop(bb)
    esc = largura / im.width
    im = im.resize((int(im.width * esc), int(im.height * esc)), Image.LANCZOS)
    pad = borda * 3
    can = Image.new('RGBA', (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    can.alpha_composite(im, (pad, pad))
    a = np.array(can.getchannel('A'))
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (borda * 2 + 1, borda * 2 + 1))
    dil = cv2.dilate((a > 40).astype(np.uint8) * 255, k)
    dil = cv2.GaussianBlur(dil, (3, 3), 0)
    branco = Image.new('RGBA', can.size, (255, 255, 255, 0)); branco.putalpha(Image.fromarray(dil))
    sombra = Image.new('RGBA', can.size, (30, 20, 10, 0)); sombra.putalpha(Image.fromarray((dil * 0.35).astype(np.uint8)))
    sombra = sombra.filter(ImageFilter.GaussianBlur(10))
    out = Image.new('RGBA', can.size, (0, 0, 0, 0))
    out.alpha_composite(sombra, (8, 14)); out.alpha_composite(branco); out.alpha_composite(can)
    if recorte_lado == 'dir':
        out = out.crop((0, 0, out.width - pad, out.height))
    elif recorte_lado == 'esq':
        out = out.crop((pad, 0, out.width, out.height))
    # fator para converter coordenadas da foto original para o adesivo
    def conv(x, y):
        x2 = (x - bb[0]) * esc + pad - (pad if recorte_lado == 'esq' else 0)
        y2 = (y - bb[1]) * esc + pad
        return x2, y2
    return out, conv, esc


def olho(r, piscando=0.0, olhar=(0.0, 0.0)):
    """Olho de desenho da Onça: miolo claro, pupila, brilho, anel amarelo grosso."""
    s = int(r * 2 + 40)
    im = Image.new('RGBA', (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = s / 2
    anel = max(6, int(r * 0.22))
    d.ellipse([c - r - anel, c - r - anel, c + r + anel, c + r + anel], fill=(20, 15, 10, 255))
    d.ellipse([c - r - anel + 4, c - r - anel + 4, c + r + anel - 4, c + r + anel - 4], fill=ANEL + (255,))
    d.ellipse([c - r, c - r, c + r, c + r], fill=(245, 236, 232, 255))
    if piscando > 0.5:  # pálpebra fechada: curva sorridente
        d.ellipse([c - r, c - r, c + r, c + r], fill=(196, 160, 90, 255))
        d.arc([c - r * .7, c - r * .9, c + r * .7, c + r * .5], 20, 160, fill=(20, 15, 10, 255), width=max(4, int(r * .16)))
    else:
        pr = r * 0.48
        px, py = c + olhar[0] * r * .35, c + olhar[1] * r * .3
        d.ellipse([px - pr, py - pr, px + pr, py + pr], fill=(15, 12, 10, 255))
        hr = pr * 0.38
        d.ellipse([px - pr * .45 - hr, py - pr * .5 - hr, px - pr * .45 + hr, py - pr * .5 + hr], fill=(255, 255, 255, 255))
    return im


# ---------------------------------------------------------------- efeitos desenhados
def ef_anel(base, x, y, r, t):
    pulso = 1 + 0.12 * math.sin(t * 9)
    d = ImageDraw.Draw(base)
    rr = r * pulso
    for w, cor in [(16, (0, 0, 0, 255)), (10, AMARELO + (255,))]:
        d.ellipse([x - rr, y - rr, x + rr, y + rr], outline=cor, width=w)


def ef_seta(base, x0, y0, x1, y1, t):
    p = ease(t / 0.35)
    xe, ye = x0 + (x1 - x0) * p, y0 + (y1 - y0) * p
    d = ImageDraw.Draw(base)
    d.line([(x0, y0), (xe, ye)], fill=(0, 0, 0, 255), width=22)
    d.line([(x0, y0), (xe, ye)], fill=AMARELO + (255,), width=12)
    if p > 0.95:
        ang = math.atan2(y1 - y0, x1 - x0)
        pts = [(x1, y1), (x1 - 46 * math.cos(ang - .5), y1 - 46 * math.sin(ang - .5)), (x1 - 46 * math.cos(ang + .5), y1 - 46 * math.sin(ang + .5))]
        d.polygon(pts, fill=AMARELO + (255,), outline=(0, 0, 0, 255), width=5)


def ef_calor(base, x, y, t, direcao=-1):
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(5):
        fase = (t * 1.6 + k / 5) % 1.0
        r = 40 + fase * 330
        a = int(255 * (1 - fase))
        cor = (255, int(120 + 100 * (1 - fase)), 30, a)
        if direcao < 0:
            d.arc([x - r, y - r, x + r, y + r], 140, 220, fill=cor, width=16)
        else:
            d.arc([x - r, y - r, x + r, y + r], -40, 40, fill=cor, width=16)
    base.alpha_composite(lay)


def ef_gotas(base, x, y, t):
    d = ImageDraw.Draw(base)
    for k in range(4):
        fase = (t * 0.9 + k * 0.27) % 1.0
        gx = x + (k - 1.5) * 34
        gy = y + fase * 260
        s = 22 + k * 3
        d.ellipse([gx - s, gy - s, gx + s, gy + s], fill=(110, 220, 70, 255), outline=(20, 60, 15, 255), width=4)
        d.polygon([(gx - s * .8, gy - s * .4), (gx, gy - s * 2.1), (gx + s * .8, gy - s * .4)], fill=(110, 220, 70, 255))
        d.ellipse([gx - s * .45, gy - s * .45, gx - s * .05, gy - s * .05], fill=(220, 255, 200, 255))


def ef_manometro(base, cx, cy, t, de=0.85, ate=0.12, rotulo='PRESSÃO'):
    """Manômetro desenhado (mesma linguagem do velocímetro do avestruz)."""
    r = 150
    d = ImageDraw.Draw(base)
    d.pieslice([cx - r - 12, cy - r - 12, cx + r + 12, cy + r + 12], 180, 360, fill=(0, 0, 0, 255))
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=(250, 250, 245, 255))
    for i, cor in enumerate([(60, 200, 90), (245, 201, 8), (230, 50, 45)]):
        d.arc([cx - r + 14, cy - r + 14, cx + r - 14, cy + r - 14], 180 + i * 60, 240 + i * 60, fill=cor + (255,), width=22)
    for i in range(11):
        a = math.pi + math.pi * i / 10
        d.line([(cx + (r - 40) * math.cos(a), cy + (r - 40) * math.sin(a)), (cx + (r - 58) * math.cos(a), cy + (r - 58) * math.sin(a))], fill=(0, 0, 0, 255), width=5)
    v = de + (ate - de) * ease(t)
    v += 0.02 * math.sin(t * 30) * (1 - ease(t))
    a = math.pi + math.pi * v
    d.line([(cx, cy), (cx + (r - 30) * math.cos(a), cy + (r - 30) * math.sin(a))], fill=(230, 40, 40, 255), width=12)
    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=(0, 0, 0, 255))
    colar(base, texto_img(rotulo, 46, (255, 255, 255), 6), cx, cy + 46)


def ef_x(base, x, y, s, t):
    p = ease(t / 0.25)
    d = ImageDraw.Draw(base)
    for (a, b) in [((-1, -1), (1, 1)), ((1, -1), (-1, 1))]:
        x0, y0 = x + a[0] * s, y + a[1] * s
        x1, y1 = x0 + (x + b[0] * s - x0) * p, y0 + (y + b[1] * s - y0) * p
        d.line([(x0, y0), (x1, y1)], fill=(0, 0, 0, 255), width=40)
        d.line([(x0, y0), (x1, y1)], fill=VERMELHO + (255,), width=26)


def ef_check(base, x, y, s, t):
    p = ease(t / 0.3)
    pts = [(x - s, y), (x - s * .3, y + s * .7), (x + s, y - s * .8)]
    d = ImageDraw.Draw(base)
    seg1 = min(1, p * 2); seg2 = max(0, p * 2 - 1)
    a = pts[0]; b = (pts[0][0] + (pts[1][0] - pts[0][0]) * seg1, pts[0][1] + (pts[1][1] - pts[0][1]) * seg1)
    for w, cor in [(40, (0, 0, 0, 255)), (26, VERDE + (255,))]:
        d.line([a, b], fill=cor, width=w)
        if seg2 > 0:
            c = (pts[1][0] + (pts[2][0] - pts[1][0]) * seg2, pts[1][1] + (pts[2][1] - pts[1][1]) * seg2)
            d.line([pts[1], c], fill=cor, width=w)


def ef_raios(base, cx, cy, t, alfa=0.55):
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    n = 16; R = 2600
    for i in range(n):
        a0 = 2 * math.pi * i / n + t * 0.35
        a1 = a0 + math.pi / n
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=(255, 214, 40, int(255 * alfa)))
    base.alpha_composite(lay)


def ef_frasco(base, img, x, y, t, larg=360):
    p = back(t / 0.4)
    colar(base, img, x, y - (1 - p) * 300, escala=larg / img.width * max(0.01, min(1, p)), rot=6 * math.sin(t * 3))


# ---------------------------------------------------------------- Onçômetro
def oncometro(base, nome, valores, t0_barras, t, alfa=1.0):
    x0, x1 = 108, 972
    y0 = 860
    linhas = list(valores.items())
    y1 = y0 + 150 + 92 * len(linhas)
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([x0, y0, x1, y1], radius=42, fill=(30, 29, 34, 245), outline=(242, 229, 101, 255), width=8)
    cap = texto_img('ONÇÔMETRO', 44, (0, 0, 0), 0)
    cw = cap.width + 60
    d.rounded_rectangle([540 - cw / 2, y0 - 34, 540 + cw / 2, y0 + 34], radius=34, fill=AMARELO + (255,), outline=(0, 0, 0, 255), width=4)
    colar(lay, cap, 540, y0 + 2)
    colar(lay, texto_img(nome, 52, (255, 255, 255), 0), 540, y0 + 82)
    for i, (rot, val) in enumerate(linhas):
        yy = y0 + 170 + i * 92
        cor = BARRAS.get(rot, AMARELO)
        r_im = texto_img(rot, 38, (255, 255, 255), 0)
        lay.alpha_composite(r_im, (x0 + 40, int(yy - r_im.height / 2)))
        bx0, bx1 = x0 + 380, x1 - 110
        d.rounded_rectangle([bx0, yy - 16, bx1, yy + 16], radius=16, fill=(53, 59, 71, 255))
        ti = t0_barras[i]
        p = ease((t - ti) / 0.55) if t >= ti else 0.0
        vv = val * p
        if vv > 0.05:
            d.rounded_rectangle([bx0, yy - 16, bx0 + (bx1 - bx0) * vv / 10, yy + 16], radius=16, fill=cor + (255,))
        num = texto_img(str(int(round(vv))) if p > 0 else '0', 44, cor, 0)
        lay.alpha_composite(num, (int(x1 - 50 - num.width / 2), int(yy - num.height / 2)))
    if alfa < 1:
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * alfa)))
    base.alpha_composite(lay)


# ---------------------------------------------------------------- palavras
def tempos_palavras(timeline):
    out = []
    for fr in timeline['frases']:
        ws = fr['texto'].split()
        pesos = [len(w.strip('.,:!?;')) + 2 for w in ws]
        tot = sum(pesos); t = fr['ini']
        for w, p in zip(ws, pesos):
            dur = (fr['fim'] - fr['ini']) * p / tot
            out.append({'w': w, 'ini': t, 'fim': t + dur, 'frase': fr['n']})
            t += dur
    return out


def norm(w):
    return w.strip('.,:!?;').upper()


# ---------------------------------------------------------------- render
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('roteiro'); ap.add_argument('saida')
    ap.add_argument('--quadros'); ap.add_argument('--ate', type=float)
    a = ap.parse_args()
    R = json.load(open(a.roteiro, encoding='utf-8'))
    base_dir = os.path.dirname(os.path.abspath(a.roteiro))
    P = lambda p: p if os.path.isabs(p) else os.path.join(base_dir, p)
    tl = json.load(open(P(R['timeline']), encoding='utf-8'))
    palavras = tempos_palavras(tl)
    dur = a.ate or tl['total']
    chaves = set(k.upper() for k in R.get('palavras_chave', []))

    fundo = Image.open(P(R['fundo'])).convert('RGB')
    FW, FH = fundo.size

    bichos = {}
    for nome, b in R['bichos'].items():
        im, conv, esc = adesivo(P(b['arquivo']), b['largura'], recorte_lado=b.get('cortado'))
        bichos[nome] = dict(im=im, conv=conv, b=b, esc=esc)
    extras = {n: adesivo(P(f), 600)[0] for n, f in R.get('objetos', {}).items()}

    def quando(lista, t):
        for s in lista:
            if s['de'] <= t < s['ate']:
                yield s

    ff = None
    if not a.quadros:
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                               '-i', P(R['narracao']), '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19',
                               '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-af', 'loudnorm=I=-14:TP=-1.5', '-shortest', '-t', str(dur), a.saida],
                              stdin=subprocess.PIPE)
    else:
        os.makedirs(a.quadros, exist_ok=True)

    nfr = int(dur * FPS)
    rnd = random.Random(3)
    for fi in range(nfr):
        t = fi / FPS
        # câmera (enquadramento) — cortes secos entre planos, zoom lento dentro do plano
        cam = next(quando(R['camera'], t), R['camera'][-1])
        tz = t - cam['de']
        z = cam['zoom'] * (1 + 0.015 * tz)
        if cam.get('tremida') and tz < cam['tremida']:
            sx, sy = rnd.uniform(-14, 14), rnd.uniform(-14, 14)
        else:
            sx = sy = 0
        cw, ch = FW / z, FW / z * H / W
        cx = cam.get('x', 0.5) * FW; cy = cam.get('y', 0.5) * FH
        ch = min(ch, FH); cw = min(cw, FW)
        x0 = max(0, min(cx - cw / 2, FW - cw)); y0 = max(0, min(cy - ch / 2, FH - ch))
        frame = fundo.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch)).convert('RGBA')
        k = W / cw  # px do quadro por px do fundo

        for e in quando(R.get('raios', []), t):
            ef_raios(frame, e['x'], e['y'], t - e['de'], e.get('alfa', .5))

        # bichos
        olhos_desenhar = []
        for s in quando(R['cenas_bicho'], t):
            B = bichos[s['bicho']]
            ts = t - s['de']
            ent = s.get('entrada', 0.45)
            p = back(ts / ent) if ent else 1.0
            ax, ay = s['x'], s['y']
            if s.get('vem_de') == 'dir':
                ax = ax + (1 - p) * 900
            elif s.get('vem_de') == 'esq':
                ax = ax - (1 - p) * 900
            elif s.get('vem_de') == 'baixo':
                ay = ay + (1 - p) * 700
            # balanço vivo: respira e balança a cabeça
            bal = s.get('balanco', 1.0)
            rot = bal * (3.0 * math.sin(ts * 2.4) + 1.5 * math.sin(ts * 5.3))
            ay += bal * 10 * math.sin(ts * 3.1)
            esc = s.get('escala', 1.0) * (1 + 0.02 * math.sin(ts * 2.0))
            if s.get('bote') and s['bote'][0] <= ts < s['bote'][0] + 0.35:
                q = (ts - s['bote'][0]) / 0.35
                ax += s['bote'][1] * math.sin(q * math.pi)
            im = B['im']
            if s.get('espelhar'):
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            # ancoragem: (ax, ay) é a posição do ponto 'ancora' do adesivo (em fração do adesivo)
            anc = s.get('ancora', (0.5, 0.5))
            iw, ih = im.width * esc, im.height * esc
            cx_img = ax + (0.5 - anc[0]) * iw
            cy_img = ay + (0.5 - anc[1]) * ih
            colar(frame, im, cx_img, cy_img, escala=esc, rot=rot)
            # pontos do olho / fosseta convertidos para o quadro
            def ponto(px, py):
                x2, y2 = B['conv'](px, py)
                if s.get('espelhar'):
                    x2 = im.width - x2
                dx, dy = (x2 - im.width / 2) * esc, (y2 - im.height / 2) * esc
                ang = math.radians(-rot)
                return cx_img + dx * math.cos(ang) - dy * math.sin(ang), cy_img + dx * math.sin(ang) + dy * math.cos(ang)
            s['_ponto'] = ponto
            b = B['b']
            if 'olho' in b:
                ox, oy = ponto(*b['olho'][:2])
                r = b['olho'][2] * B['esc'] * esc * b.get('olho_fator', 1.35)
                pis = 1.0 if ((ts + s.get('fase_piscar', 0)) % 2.6) < 0.13 else 0.0
                olhos_desenhar.append((ox, oy, r, pis, b.get('olhar', (0, 0))))
            for e in s.get('efeitos', []):
                te = ts - e['de']
                if te < 0 or ('ate' in e and te > e['ate'] - e['de']):
                    continue
                if e['tipo'] == 'anel':
                    fx, fy = ponto(*b['fosseta'])
                    ef_anel(frame, fx, fy, e.get('r', 45) * B['esc'] * esc, te)
                elif e['tipo'] == 'seta':
                    fx, fy = ponto(*b['fosseta'])
                    ef_seta(frame, fx + e['dx'], fy + e['dy'], fx + e.get('fx', 0), fy + e.get('fy', 0), te)
                elif e['tipo'] == 'calor':
                    fx, fy = ponto(*b['fosseta'])
                    ef_calor(frame, fx, fy, te, e.get('dir', -1))
                elif e['tipo'] == 'gotas':
                    fx, fy = ponto(*b['boca'])
                    ef_gotas(frame, fx, fy, te)
                elif e['tipo'] == 'rotulo':
                    fx, fy = ponto(*b['fosseta'])
                    lx, ly = e['x'], e['y']
                    p2 = ease(te / 0.3)
                    d = ImageDraw.Draw(frame)
                    d.line([(fx, fy), (fx + (lx - fx) * p2, fy + (ly - fy) * p2)], fill=(0, 0, 0, 255), width=12)
                    d.line([(fx, fy), (fx + (lx - fx) * p2, fy + (ly - fy) * p2)], fill=AMARELO + (255,), width=6)
                    if p2 > .9:
                        lab = texto_img(e['texto'], 50, (0, 0, 0), 0)
                        d.rounded_rectangle([lx - lab.width / 2 - 26, ly - 42, lx + lab.width / 2 + 26, ly + 42], radius=22, fill=AMARELO + (255,), outline=(0, 0, 0, 255), width=5)
                        colar(frame, lab, lx, ly)
        for ox, oy, r, pis, olhar in olhos_desenhar:
            colar(frame, olho(r, pis, olhar), ox, oy)

        # objetos e efeitos soltos
        for e in quando(R.get('efeitos', []), t):
            te = t - e['de']
            if e['tipo'] == 'objeto':
                ef_frasco(frame, extras[e['obj']], e['x'], e['y'], te, e.get('larg', 360))
            elif e['tipo'] == 'manometro':
                ef_manometro(frame, e['x'], e['y'], te / e.get('dur', 1.2), rotulo=e.get('rotulo', 'PRESSÃO'))
            elif e['tipo'] == 'x':
                ef_x(frame, e['x'], e['y'], e.get('s', 110), te)
            elif e['tipo'] == 'check':
                ef_check(frame, e['x'], e['y'], e.get('s', 110), te)
            elif e['tipo'] == 'gotas':
                ef_gotas(frame, e['x'], e['y'], te)

        # Onçômetro
        for o in quando(R.get('oncometro', []), t):
            al = min(1, (t - o['de']) / 0.25, (o['ate'] - t) / 0.25)
            oncometro(frame, o['nome'], o['valores'], o['barras_em'], t, al)

        # camada 3: frases que ficam e acumulam
        for f in quando(R.get('frases', []), t):
            tf = t - f['de']
            p = back(tf / 0.3)
            im = texto_img(f['texto'], f.get('tam', 74), tuple(f.get('cor', (255, 255, 255))), f.get('contorno', 9))
            colar(frame, im, f.get('x', 540), f['y'], escala=max(0.01, p), rot=f.get('rot', -3))
            if f.get('riscar') is not None and tf >= f['riscar']:
                q = ease((tf - f['riscar']) / 0.25)
                d = ImageDraw.Draw(frame)
                xa = f.get('x', 540) - im.width / 2; xb = xa + im.width * q
                d.line([(xa, f['y']), (xb, f['y'])], fill=VERMELHO + (255,), width=14)

        # camada 2: destaque gigante amarelo
        for g in quando(R.get('destaques', []), t):
            tg = t - g['de']
            p = back(tg / 0.28)
            im = texto_img(g['texto'], g.get('tam', 170), tuple(g.get('cor', AMARELO)), g.get('contorno', 15))
            colar(frame, im, g.get('x', 540), g['y'], escala=max(0.01, p), rot=g.get('rot', -4))

        # camada 1: legenda palavra a palavra no topo
        atual = None
        for pw in palavras:
            if pw['ini'] <= t < pw['fim'] + 0.05:
                atual = pw
        if atual:
            w = norm(atual['w'])
            cor = AMARELO if w in chaves else (255, 255, 255)
            pp = back((t - atual['ini']) / 0.12)
            colar(frame, texto_img(w, 66, cor, 8), 540, 330, escala=0.85 + 0.15 * max(0, min(1.1, pp)))

        rgb = frame.convert('RGB')
        if ff:
            ff.stdin.write(rgb.tobytes())
        else:
            rgb.save(os.path.join(a.quadros, f'{fi:04d}.jpg'), quality=88)
        if fi % 60 == 0:
            print(f'{t:5.1f}s', flush=True)
    if ff:
        ff.stdin.close(); ff.wait()


if __name__ == '__main__':
    main()
