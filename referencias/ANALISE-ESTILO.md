# Análise de estilo — Onça Curiosa de verdade

Feita sobre os três vídeos de referência em `videos/`, com quadros extraídos a cada 1 s em `quadros/ref1`, `ref2` e `ref3`, e medições feitas em pixel sobre os quadros nativos (720×1280).

| | Vídeo | Duração | Quadros | Cortes de cena | 1 corte a cada |
|---|---|---|---|---|---|
| REF1 | Naja / capuz de costela | 28,14 s | 28 | 11 | 2,56 s |
| REF2 | Avestruz / Top 5 mais rápidos | 35,02 s | 35 | 10 | 3,50 s |
| REF3 | Peixinho-dourado / memória | 33,25 s | 33 | 11 | 3,02 s |

Todos: **720×1280, 30 fps, áudio AAC estéreo 44,1 kHz.**

---

## 1. Cenário

**Um cenário só, do começo ao fim.** Nenhum dos três troca de lugar. O que muda é o enquadramento dentro do mesmo cenário (geral, médio, close) e o que entra por cima.

- **REF1 (naja):** savana **ilustrada**, pintura digital. Céu azul com nuvens volumosas estilizadas, acácias, rochas grandes, capim dourado, sol no canto superior direito. Traço limpo, cores chapadas e saturadas.
- **REF2 (avestruz):** savana **de imagem real**, mas clara, ensolarada, céu azul aberto com nuvens brancas. Nada de desfoque, nada de escurecimento.
- **REF3 (peixinho):** aquário **ilustrado**. Água azul-turquesa (`#00A1B2` no topo, `#00A7CB` no meio), raios de luz descendo, plantas desenhadas, pedrinhas coloridas no fundo, bolhas subindo animadas.

**O cenário é protagonista, não papel de parede.** Ele é nítido, claro e colorido, e o bicho vive dentro dele.

**Brilho médio medido** (0 a 255, média de 30 quadros):

| | Brilho |
|---|---|
| REF1 | **137** |
| REF2 | **149** |
| REF3 | **113** |
| **ONC-001** | **55** |

O nosso piloto é de duas a quase três vezes mais escuro que o canal.

## 2. O bicho

- **É foto real recortada**, não desenho — mas com tratamento de adesivo: **contorno branco grosso em volta de todo o recorte** (~8 px em 720 de largura). Isso aparece nos três, e é o que cola o bicho real no cenário sem parecer colagem malfeita.
- **Tamanho:** no plano geral o bicho ocupa cerca de **20 a 30% da altura da tela**, apoiado no terço inferior. Ele é pequeno — o cenário respira em volta. Close-ups existem (REF2, 17 s a 24 s, só o pescoço e a cabeça), mas são momento, não regra.
- **Ele se mexe.** O avestruz corre com pose alternando entre quadros; o peixe nada, vira para a esquerda e volta; a naja balança e abre o capuz. É animação de personagem, não uma foto parada com um "bob" para cima e para baixo.
- **Comparações na mesma cena:** dois recortes convivendo — avestruz × leão (25–29 s) e avestruz × carro vermelho (30–32 s) no REF2.

## 3. Olhos

É a assinatura visual do canal e aparece **o tempo todo**, não numa cena.

- Círculo grande colado sobre o olho real, bem maior que o olho verdadeiro.
- Miolo claro quase branco-rosado (`#DBC8C4`), pupila preta, brilho branco.
- **Anel amarelo em volta** (`#FAD50B`), grosso.
- No close do avestruz (REF2, 22–24 s) o olho tem raio de ~100 px em 720 de largura — **enorme**, e nesse quadro ele está piscando: a pupila vira uma curva sorridente.
- De perfil: um olho só. De frente (naja): dois.

## 4. Textos — três camadas, não uma

Essa é a diferença de construção mais importante.

**Camada 1 — legenda palavra por palavra.** Topo, centralizada, em y ≈ 220 de 1280 (**17% da altura**). Branca com contorno preto de ~5 px, fonte pesada condensada, altura ~40 px. **Sem caixa de fundo.** A palavra-chave da frase vem em **amarelo** em vez de branco.

**Camada 2 — destaque principal.** Meio-alto, y ≈ 450 a 500. **Gigante** (~110 px de altura), amarelo `#F5DD0B` com contorno preto grosso (~10 px). É onde vão os números: `70 KM/H`, `5 CM`, `2 DEDOS`, `+60 ANOS`, `2,7 M`, `Nº 5`.

**Camada 3 — frase que fica.** Meio-baixo, y ≈ 880. Branca com contorno preto, ~48 px. Exemplos: `MAIOR OLHO EM TERRA`, `NÃO MEXE COM ELE!`, `HORA DA COMIDA`, `CAPUZ DE COSTELA?!`.

**Os textos das camadas 2 e 3 permanecem por 3 a 6 segundos** e vários **se acumulam**: no REF1, `AVES` entra aos 20 s, `LAGARTOS` aos 21 s, `OVOS` aos 22 s e `COBRAS!` aos 23 s — e os quatro ficam juntos na tela, cada um numa cor. No REF2, `A MAIOR AVE DO MUNDO` fica parado de 11 s a 16 s enquanto a legenda corre por cima.

## 5. Efeitos — tudo desenhado, nada de filtro

Os efeitos são **ilustrações vetoriais**, não tratamento de imagem:

| Efeito | Onde |
|---|---|
| Esqueleto de costelas desenhado em branco sobre a cobra | REF1, 3 s / 7 s / 8 s |
| Guarda-chuva colorido ao lado do capuz | REF1, 8 s |
| Carimbo vermelho inclinado `NÃO CHEGA PERTO!` | REF1, 11 s |
| Gotas verdes de veneno | REF1, 14 s |
| Velocímetro com ponteiro animado (61 km/h, 69 km/h) | REF2, 5–6 s |
| Régua vertical amarela medindo `2,7 M` | REF2, 13–16 s |
| X vermelho grande (negação) | REF2, 2 s |
| Caixa amarela inclinada `POW!` | REF2, 27–28 s |
| Interrogações amarelas flutuando | REF3, 1–2 s |
| Labirinto amarelo que se constrói traço a traço | REF3, 24–27 s |
| Duas placas coloridas (experimento) | REF3, 20–23 s |
| Escurecimento do fundo para revelação | REF1 16–17 s, REF3 28 s |

## 6. Onçômetro

Medido no REF1 aos 21 s (quadro nativo 720×1280):

- **Painel:** x de 72 a 655 (**81% da largura**), y de 595 a 925. Fundo `#1E1D22`, cantos bem arredondados (~28 px), **borda amarela** `#F2E565`.
- **Posição:** terço inferior, **sobreposto ao cenário normal** — o bicho continua na tela, logo abaixo. Não é cena dedicada, não tem fundo preto.
- **Cabeçalho:** cápsula amarela centralizada no topo do painel com `ONÇÔMETRO` em preto.
- **Abaixo, o nome do bicho** em branco (`NAJA`, `PEIXINHO-DOURADO`).
- **Quatro linhas**, rótulo branco à esquerda, trilha `#353B47`, barra colorida e número à direita **na cor da barra**:

| Linha | Cor |
|---|---|
| VELOCIDADE | `#35A3FA` azul |
| FORÇA | `#F05E39` laranja |
| ESTRANHEZA | `#BD59F9` roxo |
| PERIGO | `#F5C908` amarelo |

- **As barras preenchem uma a uma** e o painel **fica na tela 5 a 6 segundos** (REF1: 18 s a 23 s; REF3: 24 s a 27 s).
- As notas são honestas com o bicho: o peixinho-dourado leva **PERIGO 0** e **FORÇA 1**.

## 7. Formatos recorrentes

O canal não repete um molde só — e isso é proposital:

1. **Fato único** (REF1): gancho, fato estranho, desdobramentos, Onçômetro, frase de fecho grande (`COBRA QUE COME COBRA!`).
2. **Ranking** (REF2): cartela de abertura com raios de sol, selo `TOP 5 MAIS RÁPIDOS`, `Nº 5` gigante, e **fim com gancho para o próximo**: silhueta preta e amarela do próximo animal + `QUEM É O Nº 4?` com interrogações.
3. **Quiz** (REF3): `CHUTA AÍ!` com alternativas A/B/C em caixas arredondadas e letra em círculo amarelo, **contagem regressiva 3‑2‑1** em círculo que vai de amarelo a vermelho, e depois `RESPOSTA:` com as erradas **riscadas em vermelho** e a certa em **verde**.

## 8. Ritmo

- Corte de cena a cada **2,5 a 3,5 s**, mas a tela nunca fica parada: a legenda troca de palavra a cada ~0,5 s e os destaques entram e saem por cima.
- **Duração: 28 a 35 s.** O guia escrito manda 25 a 30 s e reprova acima de ~32 s — **os dois vídeos mais longos estouram esse limite**. O canal real usa uma faixa mais larga que a do guia.
- Narração em ritmo acelerado, com a legenda sincronizada palavra a palavra.

## 9. Paleta

| Uso | Cor |
|---|---|
| Amarelo de destaque e anel do olho | `#F5DD0B` / `#FAD50B` |
| Borda do Onçômetro | `#F2E565` |
| Painel escuro | `#1E1D22` |
| Trilha de barra | `#353B47` |
| Contorno de texto e do recorte | preto / branco, grossos |
| Negação e alerta | vermelho |
| Acerto | verde |

Amarelo + branco + contorno preto grosso é a identidade. Fundo sempre claro e saturado.

---

# Comparação com o ONC-001 — o que está diferente

Ordenado do mais grave para o menor.

| # | Item | Onça Curiosa de verdade | ONC-001 | Gravidade |
|---|---|---|---|---|
| 1 | **Luz** | brilho médio 113 a 149 | **55** — escurecido e desfocado de propósito | **crítico** |
| 2 | **Cenário** | um só, nítido, claro, ilustrado ou foto real ensolarada | **seis cenários diferentes**: folhas, floresta à noite, chão de mata, comprimidos, estetoscópio, gradiente preto | **crítico** |
| 3 | **Tamanho do bicho** | 20 a 30% da altura, apoiado no terço inferior, cenário respirando | cabeça em close ocupando quase a tela toda, quase o vídeo inteiro | **crítico** |
| 4 | **Contorno do recorte** | contorno branco grosso, tipo adesivo | **nenhum contorno** | **alto** |
| 5 | **Olhos de desenho** | em praticamente todo plano, grandes, com anel amarelo | **uma cena só** (2,6 s de 26,5 s), pequenos, sem anel | **alto** |
| 6 | **Animação do bicho** | corre, nada, balança — pose muda de quadro a quadro | parado, com um leve sobe-e-desce | **alto** |
| 7 | **Camadas de texto** | três: legenda + destaque gigante amarelo + frase que fica | **uma e meia**: legenda com caixa preta atrás, e textos pontuais por cena | **alto** |
| 8 | **Texto que acumula** | `AVES`→`LAGARTOS`→`OVOS`→`COBRAS!` somando na tela | nada acumula; cada coisa aparece e some | **alto** |
| 9 | **Onçômetro** | painel de 81% da largura, sobre o cenário, bicho visível, com o nome do bicho, 5 a 6 s | **cena dedicada de 4,89 s**, fundo preto, tela inteira, **sem o nome do bicho**, bicho só como silhueta apagada | **alto** |
| 10 | **Legenda** | sem caixa, só contorno preto; palavra-chave em amarelo | **caixa preta semitransparente atrás**; tudo branco, sem destaque de palavra-chave | médio |
| 11 | **Efeitos** | ilustrações vetoriais: velocímetro, régua, esqueleto, labirinto, carimbo, POW! | filtro de falsa-cor térmica, varredura, confete — **tratamento de imagem, não desenho** | médio |
| 12 | **Objetos** | desenhados ou recortados com contorno e integrados | **fotos de banco inteiras como fundo** (comprimidos, estetoscópio), sem integração | médio |
| 13 | **Resolução** | 720×1280 | 1080×1920 | baixo (nosso é melhor; só não bater o mesmo arquivo) |
| 14 | **Duração** | 28 a 35 s | 26,53 s | baixo |
| 15 | **Fecho** | frase grande de impacto, ou gancho para o próximo vídeo | tem frase de fecho, **não tem gancho para o próximo** | médio |
| 16 | **Formato de série** | ranking Top 5 e quiz "Chuta aí" como formatos próprios | nenhum formato de série usado | médio |
| 17 | **Paleta** | amarelo `#F5DD0B` + branco + contorno preto, fundo claro | amarelo parecido, mas sobre fundo escuro — **sem a mesma força** | médio |

## O diagnóstico em uma frase

O ONC-001 ficou parecido com um **documentário curto**: foto real escurecida, close dramático, pouca informação na tela. A Onça Curiosa de verdade é um **desenho animado com bicho real colado dentro**: cenário claro e inteiro, personagem pequeno e vivo com olho de cartoon, e a tela cheia de texto e gráfico desenhado.

## O que precisa mudar na montagem

1. **Um cenário só por vídeo**, claro e saturado, sem escurecer nem desfocar. Para a jararaca: mata atlântica ilustrada ou foto real bem iluminada.
2. **Bicho pequeno, no terço inferior, com contorno branco de adesivo e animação de pose.**
3. **Olho de desenho grande com anel amarelo em todo plano em que o bicho aparece.**
4. **Três camadas de texto**, com o destaque amarelo gigante para os números (`1981`, `681 N`, etc.) e frases que ficam e acumulam.
5. **Onçômetro como painel sobre a cena**, com o nome do bicho, barras preenchendo uma a uma, 5 a 6 s — nunca cena de tela cheia.
6. **Efeitos desenhados** no lugar de filtro de imagem: para a jararaca, um cone de calor saindo da fosseta, régua, seta, carimbo.
7. **Legenda sem caixa**, com a palavra-chave em amarelo.
8. **Decidir a faixa de duração**: o guia escrito diz 25 a 30 s, o canal real entrega 28 a 35 s. Precisa de uma regra só — pergunta aberta para o dono.

> **Pendência de regra:** `GUIA-ONCA.md` diz "25 a 30 s, acima de ~32 s é reprovado" e manda "animação de recorte". Os vídeos reais vão a 33 e 35 s e usam cenário ilustrado com foto recortada por cima. Antes de remontar, o guia precisa ser atualizado para bater com o canal — senão a Duda reprova por regra o que o canal faz na prática.
