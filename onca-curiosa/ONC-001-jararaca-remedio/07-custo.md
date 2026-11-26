# ONC-001 — Narração e custo

**Etapa 7.**

## ElevenLabs — BLOQUEADO

A geração com a voz do canal **não aconteceu**. A chave respondeu:

```
HTTP 401
{"detail":{"type":"authentication_error","code":"unauthorized",
"message":"The API key you used is missing the permission text_to_speech
to execute this operation.","status":"missing_permissions"}}
```

A chave está no ambiente e é válida — ela autentica e lê a conta normalmente. O que falta é a permissão **`text_to_speech`** no escopo dela.

Conta lida antes da tentativa (endpoint `/v1/user/subscription`):

| Item | Valor |
|---|---|
| Plano | starter |
| Caracteres usados | 14.515 de 40.000 |
| Saldo | 25.485 caracteres |
| Voz configurada (`ELEVENLABS_VOICE_ID`) | "daniel narrador" — masculina, pt-BR |

**Créditos gastos neste vídeo: ZERO.** A chamada falhou antes de sintetizar qualquer caractere. O saldo continua em 25.485.

Custo previsto quando a permissão for liberada: **430 caracteres** (as 7 frases), ou seja ~1,7% do saldo. Sobra para toda a fila da semana.

> **Ação do dono:** liberar o escopo `text_to_speech` na chave do ElevenLabs. Eu não leio, não copio e não troco chave.

## Voz de rascunho (o que está no vídeo)

Para o piloto não travar, a narração foi gerada **local e de graça** com a voz do Windows **Microsoft Maria Desktop (pt-BR)**, via `System.Speech`. Custo: **R$ 0,00**, nenhuma API paga.

**Isto é um rascunho, não a voz do canal.** É voz feminina sintética de sistema; o canal usa a masculina do ElevenLabs. Serve para o dono julgar ritmo, corte e imagem — não o acabamento sonoro.

## Ajuste de ritmo

Bruto, na velocidade da leitura: **36,16 s** — acima do limite de ~32 s do guia.

Tratamento: corte de silêncio nas pontas de cada frase, `atempo` e normalização. Testes:

| atempo | Duração | Palavras/s |
|---|---|---|
| 1,15 | 27,20 s | 2,90 |
| **1,18** | **26,52 s** | **2,98** |
| 1,20 | 26,09 s | 3,03 |
| 1,30 | 24,08 s | — (abaixo da faixa) |

**Escolhido: `atempo=1,18`** — é o que cai em cima dos ~3 palavras/s do guia e dentro da faixa de 25 a 30 s.

O guia pede "+20% no ElevenLabs e atempo 1,10" (1,32x no total). Aqui a voz é outra, com ritmo natural diferente, então o valor foi **medido** em vez de copiado. Quando a voz do ElevenLabs entrar, o ajuste é refeito do mesmo jeito: medir, não presumir.

## Frases e tempos finais

| # | Entra | Sai | Duração | Palavras |
|---|---|---|---|---|
| 1 | 0,00 | 2,58 | 2,58 s | 8 |
| 2 | 2,61 | 7,48 | 4,87 s | 16 |
| 3 | 7,51 | 10,35 | 2,84 s | 9 |
| 4 | 10,37 | 14,75 | 4,37 s | 15 |
| 5 | 14,77 | 17,96 | 3,19 s | 10 |
| 6 | 17,99 | 22,88 | 4,89 s | 9 |
| 7 | 22,90 | 26,52 | 3,62 s | 12 |

**Total: 26,52 s, 79 palavras, 2,98 palavras/s.** Intervalo entre frases: 0,025 s (guia pede 0,02 a 0,03 s).

## Conferência do texto falado

Feita por leitura do texto enviado ao sintetizador contra o `03-roteiro.md`: **bate palavra por palavra**, as 7 frases.

**Não foi possível conferir de ouvido.** Não há transcrição automática instalada neste ambiente, então a pronúncia não foi verificada — em especial **"Rraw!"** (onomatopeia) e **"fosseta loreal"**. Fica como risco anotado na avaliação. Quando a voz definitiva for gerada, conferir de ouvido antes de aprovar.

## Custo total do vídeo

| Item | Custo |
|---|---|
| Imagens (iNaturalist, Pixabay) | R$ 0,00 — APIs gratuitas |
| Narração (voz local do Windows) | R$ 0,00 |
| Recorte (rembg, local) | R$ 0,00 |
| Montagem (Python + ffmpeg, local) | R$ 0,00 |
| ElevenLabs | **0 créditos** (bloqueado antes de gastar) |
| **Total** | **R$ 0,00** |
