"""ONC-001 - etapa 9: SRT PT/EN/ES, capas e pasta Entrega/."""
import json, os, shutil, sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

V = sys.argv[1]
ENT = os.path.join(V, "Entrega")
os.makedirs(ENT, exist_ok=True)
TL = json.load(open(os.path.join(V, "audio", "_timeline.json"), encoding="utf-8"))
F = "C:/Windows/Fonts/"

EN = ["That hole on the jararaca's face sees heat.",
      "It's the loreal pit, which every pit viper has: it finds prey by heat, like a thermal camera.",
      "Stranger still: its venom brings blood pressure down.",
      "From it came captopril, a blood pressure drug approved in nineteen eighty-one.",
      "Nobody drinks venom: the drug was designed from it.",
      "Jaguar-meter: speed six, strength four, weirdness ten, danger nine.",
      "Rraw! A hole that sees heat, and a venom that became medicine."]
ES = ["Ese hoyo en la cara de la jararaca ve calor.",
      "Es la fosa loreal, que toda víbora tiene: encuentra a su presa por el calor, como una cámara térmica.",
      "Más raro todavía: su veneno baja la presión.",
      "De él salió el captopril, un remedio para la presión aprobado en mil novecientos ochenta y uno.",
      "Nadie toma veneno: el remedio fue diseñado a partir de él.",
      "Onzómetro: velocidad seis, fuerza cuatro, rareza diez, peligro nueve.",
      "¡Rraw! Un hoyo que ve calor, y un veneno que se volvió remedio."]

def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")

def srt(path, linhas):
    out = []
    for i, fr in enumerate(TL["frases"]):
        out.append(f"{i+1}\n{ts(fr['ini'])} --> {ts(fr['fim'])}\n{linhas[i]}\n")
    open(path, "w", encoding="utf-8").write("\n".join(out))
    print("srt:", os.path.basename(path))

srt(os.path.join(ENT, "ONC-001-pt.srt"), [f["texto"] for f in TL["frases"]])
srt(os.path.join(ENT, "ONC-001-en.srt"), EN)
srt(os.path.join(ENT, "ONC-001-es.srt"), ES)

# ------------------------------------------------------------------ capas
# A capa e composta do zero (fundo + bicho + olho), nao reaproveita quadro
# do video: quadro ja tem as 3 camadas de texto e a capa pede poucas palavras.
import sys as _sys
_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def comp_capa(w, h, nome):
    bgp = os.path.join(V, "assets", "fundos", "foto-9618231.jpg")
    im = Image.open(bgp).convert("RGB")
    r = max(w / im.width, h / im.height) * 1.04
    im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    x = (im.width - w) // 2; y = int((im.height - h) * 0.45)
    im = im.crop((x, y, x + w, y + h))
    im = ImageEnhance.Color(im).enhance(1.14)
    im = ImageEnhance.Contrast(im).enhance(1.08).convert("RGBA")

    sn = Image.open(os.path.join(V, "assets", "_capa-bicho.png")).convert("RGBA")
    alt = int(h * 0.30)
    rr = alt / sn.height
    sn = sn.resize((int(sn.width * rr), alt), Image.LANCZOS)
    ox = (w - sn.width) // 2; oy = int(h * 0.955) - sn.height
    im.alpha_composite(sn, (ox, oy))

    d = ImageDraw.Draw(im)
    # olho de desenho com anel amarelo (assinatura do canal)
    sc = sn.width / Image.open(os.path.join(V, "assets", "_capa-bicho.png")).width
    meta = json.load(open(os.path.join(V, "assets", "_capa-bicho.json"), encoding="utf-8"))
    ex, ey = ox + int(meta["olho"][0] * sc), oy + int(meta["olho"][1] * sc)
    px, py = ox + int(meta["pit"][0] * sc), oy + int(meta["pit"][1] * sc)
    ra = int(w * 0.082)
    d.ellipse([ex-ra, ey-ra, ex+ra, ey+ra], fill=(250,213,11), outline=(20,16,8), width=6)
    ri = int(ra*0.76)
    d.ellipse([ex-ri, ey-ri, ex+ri, ey+ri], fill=(246,240,238), outline=(20,16,8), width=5)
    pr = int(ri*0.52)
    d.ellipse([ex-pr, ey-pr, ex+pr, ey+pr], fill=(18,14,10))
    d.ellipse([ex-pr, ey-pr, ex-pr+pr//2, ey-pr+pr//2], fill=(255,255,255))
    # anel na fosseta
    rp = int(w * 0.055)
    d.ellipse([px-rp, py-rp, px+rp, py+rp], outline=(250,213,11), width=10)
    d.ellipse([px-rp-10, py-rp-10, px+rp+10, py+rp+10], outline=(0,0,0), width=5)

    big = ImageFont.truetype(F + "impact.ttf", int(w * 0.175))
    st = int(w * 0.013)
    d.text((w//2, int(h*0.17)), "VENENO", font=big, fill=(229,57,53),
           stroke_width=st, stroke_fill=(0,0,0), anchor="mm")
    d.text((w//2, int(h*0.17) + int(w*0.155)), "→ REMÉDIO", font=big, fill=(245,221,11),
           stroke_width=st, stroke_fill=(0,0,0), anchor="mm")
    im.convert("RGB").save(os.path.join(ENT, nome), quality=93)
    print("capa:", nome, (w, h))

comp_capa(1080, 1920, "ONC-001-capa-universal.jpg")
comp_capa(1080, 1440, "ONC-001-capa-tiktok.jpg")

shutil.copy(os.path.join(V, "08-video.mp4"), os.path.join(ENT, "ONC-001-jararaca-remedio.mp4"))
print("mp4 copiado")
