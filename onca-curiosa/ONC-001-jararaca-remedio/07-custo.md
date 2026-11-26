# ONC-001 — Narração e custo

**Etapa 7 (versão 2 — gerada com a voz do canal).**

## ElevenLabs — FEITO

A chave foi trocada pelo dono e passou a aceitar `text_to_speech`.

### Conferência antes de gerar

| Campo | Valor |
|---|---|
| Nome da voz lido na API | **"daniel narrador"** |
| Gênero / sotaque | masculino, pt-brazilian |
| Categoria | cloned |
| Modelo | **`eleven_v4`** |
| Velocidade | **`speed: 1.2`** (+20%, como manda o guia) |

O `scripts/narrar.py` só gera depois de confirmar o nome da voz pela API; se o nome não bater, ele para. A chave nunca é impressa — só a impressão digital (SHA-256), que mudou de `2bab327ca9` para `bd69fb5123`, confirmando que é outra chave.

### Caracteres e saldo

| Item | Valor |
|---|---|
| Caracteres enviados (7 frases) | **458** |
| Contador da conta antes | 14.515 |
| Contador da conta depois | **14.700** |
| Variação do contador | **+185** |
| Saldo restante | **25.300 de 40.000** |

> **Nota honesta:** enviei 458 caracteres e o contador da API subiu 185. Não sei explicar a diferença — pode ser cobrança diferente do `eleven_v4` ou atraso na contabilização. **O número que vale é o do contador da conta.** Vou conferir de novo no próximo vídeo; se a diferença se repetir, registro o padrão.

## Ajuste de ritmo

Bruto, como veio do ElevenLabs a +20%: **34,96 s**.

Tratamento: corte de silêncio nas pontas de cada frase, `atempo` e normalização.

| atempo | Duração da fala | Palavras/s |
|---|---|---|
| 1,00 | 34,27 s | 2,31 |
| 1,08 | 31,83 s | 2,48 |
| **1,15** | **29,92 s** | **2,64** |

**Escolhido `atempo=1,15`.** Com a cartela final de 1,7 s, o vídeo fecha em **31,63 s** — dentro da faixa nova de 28 a 33 s e longe do corte de 36 s.

O guia pedia "atempo 1,10" como número fixo. Aqui ele foi **medido**, não copiado: a voz é outra e o alvo de duração mudou. O guia já foi corrigido para mandar medir.

> **Observação levada para o guia:** com 79 palavras em 31,6 s o ritmo fica em 2,64 palavras/s. Para chegar aos ~3 palavras/s do canal **nessa faixa de duração, o roteiro precisa de 85 a 100 palavras**. O ONC-001 ficou com as 79 do roteiro já aprovado pela Jojo — mexer no texto obrigaria a refazer as etapas 3 e 4. O `GUIA-ONCA.md` já está com a contagem nova para os próximos.

## Frases e tempos finais

| # | Entra | Sai | Duração | Palavras |
|---|---|---|---|---|
| 1 | 0,00 | 3,04 | 3,04 s | 8 |
| 2 | 3,06 | 8,33 | 5,27 s | 16 |
| 3 | 8,36 | 11,82 | 3,46 s | 9 |
| 4 | 11,84 | 16,69 | 4,85 s | 15 |
| 5 | 16,72 | 20,30 | 3,58 s | 10 |
| 6 | 20,32 | 25,73 | 5,41 s | 9 |
| 7 | 25,75 | 29,92 | 4,17 s | 12 |
| — | 29,92 | 31,62 | 1,70 s | cartela final, sem fala |

Intervalo entre frases: 0,025 s (guia pede 0,02 a 0,03 s).

## Conferência do texto falado

O texto enviado ao ElevenLabs bate palavra por palavra com o `03-roteiro.md`, nas 7 frases.

**Não foi possível conferir de ouvido** — não há transcrição automática neste ambiente. A pronúncia de "Rraw!" e de "fosseta loreal" segue como risco anotado na avaliação.

## A voz de rascunho saiu

A narração local do Windows usada na versão 1 **foi descartada**. Os arquivos `audio/f*.wav` ficam na pasta só como registro; o `07-narracao.wav` é a voz do canal.

## Custo total do vídeo

| Item | Custo |
|---|---|
| Imagens (iNaturalist, Pixabay) | R$ 0,00 — APIs gratuitas |
| Recorte (rembg, local) | R$ 0,00 |
| Montagem (Python + ffmpeg, local) | R$ 0,00 |
| Narração (ElevenLabs) | **185 caracteres** pelo contador da conta |
| **Dinheiro gasto** | **R$ 0,00** (dentro do plano já assinado) |
