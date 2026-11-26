# ONC-001 — Narração e custo

**Etapa 7.**

## ElevenLabs — AINDA BLOQUEADO (2ª tentativa, 25/11/2026)

O dono informou que a permissão `text_to_speech` foi liberada. **Tentei de novo e a API continua recusando**, com exatamente a mesma resposta:

```
HTTP 401
{"detail":{"type":"authentication_error","code":"unauthorized",
"message":"The API key you used is missing the permission text_to_speech
to execute this operation.","status":"missing_permissions"}}
```

A etapa 7 **parou aqui**, como mandado. Nenhuma outra voz foi usada como substituta.

### Conferência da voz (feita antes de tentar gerar)

O `ELEVENLABS_VOICE_ID` do ambiente aponta para a voz certa:

| Campo | Valor |
|---|---|
| Nome | **"daniel narrador"** |
| Gênero / sotaque | masculino, pt-brazilian |
| Categoria | cloned |

### O que a chave consegue e não consegue

| Chamada | Resultado |
|---|---|
| `GET /v1/voices` | 200 |
| `GET /v1/models` | 200 |
| `GET /v1/user/subscription` | 200 |
| `GET /v1/history` | **401 missing_permissions** |
| `POST /v1/text-to-speech` | **401 missing_permissions** |

Ou seja: a chave autentica e lê, mas **não tem nem `text_to_speech` nem acesso ao histórico**. É uma chave só de leitura.

### Identificação da conta (para o dono conferir se mexeu na chave certa)

| Campo | Valor |
|---|---|
| `user_id` | `user_7901m81g6ggxe1vvsj7ph14eynbk` |
| workspace | nenhum |
| plano | starter |
| saldo | 14.515 de 40.000 caracteres usados |
| chave: prefixo / tamanho | `sk_...` / 51 caracteres |
| chave: impressão digital (SHA-256, 10 primeiros) | `2bab327ca9` |

A impressão digital é um hash, não a chave. Serve para o dono confirmar se a chave que ele editou é a mesma que está no meu ambiente — **se for outra, o problema é que o ambiente tem a chave antiga.**

### Parâmetros prontos para quando liberar

| Item | Valor |
|---|---|
| Modelo | `eleven_v4` (confirmado disponível na conta) |
| Voz | `daniel narrador` |
| Velocidade | `speed: 1.2` (+20%) |
| Custo previsto | **430 caracteres** (~1,7% do saldo) |

**Créditos gastos até agora: ZERO.** As duas tentativas falharam antes de sintetizar qualquer caractere.

## Voz de rascunho (o que está no vídeo atual — a ser substituída)

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
