# ONC-001 — Avaliação (versão 2, estilo oficial)

**Etapa 9.** Conferido no vídeo montado e na folha de quadros (`08-quadros.png`).
Aprova só com **todas as notas ≥ 8**. Critérios novos do `GUIA-ONCA.md` de 25/11/2026.

## Notas

| Item | Nota | Por quê |
|---|---|---|
| Fidelidade | **9** | O texto enviado ao ElevenLabs bate palavra por palavra com o `03-roteiro.md`, nas 7 frases. Tira 1 porque a pronúncia não foi conferida de ouvido — não há transcrição automática neste ambiente. |
| Imagem × tema | **9** | Em todos os planos com bicho é *Bothrops jararaca* identificada no iNaturalist. Tira 1 porque entre 14 s e 20 s o recorte dos comprimidos encosta na cabeça da cobra e o quadro fica apertado. |
| Gancho | **10** | No quadro 0 já estão a cabeça, o anel amarelo na fosseta, a seta e o texto-gancho **em tamanho cheio** — não entra crescendo. |
| Ritmo | **9** | 8 beats em 31,63 s. O maior é o do Onçômetro, com 5,43 s, mas ele tem 4 batidas internas (uma barra a cada ~0,8 s), igual ao canal, que segura o painel de 5 a 6 s. Nenhum trecho passa de ~1,9 s sem mudança. |
| **Estilo do canal** | **10** | 8 de 8 itens medíveis passam. Tabela abaixo. |
| Técnica | **6** | **REPROVA.** Ver abaixo. |
| Licenças | **10** | Todos os assets usados estão no `06-creditos.md` com banco, ID, autor, licença e link. Só CC BY e Pixabay. |

## Os 8 itens medíveis do estilo

| # | Item | Exigência | Medido | |
|---|---|---|---|---|
| 1 | Brilho médio | ≥ 110 | **120,0** (mín. 60,4 na cartela final, máx. 128,8) | ✅ |
| 2 | Um cenário só | 1 | **1** — `foto-9618231.jpg`, do início ao fim, com Ken Burns lento | ✅ |
| 3 | Bicho 20–30% da altura, terço inferior | 20–30% | **26,0%** (500 px de 1920), base em y = 1830 | ✅ |
| 4 | Contorno branco de adesivo | em todo recorte | cobra e comprimidos, 13 px | ✅ |
| 5 | Olho de desenho com anel amarelo | maior parte dos planos | **7 de 7** beats com bicho | ✅ |
| 6 | 3 camadas de texto | 3 | legenda topo sem caixa (chave em amarelo) + destaque gigante amarelo + frase que acumula | ✅ |
| 7 | Onçômetro painel sobre a cena com nome do bicho | sim | painel de 876 px sobre o cenário, cobra visível abaixo, "JARARACA" no cabeçalho | ✅ |
| 8 | Efeitos desenhados | nada de filtro | cone de calor vetorial, anel + seta na fosseta, carimbo "VENENO", X vermelho, check verde, "1981" gigante, silhueta de cupinzeiro | ✅ |

Duração: **31,63 s** — dentro de 28 a 33 s, bem abaixo do corte de 36 s.

## Técnica — por que ainda reprova

**Um motivo só, e é o mesmo da versão anterior: o vídeo saiu sem trilha.**

A pasta `musicas/` continua com apenas o `README.md`. O guia manda trilha da Biblioteca de Áudio do YouTube a ~−24 dB abaixo da voz, abaixando sob a fala, mais efeitos sonoros nos efeitos visuais. A regra proíbe música de qualquer outra fonte, então o vídeo foi entregue com voz seca.

O resto de técnica está bom: loudness integrado **−15,3 LUFS**, pico **−1,3 dBTP** (sem estouro e sem corte), legenda sincronizada com a narração real, nada escrito acima de 165 px nem abaixo de 1755 px, sem marca-d'água e sem texto cortado.

## Correções feitas antes desta avaliação

Duas voltas, dentro do limite do manual.

**1ª volta — 5 reprovações:**

| Cena / tempo | Problema | Correção |
|---|---|---|
| 10 s (beat "veneno") | **O recorte virou uma mancha branca.** O alfa fantasma do corpo semitransparente foi engordado pelo contorno de adesivo e cobriu a cobra. | `limpa_alfa()` corta o alfa em 150 antes do contorno. Virou regra no guia. |
| 0 s | O texto-gancho entrava crescendo e aparecia pequeno no quadro 0. O guia exige **tamanho cheio no frame 0**. | A batida de entrada caiu de 1,6× para 0,28×. |
| 6 s–8 s | O cone de calor estava fino e quase invisível. | Alcance de 560 para 680 px, abertura de 150 para 205, opacidade e espessura das ondas aumentadas. |
| 12 s–20 s | O comprimido entrava pequeno e escondido atrás da cabeça. | De 480 para 620 px e reposicionado acima da cobra. |
| 30 s | A silhueta do cupinzeiro era um triângulo tosco. | Virou curva de sino com estrias verticais, no traço amarelo do canal. |

**2ª volta:** nenhuma. A primeira volta resolveu os cinco.

## Comparação com a versão 1

| | v1 (documentário) | v2 (estilo do canal) |
|---|---|---|
| Brilho médio | 55 | **120,0** |
| Cenários | 6 | **1** |
| Bicho | close ocupando quase a tela | **26% da altura, terço inferior** |
| Contorno de adesivo | não | **sim** |
| Olho com anel amarelo | 1 plano de 9 | **7 de 7** |
| Camadas de texto | 1 (com caixa preta) | **3** |
| Onçômetro | cena de tela cheia, fundo preto, sem nome | **painel sobre a cena, com "JARARACA"** |
| Efeitos | filtro térmico e varredura | **desenhados** |
| Duração | 26,53 s | **31,63 s** |
| Voz | Windows (rascunho) | **ElevenLabs "daniel narrador", eleven_v4** |

## Resultado

**REPROVADO na etapa 9** — Técnica 6, abaixo de 8. Nota de estilo **10**.

**Falta uma coisa só: trilha.** Resolvido isso, é refazer a etapa 8 (só a mixagem, nem precisa re-renderizar os quadros) e reavaliar. Tudo o mais está aprovado.

A pasta `Entrega/` foi montada para o dono ver o resultado. **Não é material publicável.**

## Riscos anotados

- Pronúncia de "Rraw!" e "fosseta loreal" não conferida de ouvido.
- Texto integral de Ferreira (1965) e Ondetti (1971) não lido (paywall). O roteiro não afirma nada além do que o registro primário do NCBI já diz.
- A cartela final (29,9 s a 31,6 s) tem véu escuro e puxa o brilho mínimo para 60,4. A média fica em 120,0 e passa, mas se a cartela crescer em vídeos futuros isso precisa ser revisto.
