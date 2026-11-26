# GUIA-ONCA.md — Onça Curiosa (@oncacuriosabr)

> Guia de estilo do canal. Lido junto com `MANUAL-FABRICA.md` antes de qualquer trabalho.

## Pautas

- Pode repetir bicho, **nunca o fato**. Mínimo de 2 semanas entre vídeos do mesmo animal.
- Fatos já usados estão em `FATOS-USADOS.md`. Em bicho repetido, se não tiver certeza de que o fato é novo, **perguntar ao dono**.
- Antes de aprovar, conferir imagem real suficiente do bicho nos bancos. **Sem imagem boa, troca o bicho.**

## Roteiro

- **25 a 30 s** (~65 a 80 palavras), 6 ou 7 frases curtas, no máximo **3 fatos**. Acima de ~32 s é reprovado.
- **1º segundo:** parte estranha do bicho + fato "impossível"; texto-gancho grande no frame 0.
- Comparação com o dia a dia (tomada, ar-condicionado, canudinho, GPS).
- **Penúltima frase: Onçômetro** (Velocidade, Força, Estranheza, Perigo).
- **Última frase:** rugido curto + retoma o gancho (final em loop).
- Números por extenso. Pergunta fácil para o comentário fixado.

## Visual por camadas (Python + ffmpeg, 1080x1920)

- **Fundo:** habitat real (vídeo/foto dos bancos).
- **Bicho** recortado da foto real com `rembg`, andando com balanço de passo, entrando e saindo.
- **Olhos de desenho:** de perfil UM olho, de frente dois; estilo próprio por bicho; todos piscam.
- **Efeitos:** zoom de impacto, tremida, números gigantes, X vermelho, confete, tela dividida, velocímetro.
- **Legenda** palavra por palavra no topo; nada importante nos ~165 px de cima e de baixo.
- Mudança visual a cada **2 a 4 s**.
- Shorts **SEM** a oncinha.

## Áudio

- ElevenLabs, voz do `ELEVENLABS_VOICE_ID`, velocidade **+20%**; ~3 palavras/s.
- Pausas internas **0,07 s**; **0,02 a 0,03 s** entre frases; `atempo 1,10`.
- Trilha da pasta `musicas/` a cerca de **−24 dB** abaixo da voz, abaixando sob a fala.
- Efeitos sonoros nos efeitos visuais.

## Entrega

- MP4 **1080x1920**.
- **Capa universal** (mínimo de palavras: números, nomes, símbolos, onomatopeias).
- **Capa TikTok 1080x1440**.
- **SRT PT/EN/ES**.
- `POSTAGEM.md` com título, descrição, hashtags (`curiosidades`, `animais`, `natureza` + 2 do tema), fontes, créditos e horário sugerido (**12h ou 19h**).
