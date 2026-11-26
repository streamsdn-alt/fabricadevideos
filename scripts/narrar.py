"""ONC-001 - etapa 7: narracao no ElevenLabs com a voz do canal.

Regras do dono: SEMPRE a voz "daniel narrador" (ELEVENLABS_VOICE_ID),
modelo eleven_v4, velocidade +20%. Se o ElevenLabs falhar, PARA.
Nunca substituir por voz do Windows, Edge ou qualquer outra.
"""
import json, os, subprocess, sys, urllib.request, urllib.error

V = sys.argv[1]
MODEL = "eleven_v4"
SPEED = 1.2                      # +20%, como manda o GUIA-ONCA.md
AUD = os.path.join(V, "audio")
os.makedirs(AUD, exist_ok=True)
KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE = os.environ["ELEVENLABS_VOICE_ID"]
VOZ_ESPERADA = "daniel narrador"

def api(path, data=None, raw=False, timeout=180):
    h = {"xi-api-key": KEY}
    if data is not None:
        h["Content-Type"] = "application/json"
        data = json.dumps(data).encode()
    r = urllib.request.Request("https://api.elevenlabs.io" + path, data=data, headers=h)
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        return resp.read() if raw else json.loads(resp.read().decode())

# ---- 1. confere que o ID do ambiente e mesmo a voz certa (sem mostrar a chave)
try:
    v = api(f"/v1/voices/{VOICE}")
except urllib.error.HTTPError as e:
    print("PARADA: nao consegui ler a voz.", e.code, e.read()[:300].decode("utf-8", "replace"))
    sys.exit(1)
nome = (v.get("name") or "").strip()
print(f"voz do ambiente: {nome!r} | {v.get('labels')}")
if nome.lower() != VOZ_ESPERADA:
    print(f"PARADA: o ELEVENLABS_VOICE_ID aponta para {nome!r}, e nao para {VOZ_ESPERADA!r}.")
    sys.exit(1)
print("conferido: e a voz do canal.")

antes = api("/v1/user/subscription")
print("saldo antes:", antes["character_count"], "/", antes["character_limit"])

FRASES = json.load(open(os.path.join(AUD, "_frases.json"), encoding="utf-8"))

def dur(p):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(o.stdout.strip())

chars = 0
for i, f in enumerate(FRASES, 1):
    body = {"text": f, "model_id": MODEL,
            "voice_settings": {"stability": 0.45, "similarity_boost": 0.8,
                               "style": 0.3, "use_speaker_boost": True, "speed": SPEED}}
    try:
        mp3 = api(f"/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128", body, raw=True)
    except urllib.error.HTTPError as e:
        print(f"PARADA na frase {i}: HTTP {e.code} {e.read()[:400].decode('utf-8','replace')}")
        print("Etapa 7 interrompida. Nao vou substituir por outra voz.")
        sys.exit(1)
    p_mp3 = os.path.join(AUD, f"el{i}.mp3")
    open(p_mp3, "wb").write(mp3)
    p_wav = os.path.join(AUD, f"el{i}.wav")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", p_mp3, "-ar", "44100", "-ac", "1", p_wav],
                   check=True)
    chars += len(f)
    print(f"f{i}: {dur(p_wav):5.2f}s  {len(f.split()):2d} pal  {len(f)} chars")

depois = api("/v1/user/subscription")
gasto = depois["character_count"] - antes["character_count"]
print("chars enviados:", chars, "| GASTO REAL:", gasto)
print("saldo depois:", depois["character_count"], "/", depois["character_limit"])
json.dump({"modelo": MODEL, "speed": SPEED, "voz": nome,
           "chars_enviados": chars, "gasto_creditos": gasto,
           "saldo_antes": antes["character_count"], "saldo_depois": depois["character_count"],
           "limite": depois["character_limit"]},
          open(os.path.join(AUD, "_eleven.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
