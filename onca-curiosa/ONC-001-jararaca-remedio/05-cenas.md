# ONC-001 — Plano de cenas

**Etapa 5.** Tempos medidos na narração real (`audio/_timeline.json`), não estimados.
Duração total: **26,52 s**. Canvas 1080×1920. Área segura: nada importante acima de 165 px nem abaixo de 1755 px.

## Faixas do canvas

| Faixa | y | Uso |
|---|---|---|
| 0–165 | topo | **proibido** (interface) |
| 165–480 | legenda | legenda palavra por palavra |
| 480–1500 | imagem | bicho e cenário |
| 1500–1755 | efeito | números gigantes, Onçômetro, rótulos |
| 1755–1920 | rodapé | **proibido** (interface) |

## Cenas

| # | Entra | Sai | Dur | Frase | Camadas | Bicho / ação | Efeito | Termo de busca |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,00 | 2,58 | 2,58 | 1 | fundo folhas escurecido + cabeça recortada + marcador na fosseta + texto-gancho | *Bothrops jararaca*, cabeça de perfil, língua para fora | zoom de impacto + círculo vermelho pulsando na fosseta | `Bothrops jararaca head` / `cabeça de jararaca` |
| 2 | 2,61 | 5,05 | 2,44 | 2a | fundo folhas + cabeça recortada + rótulo com linha + olho de desenho | mesma cabeça, outro ângulo; olho pisca | rótulo "FOSSETA LOREAL" entrando por deslize | `Bothrops jararaca close-up` / `jararaca de perto` |
| 3 | 5,05 | 7,48 | 2,43 | 2b | fundo floresta à noite + cobra em falsa-cor térmica + linhas de varredura | cobra vista "pelo calor" | falsa-cor térmica + varredura + rótulo "CÂMERA TÉRMICA" | `forest night` / `floresta à noite` |
| 4 | 7,51 | 10,35 | 2,84 | 3 | fundo chão de mata + cobra enrolada entrando pela esquerda com balanço de passo | *Bothrops jararaca* enrolada, entra e para | tremida de impacto + palavra "VENENO" em vermelho | `Bothrops jararaca coiled` / `jararaca enrolada` + `rainforest floor` |
| 5 | 10,37 | 12,60 | 2,23 | 4a | foto de comprimidos com zoom lento + número gigante | — | número "1981" batendo na tela | `pills medicine` / `comprimidos remédio` |
| 6 | 12,60 | 14,75 | 2,15 | 4b | foto de aparelho de pressão com zoom lento + seta | — | seta caindo + "PRESSÃO" | `blood pressure monitor` / `aparelho de pressão` |
| 7 | 14,77 | 17,96 | 3,19 | 5 | **tela dividida**: cobra à esquerda, comprimido à direita | cobra parada à esquerda | X vermelho sobre a cobra, check sobre o comprimido | — (reaproveita assets das cenas 4 e 5) |
| 8 | 17,99 | 22,88 | 4,89 | 6 | fundo escuro + silhueta da cobra + 4 barras do Onçômetro | silhueta ao fundo | barras preenchendo **uma a cada ~1,2 s** (4 mudanças visuais dentro da cena) | — |
| 9 | 22,90 | 26,52 | 3,62 | 7 | fundo folhas (volta ao da cena 1) + cabeça recortada + texto-gancho de novo | cabeça de perfil, fecha em loop | flash + confete + retomada do gancho | `Bothrops jararaca head` / `cabeça de jararaca` |

**Mudança visual:** a maior cena é a 8, com 4,89 s, e ela tem quatro batidas internas (uma barra por vez). Nenhuma cena fica mais de 2,9 s sem mudar. Dentro da regra de 2 a 4 s.

## Espécie — regra firme desta pauta

O fato depende da fosseta loreal da jararaca. **Só serve imagem identificada como *Bothrops jararaca*.** Cobra genérica do Pixabay está proibida nas cenas 1, 2, 3, 4, 7 e 9. O bicho vem do iNaturalist, onde a identificação é de grau de pesquisa. Pixabay só entra em fundo (folhas, floresta, chão) e objeto (comprimido, aparelho de pressão).

## Coordenadas de referência (recorte `inat-348275825`, 1400×933)

- **Fosseta loreal:** centro (610, 310), raio ~48 px — é o buraco que o vídeo inteiro aponta.
- **Olho:** centro (790, 265), raios 75 × 62 — onde entra o olho de desenho.
- A cobra está de perfil, virada para a esquerda → **UM olho de desenho**, como manda o guia.

## Aviso para a montagem

- A pasta `musicas/` está vazia. Sem trilha da Biblioteca de Áudio do YouTube, a cena não leva música. **Não substituir por música de outra fonte.**
- A narração entregue na etapa 7 é voz local de rascunho (ver `07-custo.md`). O corte de cenas usa os tempos dessa voz; se a voz definitiva mudar a duração das frases, as cenas são replanejadas antes da montagem final.
