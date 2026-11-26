import json, os, sys, urllib.parse, urllib.request
from PIL import Image
OUT=sys.argv[1]; D=os.path.join(OUT,"assets","fundos"); os.makedirs(D,exist_ok=True)
PX=os.environ["PIXABAY_API_KEY"]; UA="FabricaDeVideos/1.0"
def get(u,p=None):
    if p: u+="?"+urllib.parse.urlencode(p)
    return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=60).read().decode())
def brilho(p):
    im=Image.open(p).convert("RGB")
    r=max(1080/im.width,1920/im.height)
    im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x=(im.width-1080)//2; im=im.crop((x,0,x+1080,1920)).convert("L").resize((54,96))
    return sum(im.getdata())/(54*96)
res=[];seen=set()
TERMOS=["forest floor leaves","jungle undergrowth","rainforest understory","tropical forest green",
        "forest path sunlight","green jungle leaves","atlantic forest brazil","fern forest"]
for q in TERMOS:
    try: d=get("https://pixabay.com/api/",{"key":PX,"q":q,"image_type":"photo","orientation":"vertical","per_page":12,"safesearch":"true","min_width":1080})
    except Exception as e: print("falhou",q,e); continue
    for h in d.get("hits",[]):
        if h.get("isAiGenerated") or h.get("isLowQuality") or h["id"] in seen: continue
        seen.add(h["id"])
        p=os.path.join(D,f"foto-{h['id']}.jpg")
        try: open(p,"wb").write(urllib.request.urlopen(urllib.request.Request(h["largeImageURL"],headers={"User-Agent":UA}),timeout=120).read())
        except Exception as e: print("dl falhou",h["id"],e); continue
        b=brilho(p)
        res.append({"id":h["id"],"termo":q,"autor":h["user"],"brilho":round(b,1),
                    "arquivo":os.path.basename(p),"link":h["pageURL"],"w":h["imageWidth"],"h":h["imageHeight"]})
res.sort(key=lambda r:-r["brilho"])
json.dump(res,open(os.path.join(D,"_fotos.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(f"{len(res)} fotos. TOP 10 por brilho:")
for r in res[:10]: print(f"  {r['arquivo']:<18} br {r['brilho']:5.1f}  {r['termo']:<26} {r['w']}x{r['h']}  {r['autor']}")
