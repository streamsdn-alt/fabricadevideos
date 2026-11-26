# Modelo de montagem da Onça Curiosa

Feito a partir dos 3 vídeos de referência e do ANALISE-ESTILO.md. Exemplo pronto: `ONC-001-modelo.mp4` (jararaca, 31,6 s, voz Daniel narrador, brilho médio 132).

## Como usar (Luna)
```
pip install pillow numpy opencv-python
python onca_render.py ONC-001.json saida.mp4          # vídeo final
python onca_render.py ONC-001.json x.mp4 --ate 3      # teste rápido dos 3 primeiros segundos
python onca_render.py ONC-001.json x --quadros pasta/ # salva os quadros em vez do vídeo
```
Precisa do `ffmpeg` no PATH. Leva cerca de 40 s por vídeo.

## O que o modelo já faz sozinho
- Um cenário só; a "câmera" muda o enquadramento (cortes secos + zoom lento + tremida opcional).
- Bicho como adesivo: contorno branco, sombra, balanço, respiração, bote, entrada pela lateral. O lado onde a foto foi cortada fica fora da tela (`cortado`).
- Olho de desenho com anel amarelo, pupila olhando para a frente, pisca a cada ~2,6 s.
- 3 camadas de texto: legenda palavra a palavra no topo (palavras-chave em amarelo), `destaques` gigantes no meio, `frases` que ficam e acumulam (com opção de riscar).
- Onçômetro como painel sobre a cena, com o nome do bicho e barras enchendo uma a uma no tempo da fala.
- Efeitos desenhados: anel pulsando, seta, rótulo com linha, ondas de calor, gotas de veneno, manômetro, X vermelho, check verde, raios de sol, objeto entrando (adesivo).

## O que muda a cada vídeo
Só o JSON: cenário, adesivos (com a posição do olho na foto), câmera, cenas do bicho, textos, efeitos e Onçômetro. Os tempos vêm do `_timeline.json` da Paula (as palavras são distribuídas dentro de cada frase).

## Limites conhecidos
- `fundo_mata.py` desenha um cenário de mata em código. É claro e no estilo, mas mais simples que os cenários pintados do canal. Com imagem gerada (Gemini/Leonardo), troque só o `fundo`.
- O bicho só balança: pose que muda (correr, nadar) precisa de vários recortes do mesmo bicho.
- Sem trilha nem efeitos sonoros: a pasta `musicas/` está vazia.

Fonte: Montserrat Black (SIL Open Font License).
