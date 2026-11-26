import json, os, sys, urllib.request, subprocess

OUT = sys.argv[1]
os.makedirs(os.path.join(OUT, "audio"), exist_ok=True)
KEY = os.environ["ELEVENLABS_API_KEY"]; VOICE = os.environ["ELEVENLABS_VOICE_ID"]

FRASES = [
 "Esse buraco na cara da jararaca enxerga calor.",
 "É a fosseta loreal, que toda víbora tem: acha a presa pelo calor, como câmera térmica.",
 "Mais estranho ainda: o veneno dela derruba a pressão.",
 "Dele saiu o captopril, remédio de pressão aprovado em mil novecentos e oitenta e um.",
 "Ninguém toma veneno: o remédio foi desenhado a partir dele.",
 "Onçômetro: velocidade seis, força quatro, estranheza dez, perigo nove.",
 "Rraw! Um buraco que vê calor, e um veneno que virou remédio.",
]

def saldo():
    req = urllib.request.Request("https://api.elevenlabs.io/v1/user/subscription", headers={"xi-api-key": KEY})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode())
    return d["character_count"], d["character_limit"]

antes = saldo()
print("saldo antes:", antes[0], "/", antes[1])

def dur(p):
    o = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
                       capture_output=True, text=True)
    return float(o.stdout.strip())

total_chars = 0
info = []
for i, f in enumerate(FRASES, 1):
    body = json.dumps({"text": f, "model_id": "eleven_multilingual_v2",
                       "voice_settings": {"stability": 0.45, "similarity_boost": 0.8,
                                          "style": 0.35, "use_speaker_boost": True, "speed": 1.2}}).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128",
        data=body, headers={"xi-api-key": KEY, "Content-Type": "application/json"})
    mp3 = os.path.join(OUT, "audio", f"f{i}.mp3")
    try:
        with urllib.request.urlopen(req, timeout=180) as r, open(mp3, "wb") as fh:
            fh.write(r.read())
    except urllib.error.HTTPError as e:
        print("ERRO", i, e.code, e.read()[:300]); sys.exit(1)
    wav = os.path.join(OUT, "audio", f"f{i}.wav")
    subprocess.run(["ffmpeg","-y","-v","error","-i",mp3,"-ar","44100","-ac","1",wav], check=True)
    d = dur(wav)
    pal = len(f.split())
    total_chars += len(f)
    info.append({"n": i, "texto": f, "palavras": pal, "chars": len(f), "dur": round(d, 3),
                 "pal_s": round(pal / d, 2)})
    print(f"f{i}: {d:.2f}s  {pal} pal  {pal/d:.2f} pal/s  {len(f)} chars")

depois = saldo()
soma = sum(x["dur"] for x in info)
print("soma das frases:", round(soma, 2), "s")
print("saldo depois:", depois[0], "/", depois[1])
print("GASTO REAL:", depois[0] - antes[0], "caracteres")
json.dump({"frases": info, "soma_frases_s": round(soma, 3), "chars_enviados": total_chars,
           "gasto_creditos": depois[0] - antes[0], "saldo_antes": antes[0], "saldo_depois": depois[0],
           "limite": depois[1]},
          open(os.path.join(OUT, "audio", "_narracao.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
