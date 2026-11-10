# HITMAN World of Assassination — medições originais de potência

Esta pasta contém os **15 CSVs originais de potência elétrica da GPU**, registrados em **15/10/2026** durante o benchmark integrado de HITMAN World of Assassination, com cinco configurações gráficas e três execuções por configuração.

Estes arquivos são diferentes dos [benchmarks complementares de FPS de novembro](../../2026-11-09/README.md). Os dados originais desta pasta sustentam os cálculos de potência elétrica do TCC; as execuções posteriores registram o FPS e não substituem as medições originais.

## Condições experimentais

- GPU NVIDIA GeForce RTX 4080; resolução de 2560×1440 pixels; limite de 60 FPS pelo Painel de Controle da NVIDIA.
- Preset gráfico Ultra, nas condições Nativo, DLSS Quality, DLSS Performance, FSR Quality e FSR Performance.
- Coleta da GPU com script Python e NVIDIA Management Library (NVML), aproximadamente uma leitura por segundo.
- Colunas originais: `timestamp,elapsed_s,power_w,gpu_util_percent`.
- Nenhuma amostra foi excluída ou alterada; os 15 arquivos foram preservados exatamente como recebidos, incluindo nomes e quebras de linha CRLF.

## Organização

Cada CSV está em `<configuracao>/<execucao>/<nome-original>.csv`, com `01`, `02` e `03` como números de execução.

## Resumo das medições

Amostras e médias individuais em ordem de execução (1 / 2 / 3). A média final de cada modo é a média aritmética das três médias de execução.

| Configuração | Amostras por execução | Potências médias 1 / 2 / 3 (W) | Média das três (W) |
|---|---|---|---:|
| Nativo | 103 / 103 / 104 | 77.07 / 77.04 / 76.94 | 77.02 |
| DLSS-Quality | 104 / 103 / 103 | 63.35 / 63.79 / 64.44 | 63.86 |
| DLSS-Performance | 103 / 103 / 103 | 58.27 / 58.89 / 58.91 | 58.69 |
| FSR-Quality | 103 / 103 / 103 | 67.94 / 69.21 / 67.52 | 68.22 |
| FSR-Performance | 103 / 103 / 104 | 58.00 / 58.54 / 59.39 | 58.64 |
| **Total** | **1.548 amostras** | **15 execuções** | — |

As médias reproduzem os valores informados no artigo *Sustentabilidade Gráfica*, considerando o arredondamento para duas casas decimais.

## Integridade e reprodução

O [indice.csv](indice.csv) reúne o nome original, a configuração, o número de execução, a quantidade de registros, a potência média por execução, o hash Git SHA-1 do blob e o SHA-256 de cada CSV.

A identidade binária dos 15 arquivos foi verificada comparando os hashes Git calculados a partir dos arquivos originais com os blobs publicados. As medições são da **potência elétrica da GPU em W**, não da energia total consumida pelo computador. Leituras dentro de uma mesma execução não constituem repetições experimentais independentes.
