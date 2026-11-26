# ONC-001 — Plano de cenas (versão 2, estilo oficial)

**Etapa 5.** Refeito sobre o `GUIA-ONCA.md` de 25/11/2026 e a `referencias/ANALISE-ESTILO.md`.
Tempos medidos na narração real do ElevenLabs (`audio/_timeline.json`). Duração total: **31,63 s**. Canvas 1080×1920.

## A mudança de concepção

A versão 1 trocava de cenário a cada cena e escurecia tudo. **Agora é um cenário só, claro, do começo ao fim**, e o que muda é o que entra por cima: o bicho, as três camadas de texto e os efeitos desenhados. É assim que o canal funciona.

## Cenário único

`assets/fundos/foto-9618231.jpg` — sub-bosque de mata, tronco com folhas grandes e luz entrando. Ken Burns lento de 7% ao longo dos 31,63 s. **Sem escurecer, sem desfocar.** Brilho medido do vídeo montado: **120,0** (mínimo exigido: 110).

## Faixas do canvas

| Faixa | y | Uso |
|---|---|---|
| 0–165 | topo | **proibido** (interface) |
| ~330 | camada 1 | legenda palavra por palavra, sem caixa |
| ~700 | camada 2 | destaque gigante amarelo |
| 820–1315 | Onçômetro | painel sobre a cena (só no beat 6) |
| ~1150 | camada 3 | frase que fica e acumula |
| 1330–1830 | bicho | 500 px = **26% da altura**, apoiado no terço inferior |
| 1755–1920 | rodapé | **proibido** (interface) |

## Beats

| # | Entra | Sai | Dur | Frase | Pose | O que entra por cima |
|---|---|---|---|---|---|---|
| 1 | 0,00 | 3,04 | 3,04 | 1 | A (perfil p/ esquerda) | **texto-gancho em tamanho cheio no quadro 0**: "ESSE BURACO / VÊ CALOR"; anel amarelo pulsando na fosseta + seta |
| 2 | 3,06 | 8,33 | 5,27 | 2 | A | destaque "FOSSETA LOREAL"; **cone de calor vetorial** saindo da fosseta a partir de +1,9 s; camada 3 acumula "ACHA A PRESA PELO CALOR" (+2,4 s) e "COMO CÂMERA TÉRMICA" (+3,7 s) |
| 3 | 8,36 | 11,82 | 3,46 | 3 | **B (vira para a direita)** | carimbo vermelho inclinado "VENENO" batendo; camada 3 "DERRUBA A PRESSÃO" |
| 4 | 11,84 | 16,69 | 4,85 | 4 | A | recorte de comprimidos com contorno de adesivo entrando pela direita; "1981" gigante amarelo; camada 3 "VIROU REMÉDIO DE PRESSÃO" |
| 5 | 16,72 | 20,30 | 3,58 | 5 | A | **X vermelho** sobre a cobra e **check verde** sobre o comprimido; camada 3 acumula "NINGUÉM TOMA VENENO" e "O REMÉDIO FOI DESENHADO" |
| 6 | 20,32 | 25,73 | 5,41 | 6 | A | **Onçômetro como painel sobre a cena**, com "JARARACA" no cabeçalho; 4 barras preenchendo uma a cada ~0,8 s |
| 7 | 25,75 | 29,92 | 4,17 | 7 | A | retoma o gancho: "VÊ CALOR." + camada 3 "E VIROU REMÉDIO." |
| 8 | 29,92 | 31,62 | 1,70 | — | — | **cartela de gancho para o próximo vídeo**: "PRÓXIMO: 200 MILHÕES DELES", silhueta de cupinzeiro desenhada em amarelo, "E A RAINHA? NINGUÉM ACHOU." |

**Mudança visual:** o maior beat é o do Onçômetro, com 5,41 s, e ele tem 4 batidas internas. Nenhum trecho fica mais de ~1,9 s sem mudança.

## O bicho

- Duas poses: **A** = `inat-348275825` (perfil para a esquerda), **B** = `inat-348275873` (perfil para a direita). A troca no beat 3 é a "virada" do personagem.
- **Contorno branco de adesivo** de 13 px em todos os recortes, bicho e comprimido.
- **Limpeza de alfa antes do contorno** (corte em 150): sem isso o corpo semitransparente vira mancha branca. Foi o defeito que reprovou a primeira montagem.
- Movimento contínuo: balanço lateral, respiração e flutuação vertical.
- **Olho de desenho com anel amarelo em todos os 7 beats com bicho**, piscando a cada ~3 s.

## Efeitos — todos desenhados

Anel + seta na fosseta · cone de calor em três camadas com ondas · carimbo inclinado "VENENO" · "1981" gigante batendo · X vermelho · check verde · painel do Onçômetro · silhueta de cupinzeiro em curva de sino com estrias.

**Nenhum filtro de imagem.** A falsa-cor térmica e a varredura da versão 1 saíram: eram tratamento de imagem, que é outra linguagem.

## Pendência

A pasta `musicas/` continua vazia. Sem trilha da Biblioteca de Áudio do YouTube, o vídeo sai com voz seca e **reprova em Técnica**. Não substituir por música de outra fonte.
