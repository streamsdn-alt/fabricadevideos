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
BASE = Image.open(os.path.join(V, "_render", "out", "00012.jpg")).convert("RGB")

def capa(w, h, nome):
    im = BASE.copy()
    r = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    im = im.crop(((im.width - w) // 2, 0, (im.width - w) // 2 + w, h))
    im = ImageEnhance.Contrast(im).enhance(1.12)
    d = ImageDraw.Draw(im)
    big = ImageFont.truetype(F + "impact.ttf", int(w * 0.155))
    sml = ImageFont.truetype(F + "impact.ttf", int(w * 0.105))
    y = int(h * 0.80)
    d.text((w // 2, y), "VENENO", font=big, fill=(235, 50, 50),
           stroke_width=int(w * 0.011), stroke_fill=(0, 0, 0), anchor="mm")
    d.text((w // 2, y + int(w * 0.135)), "→ REMÉDIO", font=big, fill=(255, 232, 60),
           stroke_width=int(w * 0.011), stroke_fill=(0, 0, 0), anchor="mm")
    d.text((w // 2, int(h * 0.09)), "1981", font=sml, fill=(255, 255, 255),
           stroke_width=int(w * 0.009), stroke_fill=(0, 0, 0), anchor="mm")
    im.save(os.path.join(ENT, nome), quality=93)
    print("capa:", nome, im.size)

capa(1080, 1920, "ONC-001-capa-universal.jpg")
capa(1080, 1440, "ONC-001-capa-tiktok.jpg")

shutil.copy(os.path.join(V, "08-video.mp4"), os.path.join(ENT, "ONC-001-jararaca-remedio.mp4"))
print("mp4 copiado")
