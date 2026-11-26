# ONC-001 — Avaliação

**Etapa 9.** Conferido no vídeo montado e na folha de quadros (`08-quadros.png`, um quadro a cada 2 s).
Aprova só com **todas as notas ≥ 8**.

## Notas

| Item | Nota | Por quê |
|---|---|---|
| Fidelidade | **9** | O texto enviado ao sintetizador bate palavra por palavra com o `03-roteiro.md`, nas 7 frases. Tira 1 porque a pronúncia não foi conferida de ouvido (sem transcrição automática no ambiente). |
| Imagem × tema | **8** | Nos 7 quadros em que a cobra aparece (0, 2, 4, 6, 8, 10, 16, 24, 26 s) é *Bothrops jararaca* identificada no iNaturalist. Nenhuma cobra genérica. Tira 2 pelo fundo da cena 7, um render 3D de fundo azul chapado que destoa do resto, e pelo clipe de "folhas" que na verdade é cachoeira. |
| Gancho | **9** | No frame 0 já estão a cabeça, o círculo vermelho na fosseta e o texto grande "ESSE BURACO VÊ CALOR". A parte estranha e o fato impossível aparecem juntos no 1º segundo. |
| Ritmo | **9** | 9 cenas em 26,53 s. A maior é a do Onçômetro (4,89 s) e ela tem 4 batidas internas. Nenhum trecho passa de 2,9 s sem mudança. Duração dentro de 25–30 s. |
| Técnica | **6** | **REPROVA.** Ver abaixo. |
| Licenças | **10** | Os 10 assets usados estão no `06-creditos.md` com banco, ID, autor, licença e link. Só CC BY e Pixabay. O asset com marca ("Tensoval") foi pego e trocado. |

## Técnica — por que reprova

1. **Sem trilha.** O guia pede música da Biblioteca de Áudio do YouTube a ~−24 dB abaixo da voz, abaixando sob a fala. A pasta `musicas/` está vazia e a regra proíbe música de qualquer outra fonte. O vídeo saiu com voz seca. **Isso sozinho já reprova.**
2. **A voz não é a do canal.** É a voz local do Windows (feminina, de sistema), usada só para o piloto não travar. A voz do canal é a masculina do ElevenLabs, bloqueada por falta da permissão `text_to_speech` na chave.
3. **Sem efeitos sonoros** nos efeitos visuais, pelo mesmo motivo do item 1.

O que está bom em técnica: loudness integrado **−15,6 LUFS**, pico **−1,3 dBTP** (sem estouro e sem corte), legenda sincronizada com a narração real, nada escrito acima de 165 px nem abaixo de 1755 px, nenhuma marca-d'água, nenhum texto cortado.

## Correções feitas antes desta avaliação

Duas voltas, dentro do limite do manual.

**1ª volta — 5 reprovações:**

| Cena / tempo | Problema | Correção |
|---|---|---|
| 14,0 s (cena 6) | **Marca "Tensoval" legível no aparelho de pressão.** Viola regra de marcas. | Trocado pelo asset 1584223 (estetoscópio, sem marca). |
| 0,0 s (cena 1) | O texto-gancho só entrava a partir de ~0,2 s. O guia exige **no frame 0**. | Passou a aparecer desde o primeiro quadro. |
| 8,0 s (cena 4) | A cobra ainda estava entrando e aparecia só um pedaço na borda. | Entrada acelerada, com easing, e cobra enquadrada. |
| 18,0 s (cena 8) | Rótulo "ONÇÔMETRO" desenhado **duas vezes** (legenda + rótulo da cena). | Rótulo removido; fica só a legenda. |
| 18,0–19,0 s (cena 8) | As 4 barras ficavam vazias no começo da cena. | Preenchimento começa no primeiro quadro da cena. |

**2ª volta — 1 reprovação:**

| Cena / tempo | Problema | Correção |
|---|---|---|
| 8,0–10,0 s e 16,0 s (cenas 4 e 7) | A cobra enrolada ocupa só **20% de pixels opacos** depois do recorte: no 9×16 ela vira um risco fino num fundo marrom vazio. | Trocada pela cabeça recortada, que preenche o quadro. Conferido na folha de quadros. |

## Resultado

**REPROVADO na etapa 9** — nota de Técnica 6, abaixo de 8.

Os dois motivos da reprova **dependem do dono**, não da equipe:

1. liberar a permissão `text_to_speech` na chave do ElevenLabs;
2. colocar ao menos uma trilha e alguns efeitos da Biblioteca de Áudio do YouTube na pasta `musicas/`.

Resolvidos os dois, é refazer só as etapas 7 e 8 (narração e montagem) — o roteiro, os fatos, as cenas e os assets já estão aprovados e não se mexe neles.

A pasta `Entrega/` foi montada mesmo assim, para o dono ver o piloto e julgar roteiro, corte e imagem. **Não é material publicável.**

## Riscos anotados

- Pronúncia de "Rraw!" e "fosseta loreal" não conferida de ouvido.
- Texto integral de Ferreira (1965) e Ondetti (1971) não lido (paywall). O roteiro não afirma nada além do que o registro primário do NCBI já diz.
