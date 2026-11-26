import json, os, subprocess, sys, urllib.parse, urllib.request
from PIL import Image

OUT = sys.argv[1]; D = os.path.join(OUT, "assets", "fundos")
os.makedirs(D, exist_ok=True)
PX = os.environ["PIXABAY_API_KEY"]
UA = "FabricaDeVideos/1.0"

def get(url, p=None):
    if p: url += "?" + urllib.parse.urlencode(p)
    r = urllib.request.Request(url, headers={"User-Agent": UA})
    return json.loads(urllib.request.urlopen(r, timeout=60).read().decode())

def brilho(path):
    subprocess.run(["ffmpeg","-y","-v","error","-i",path,"-vf",
                    "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=1",
                    "-frames:v","6","-q:v","4", os.path.join(D,"_t%02d.jpg")], check=True)
    vs=[]
    for i in range(1,7):
        p=os.path.join(D,f"_t{i:02d}.jpg")
        if os.path.exists(p):
            im=Image.open(p).convert("L").resize((48,84))
            vs.append(sum(im.getdata())/(48*84)); os.remove(p)
    return sum(vs)/len(vs) if vs else 0

cands=[]
for q in ["tropical forest","rainforest","jungle","forest sunlight","green forest path","bamboo forest"]:
    try: d=get("https://pixabay.com/api/videos/", {"key":PX,"q":q,"per_page":20,"safesearch":"true"})
    except Exception as e: print("falhou",q,e); continue
    for h in d.get("hits",[]):
        if h.get("isAiGenerated") or h.get("isLowQuality"): continue
        v=h["videos"].get("large") or h["videos"].get("medium")
        if not v or not v.get("url"): continue
        if h.get("duration",0) < 6: continue
        cands.append((q,h["id"],h["user"],v["url"],h.get("duration"),h.get("pageURL")))

seen=set(); res=[]
for q,i,u,url,dur,page in cands:
    if i in seen: continue
    seen.add(i)
    p=os.path.join(D,f"bg-{i}.mp4")
    try:
        req=urllib.request.Request(url, headers={"User-Agent":UA})
        open(p,"wb").write(urllib.request.urlopen(req, timeout=180).read())
    except Exception as e:
        print("download falhou",i,e); continue
    if os.path.getsize(p) > 60_000_000:
        os.remove(p); continue
    b=brilho(p)
    res.append({"id":i,"termo":q,"autor":u,"brilho":round(b,1),"dur":dur,"arquivo":f"bg-{i}.mp4","link":page})
    print(f"bg-{i:<9} {q:<22} brilho {b:5.1f}  {dur}s  {u}")
    if len([r for r in res if r["brilho"]>=130]) >= 6: break

res.sort(key=lambda r:-r["brilho"])
json.dump(res, open(os.path.join(D,"_fundos.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("\nTOP 6 por brilho:")
for r in res[:6]: print("  ", r["arquivo"], r["brilho"], r["termo"])
