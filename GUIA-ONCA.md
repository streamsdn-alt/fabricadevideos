# GUIA-ONCA.md — Onça Curiosa (@oncacuriosabr)

> Guia de estilo do canal. Lido junto com `MANUAL-FABRICA.md` antes de qualquer trabalho.
>
> **Referência visual oficial: [`referencias/ANALISE-ESTILO.md`](referencias/ANALISE-ESTILO.md)**, medida sobre três vídeos reais do canal. Em qualquer dúvida de aparência, vale o que está lá. Este guia é o resumo operacional dela.
>
> Atualizado em 25/11/2026 com as decisões do dono.

## Pautas

- Pode repetir bicho, **nunca o fato**. Mínimo de 2 semanas entre vídeos do mesmo animal.
- Fatos já usados estão em `FATOS-USADOS.md`. Em bicho repetido, se não tiver certeza de que o fato é novo, **perguntar ao dono**.
- Antes de aprovar, conferir imagem real suficiente do bicho nos bancos. **Sem imagem boa, troca o bicho.**

## Formatos

Três formatos aprovados. **Variar entre eles** — não repetir o mesmo molde em série.

1. **Fato único.** Gancho, fato estranho, desdobramentos, Onçômetro, frase grande de fecho.
2. **Ranking.** Cartela de abertura com selo ("TOP 5 MAIS RÁPIDOS"), número gigante ("Nº 5"), e fecho com gancho para o próximo: silhueta do próximo bicho + **"QUEM É O Nº 4?"**.
3. **Quiz.** **"CHUTA AÍ!"** com alternativas A/B/C em caixas arredondadas e letra em círculo amarelo, contagem regressiva **3‑2‑1** em círculo que vai de amarelo a vermelho, depois "RESPOSTA:" com as erradas **riscadas em vermelho** e a certa em **verde**.

> **Não colocar quiz em todos os vídeos.** O teste "quiz × sem quiz" ainda vai ser avaliado em **03/12/2026**.

## Roteiro

- **28 a 33 s.** **Acima de 36 s é reprovado.**
- ~**85 a 100 palavras**, 7 ou 8 frases curtas, no máximo **3 fatos**.
- Ritmo de fala por volta de **2,6 a 3,0 palavras/s** (é o que a faixa de duração permite).
- **1º segundo:** parte estranha do bicho + fato "impossível"; **texto-gancho grande já no frame 0, em tamanho cheio** — não pode entrar crescendo.
- Comparação com o dia a dia (tomada, ar-condicionado, canudinho, GPS, câmera térmica).
- **Penúltima frase: Onçômetro** (Velocidade, Força, Estranheza, Perigo).
- **Última frase:** rugido curto + retoma o gancho (final em loop).
- Números por extenso. Pergunta fácil para o comentário fixado.

## Visual — as 8 regras que a Duda mede

Estas são as regras que reprovam na etapa 9. Todas saíram da análise dos vídeos reais.

| # | Regra | Como se mede |
|---|---|---|
| 1 | **Brilho médio do vídeo ≥ 110** (escala 0–255) | média da luminância de 1 em cada 10 quadros |
| 2 | **Um cenário só** do começo ao fim | conferir na folha de quadros |
| 3 | **Bicho com 20 a 30% da altura**, apoiado no terço inferior | altura do recorte ÷ 1920 |
| 4 | **Contorno branco de adesivo** em todo recorte | olhar a borda do bicho e dos objetos |
| 5 | **Olho de desenho com anel amarelo** na maior parte dos planos | contar os planos com bicho que têm o olho |
| 6 | **3 camadas de texto** | topo palavra a palavra sem caixa / destaque gigante amarelo no meio / frase que acumula embaixo |
| 7 | **Onçômetro como painel sobre a cena, com o nome do bicho** | nunca cena dedicada de tela cheia |
| 8 | **Efeitos desenhados** | nada de filtro de imagem (falsa-cor, varredura, desfoque artístico) |

## Cenário

- **Foto real CLARA e nítida** dos bancos (Pixabay, Coverr, Wikimedia, iNaturalist). **Um cenário por vídeo.**
- **Proibido escurecer e proibido desfocar.** Realce de cor e contraste leve é permitido; escurecer não.
- Cenário ilustrado gerado fica para depois — ainda não está liberado.
- O cenário é protagonista, não papel de parede: ele respira em volta do bicho.

## O bicho

- Foto real recortada (`rembg`), **com contorno branco grosso de adesivo** (~13 px em 1080 de largura).
- **Limpar o alfa fantasma antes do contorno** (corte em ~150): corpo meio transparente vira mancha branca no recorte.
- **20 a 30% da altura da tela**, apoiado no terço inferior (base por volta de y = 1830).
- **Ele se mexe:** balanço, respiração, troca de pose. Foto parada é reprovada.

## Olhos

É a assinatura do canal e aparece **na maior parte dos planos**, não numa cena.

- Círculo grande colado sobre o olho real, bem maior que o olho verdadeiro.
- Miolo claro quase branco, pupila preta, brilho branco.
- **Anel amarelo grosso** em volta (`#FAD50B`), com contorno preto.
- Pisca de tempos em tempos (pupila vira uma curva).
- De perfil: **um** olho. De frente: dois.

## As 3 camadas de texto (1080×1920)

| Camada | y | Como é |
|---|---|---|
| **1 — legenda** | ~330 | palavra por palavra, centralizada, **sem caixa de fundo**, branca com contorno preto de ~9 px, ~66 px de corpo. **Palavra-chave da frase em amarelo.** |
| **2 — destaque gigante** | ~700 | amarelo `#F5DD0B`, contorno preto de ~15 px, ~190 px de corpo. É onde vão os números: `1981`, `70 KM/H`, `5 CM`. |
| **3 — frase que fica** | ~1150 | branca com contorno preto, ~60 px. **Fica de 3 a 6 s e acumula** com a frase seguinte. |

Área segura: nada importante acima de 165 px nem abaixo de 1755 px.

## Efeitos — todos desenhados

Vetor, nunca filtro de imagem. Do repertório do canal:

velocímetro com ponteiro · régua medindo · esqueleto por cima do bicho · carimbo inclinado · X vermelho · check verde · caixa `POW!` · interrogações flutuando · labirinto que se constrói · números gigantes · setas e anéis marcando parte do corpo · cone de calor · escurecimento só para revelação.

## Onçômetro

- **Painel sobre a cena**, com o bicho visível logo abaixo. **Nunca cena dedicada de tela cheia.**
- Largura ~81% da tela (x de 104 a 980), altura ~495 px, cantos arredondados (raio 42).
- Fundo `#1E1D22`, **borda amarela** `#F2E565` de 6 px.
- **Cápsula amarela** centralizada na borda de cima com `ONÇÔMETRO` em preto.
- **Nome do bicho** logo abaixo, em branco (`JARARACA`, `NAJA`, `PEIXINHO-DOURADO`).
- Quatro linhas, rótulo branco à esquerda, trilha `#353B47`, barra colorida, número à direita **na cor da barra**:

| Linha | Cor |
|---|---|
| VELOCIDADE | `#35A3FA` azul |
| FORÇA | `#F05E39` laranja |
| ESTRANHEZA | `#BD59F9` roxo |
| PERIGO | `#F5C908` amarelo |

- **Barras preenchem uma a uma**, painel fica de 5 a 6 s.
- **As notas são honestas com o bicho.** No canal, o peixinho-dourado leva PERIGO 0 e FORÇA 1.

## Paleta

| Uso | Cor |
|---|---|
| Amarelo de destaque e anel do olho | `#F5DD0B` / `#FAD50B` |
| Borda do Onçômetro | `#F2E565` |
| Painel escuro | `#1E1D22` |
| Trilha de barra | `#353B47` |
| Negação e alerta | vermelho `#E53935` |
| Acerto | verde `#3CDC78` |

Amarelo + branco + contorno preto grosso sobre fundo claro e saturado. É a identidade.

## Ritmo

- Mudança visual a cada **2 a 4 s**. A tela nunca fica parada: a legenda troca de palavra e os destaques entram e saem por cima.
- Shorts **SEM** a oncinha.

## Áudio

- **ElevenLabs, voz "daniel narrador"** (`ELEVENLABS_VOICE_ID`), **modelo `eleven_v4`**, **velocidade +20%** (`speed: 1.2`).
- **Nunca** usar voz do Windows, Edge ou qualquer outra como substituta. Se o ElevenLabs falhar, **parar a etapa 7 e avisar o dono.**
- Antes de gerar, **conferir pelo nome da voz na API** que o `ELEVENLABS_VOICE_ID` é mesmo a "daniel narrador" — sem nunca mostrar a chave.
- Pausas internas 0,07 s; 0,02 a 0,03 s entre frases.
- **O ajuste final de ritmo é medido, não copiado:** cortar silêncio nas pontas e escolher o `atempo` que põe a duração dentro de 28 a 33 s.
- Trilha da pasta `musicas/` a cerca de **−24 dB** abaixo da voz, abaixando sob a fala. Efeitos sonoros nos efeitos visuais.
- Registrar sempre os caracteres gastos.

## Entrega

- MP4 **1080×1920**.
- **Capa universal** (mínimo de palavras: números, nomes, símbolos, onomatopeias).
- **Capa TikTok 1080×1440**.
- **SRT PT/EN/ES**.
- `POSTAGEM.md` com título, descrição, hashtags (`curiosidades`, `animais`, `natureza` + 2 do tema), fontes, créditos e horário sugerido (**12h ou 19h**).
