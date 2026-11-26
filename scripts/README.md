# scripts/

Ferramentas da produção. Python + ffmpeg, tudo local e grátis.

| Script | Etapa | O que faz |
|---|---|---|
| `curar.py` | 6 | baixa assets do iNaturalist (CC0/CC BY) e do Pixabay (descartando IA), grava `_creditos.json` |
| `narrar.py` | 7 | narração pelo ElevenLabs; mede duração e registra o gasto de créditos |
| `narrar-local.ps1` | 7 | **rascunho**: voz local do Windows (pt-BR), grátis, para quando o ElevenLabs estiver indisponível |
| `montar.py` | 8 | montagem por camadas: fundo, recorte, olhos de desenho, efeitos, legenda palavra por palavra |
| `embalar.py` | 9 | SRT PT/EN/ES, capa universal, capa TikTok, pasta `Entrega/` |

Uso: `python -I scripts/<script>.py <canal>/<ONC-NNN-tema>`

Dependências: `python -m pip install rembg[cpu] pillow` e ffmpeg no PATH.
