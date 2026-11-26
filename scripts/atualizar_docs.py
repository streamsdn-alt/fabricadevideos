import io, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fabrica-init"))
V = "onca-curiosa/ONC-001-jararaca-remedio"

# ---------------- 06-creditos.md
p = f"{V}/06-creditos.md"; s = io.open(p, encoding="utf-8").read()
velho = """| `px-jungle_leaves-183638.mp4` | Pixabay | 183638 | Mujibarsk_786 | Pixabay Content License | <https://pixabay.com/videos/id-183638/> |
| `px-forest_night-11721.mp4` | Pixabay | 11721 | Iconikmg | Pixabay Content License | <https://pixabay.com/videos/id-11721/> |
| `px-rainforest_floor-23.mp4` | Pixabay | 23 | DistillVideos | Pixabay Content License | <https://pixabay.com/videos/id-23/> |
| `px-pills_medicine-1539191.jpg` | Pixabay | 1539191 | stevepb | Pixabay Content License | <https://pixabay.com/photos/thermometer-medications-tablets-1539191/> |
| `px-pills_medicine-8287535.jpg` | Pixabay | 8287535 | kravaivan11 | Pixabay Content License | <https://pixabay.com/photos/medicine-pills-medication-bottle-8287535/> |
| `px-blood_pressure_monitor-1584223.jpg` | Pixabay | 1584223 | Bru-nO | Pixabay Content License | <https://pixabay.com/photos/blood-pressure-stethoscope-medical-1584223/> |"""
novo = """| `fundos/foto-9618231.jpg` | Pixabay | 9618231 | ignartonosbg | Pixabay Content License | <https://pixabay.com/photos/leaves-green-nature-plant-tree-9618231/> |
| `px-pills_medicine-8287535.jpg` | Pixabay | 8287535 | kravaivan11 | Pixabay Content License | <https://pixabay.com/photos/medicine-pills-medication-bottle-8287535/> |"""
assert velho in s, "tabela de creditos nao encontrada"
s = s.replace(velho, novo)

velho2 = s[s.index("## Observação sobre o termo de busca"):s.index("## Assets baixados e não usados")]
novo2 = """## O cenário (versão 2)

Agora o vídeo tem **um cenário só**, como manda o guia: `fundos/foto-9618231.jpg`, foto real de sub-bosque de mata — tronco com folhas grandes e luz entrando. **Brilho medido 117,6** antes de qualquer tratamento; no vídeo montado a média fica em **120,0**, acima do mínimo de 110.

Tratamento aplicado: realce de cor (1,14) e de contraste (1,08), mais um Ken Burns lento de 7%. **Não foi escurecido nem desfocado**, como a regra exige.

### Por que este e não outro

Foram baixados e medidos **91 candidatos** (6 vídeos e 85 fotos) do Pixabay. Os mais claros pelo número eram pássaro, neve e duna — brilho alto, conteúdo errado. Filtrando também por verde dominante sobraram poucos, e este foi o único com sub-bosque de mata real, claro, sem gente e sem objeto construído. Os descartados ficam registrados em `assets/fundos/_fotos.json` e `_fotos2.json`.

Os clipes e fotos da versão 1 (`px-jungle_leaves-183638.mp4`, `px-forest_night-11721.mp4`, `px-rainforest_floor-23.mp4`, `px-blood_pressure_monitor-1584223.jpg`, `px-pills_medicine-1539191.jpg`) **saíram do vídeo** — eram seis cenários diferentes e escurecidos. Ficam na pasta como registro.

"""
s = s.replace(velho2, novo2)
io.open(p, "w", encoding="utf-8").write(s)
print("06-creditos.md atualizado")

# ---------------- CLIPES-USADOS.md
p = "CLIPES-USADOS.md"; s = io.open(p, encoding="utf-8").read()
for linha in ["| Onça Curiosa | ONC-001 | 183638 | Pixabay | Mujibarsk_786 | Pixabay Content License | 2026-11-25 |\n",
              "| Onça Curiosa | ONC-001 | 11721 | Pixabay | Iconikmg | Pixabay Content License | 2026-11-25 |\n",
              "| Onça Curiosa | ONC-001 | 23 | Pixabay | DistillVideos | Pixabay Content License | 2026-11-25 |\n",
              "| Onça Curiosa | ONC-001 | 1539191 | Pixabay | stevepb | Pixabay Content License | 2026-11-25 |\n",
              "| Onça Curiosa | ONC-001 | 1584223 | Pixabay | Bru-nO | Pixabay Content License | 2026-11-25 |\n"]:
    s = s.replace(linha, "")
s = s.replace("| Onça Curiosa | ONC-001 | 8287535 | Pixabay | kravaivan11 | Pixabay Content License | 2026-11-25 |",
              "| Onça Curiosa | ONC-001 | 8287535 | Pixabay | kravaivan11 | Pixabay Content License | 2026-11-25 |\n| Onça Curiosa | ONC-001 | 9618231 | Pixabay | ignartonosbg | Pixabay Content License | 2026-11-25 |")
io.open(p, "w", encoding="utf-8").write(s)
print("CLIPES-USADOS.md atualizado")
