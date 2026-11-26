param([string]$Out, [int]$Rate = 2)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech

$audioDir = Join-Path $Out 'audio'
if (-not (Test-Path $audioDir)) { New-Item -ItemType Directory -Path $audioDir | Out-Null }

$frasesPath = Join-Path $Out 'audio\_frases.json'
$frases = (Get-Content -Raw -Encoding UTF8 $frasesPath | ConvertFrom-Json)

$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SelectVoice('Microsoft Maria Desktop')
$synth.Rate = $Rate

$i = 0
foreach ($f in $frases) {
    $i++
    $wav = Join-Path $audioDir ("f{0}.wav" -f $i)
    $synth.SetOutputToWaveFile($wav)
    $synth.Speak($f)
    "gerou f$i"
}
$synth.SetOutputToNull()
$synth.Dispose()
"OK rate=$Rate"
