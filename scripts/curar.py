import json, os, sys, urllib.request, urllib.parse

OUT = sys.argv[1]
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
UA = "FabricaDeVideos/1.0 (educational video project; contact via project repo)"

def get(url, params=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))

def download(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r, open(path, "wb") as f:
        f.write(r.read())
    return os.path.getsize(path)

creditos = []

# --- iNaturalist: Bothrops jararaca, so CC0 / CC BY, research grade ---
d = get("https://api.inaturalist.org/v1/observations", {
    "taxon_name": "Bothrops jararaca", "photo_license": "cc0,cc-by",
    "quality_grade": "research", "per_page": 60, "order_by": "votes"})
n = 0
seen = set()
for o in d.get("results", []):
    tx = (o.get("taxon") or {}).get("name")
    if tx != "Bothrops jararaca":
        continue
    for p in o.get("photos", []):
        lic = (p.get("license_code") or "").lower()
        if lic not in ("cc0", "cc-by"):
            continue
        if p["id"] in seen:
            continue
        seen.add(p["id"])
        url = p["url"].replace("square.", "original.").replace("/square", "/original")
        ext = os.path.splitext(urllib.parse.urlparse(url).path)[1] or ".jpg"
        name = f"inat-{p['id']}{ext}"
        try:
            size = download(url, os.path.join(OUT, "assets", name))
        except Exception as e:
            print("falhou", name, e); continue
        creditos.append({"arquivo": name, "banco": "iNaturalist", "id": str(p["id"]),
                         "autor": (p.get("attribution") or "").split(",")[0].replace("(c) ", "").strip(),
                         "licenca": lic.upper(), "link": f"https://www.inaturalist.org/observations/{o['id']}",
                         "especie": tx, "bytes": size})
        print("ok", name, size, lic)
        n += 1
        if n >= 10:
            break
    if n >= 10:
        break

# --- Pixabay: fundo de habitat e objetos, descartando IA ---
PX = os.environ["PIXABAY_API_KEY"]
def pixabay(q, kind, want):
    base = "https://pixabay.com/api/videos/" if kind == "video" else "https://pixabay.com/api/"
    pr = {"key": PX, "q": q, "per_page": 30, "safesearch": "true"}
    if kind == "photo":
        pr["image_type"] = "photo"
    try:
        d = get(base, pr)
    except Exception as e:
        print("pixabay falhou", q, e); return 0
    got = 0
    for h in d.get("hits", []):
        if h.get("isAiGenerated") or h.get("isLowQuality"):
            continue
        if kind == "video":
            url = h["videos"]["large"]["url"] or h["videos"]["medium"]["url"]
            ext = ".mp4"
        else:
            url = h.get("largeImageURL")
            ext = ".jpg"
        if not url:
            continue
        name = f"px-{q.replace(' ','_')}-{h['id']}{ext}"
        try:
            size = download(url, os.path.join(OUT, "assets", name))
        except Exception as e:
            print("falhou", name, e); continue
        creditos.append({"arquivo": name, "banco": "Pixabay", "id": str(h["id"]),
                         "autor": h.get("user"), "licenca": "Pixabay Content License",
                         "link": h.get("pageURL"), "especie": "-", "bytes": size,
                         "termo": q, "ia": bool(h.get("isAiGenerated"))})
        print("ok", name, size)
        got += 1
        if got >= want:
            break
    return got

pixabay("rainforest floor", "video", 2)
pixabay("jungle leaves", "video", 2)
pixabay("forest night", "video", 1)
pixabay("pills medicine", "photo", 3)
pixabay("blood pressure monitor", "photo", 2)

json.dump(creditos, open(os.path.join(OUT, "assets", "_creditos.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("TOTAL", len(creditos))
