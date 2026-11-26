# ONC-001 — Créditos e licenças

**Etapa 6.** Todo asset baixado por API oficial. Nenhum site raspado. Pexels não acessado.

## Assets usados no vídeo

| Arquivo | Banco | ID | Autor | Licença | Link |
|---|---|---|---|---|---|
| `inat-348275825.jpg` | iNaturalist | 348275825 | Pedro Alvaro Neves | **CC BY** | <https://www.inaturalist.org/observations/196328139> |
| `inat-348275850.jpg` | iNaturalist | 348275850 | Pedro Alvaro Neves | **CC BY** | <https://www.inaturalist.org/observations/196328139> |
| `inat-348275873.jpg` | iNaturalist | 348275873 | Pedro Alvaro Neves | **CC BY** | <https://www.inaturalist.org/observations/196328139> |
| `inat-348275890.jpg` | iNaturalist | 348275890 | Pedro Alvaro Neves | **CC BY** | <https://www.inaturalist.org/observations/196328139> |
| `fundos/foto-9618231.jpg` | Pixabay | 9618231 | ignartonosbg | Pixabay Content License | <https://pixabay.com/photos/leaves-green-nature-plant-tree-9618231/> |
| `px-pills_medicine-8287535.jpg` | Pixabay | 8287535 | kravaivan11 | Pixabay Content License | <https://pixabay.com/photos/medicine-pills-medication-bottle-8287535/> |

**Atribuição obrigatória na descrição do vídeo:** as quatro fotos da jararaca são CC BY de **Pedro Alvaro Neves** (iNaturalist). Pixabay não exige atribuição, mas os autores vão creditados do mesmo jeito.

Nenhum asset veio marcado como gerado por IA (`isAiGenerated = false` em todos os resultados do Pixabay; os do iNaturalist são fotos de observação de campo, com identificação de grau de pesquisa).

## Espécie — conferência

As quatro imagens do bicho são de observações identificadas como ***Bothrops jararaca*** em grau de pesquisa no iNaturalist. **Nenhuma cobra genérica entrou no vídeo.** O Pixabay foi usado só para fundo e objeto.

## Asset reprovado

| Arquivo | Motivo |
|---|---|
| `px-blood_pressure_monitor-867855.jpg` | **Marca visível no aparelho ("Tensoval").** Viola a regra de não usar logo nem marca. Trocado por `px-blood_pressure_monitor-1584223.jpg`, que não tem marca legível. Arquivo mantido na pasta como registro da reprovação, **proibido de usar**. |

## O cenário (versão 2)

Agora o vídeo tem **um cenário só**, como manda o guia: `fundos/foto-9618231.jpg`, foto real de sub-bosque de mata — tronco com folhas grandes e luz entrando. **Brilho medido 117,6** antes de qualquer tratamento; no vídeo montado a média fica em **120,0**, acima do mínimo de 110.

Tratamento aplicado: realce de cor (1,14) e de contraste (1,08), mais um Ken Burns lento de 7%. **Não foi escurecido nem desfocado**, como a regra exige.

### Por que este e não outro

Foram baixados e medidos **91 candidatos** (6 vídeos e 85 fotos) do Pixabay. Os mais claros pelo número eram pássaro, neve e duna — brilho alto, conteúdo errado. Filtrando também por verde dominante sobraram poucos, e este foi o único com sub-bosque de mata real, claro, sem gente e sem objeto construído. Os descartados ficam registrados em `assets/fundos/_fotos.json` e `_fotos2.json`.

Os clipes e fotos da versão 1 (`px-jungle_leaves-183638.mp4`, `px-forest_night-11721.mp4`, `px-rainforest_floor-23.mp4`, `px-blood_pressure_monitor-1584223.jpg`, `px-pills_medicine-1539191.jpg`) **saíram do vídeo** — eram seis cenários diferentes e escurecidos. Ficam na pasta como registro.

## Assets baixados e não usados

Ficam na pasta `assets/` para reaproveitamento interno deste vídeo, e **não entram** no `CLIPES-USADOS.md` (o bloqueio de 60 dias vale para o que foi ao ar):

`inat-345617884`, `inat-461869666`, `inat-461869667`, `inat-461869680`, `inat-461869681`, `inat-461869693`, `px-pills_medicine-1853400`.

Os dois clipes grandes do Pixabay baixados e descartados (`px-rainforest_floor-216134.mp4`, 155 MB, e `px-jungle_leaves-122802.mp4`, 131 MB) foram **apagados** para não inchar o repositório. São redownloadáveis pelos IDs.

## Trilha

**A pasta `musicas/` está vazia.** O vídeo saiu **sem trilha**. Não foi usada música de nenhuma outra fonte. Ver a pendência no `09-avaliacao.md`.
