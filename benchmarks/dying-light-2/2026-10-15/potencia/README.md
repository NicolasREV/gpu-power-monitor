# Dying Light 2 — medições originais de potência da GPU

Esta pasta contém **15 arquivos CSV originais** do monitor de potência elétrica da GPU, registrados durante o benchmark integrado de *Dying Light 2* em **15/10/2026**, com cinco configurações gráficas e três execuções por configuração.

**Não confundir:** os [cinco JSONs complementares de FPS](../../2026-11-09/README.md) correspondem a outras execuções, realizadas depois para documentar o desempenho do benchmark; eles não substituem nem integram as 15 execuções originais de potência. Há também [logs do jogo](../README.md) armazenados separadamente.

## Condições experimentais

- GPU NVIDIA GeForce RTX 4080; resolução 2560×1440; limite de 60 FPS aplicado pelo Painel de Controle da NVIDIA.
- Preset Very High, sem ray tracing, frame generation, sincronização vertical ou resolução dinâmica.
- Configurações: Nativo, DLSS Quality, DLSS Performance, FSR Quality e FSR Performance.
- Coleta com script Python usando NVIDIA Management Library (NVML); colunas: `timestamp,elapsed_s,power_w,gpu_util_percent`.
- **Nenhuma amostra foi removida ou filtrada.** Os CSVs permanecem exatamente como recebidos, incluindo nomes originais, quebras CRLF e todas as linhas.

## Organização

Cada arquivo está em `<configuracao>/<execucao>/<nome-original>.csv`, com `01`, `02` e `03` representando as repetições experimentais.

## Resumo dos resultados

As quantidades e médias individuais são listadas em ordem 1 / 2 / 3. A média por configuração é a média aritmética das médias das três execuções.

| Configuração | Amostras por execução | Potências médias 1 / 2 / 3 (W) | Média das três (W) |
|---|---|---|---:|
| Nativo | 109 / 109 / 109 | 111.88 / 111.41 / 111.23 | 111.51 |
| DLSS-Quality | 109 / 109 / 109 | 95.64 / 96.12 / 94.86 | 95.54 |
| DLSS-Performance | 109 / 109 / 109 | 81.86 / 81.27 / 79.41 | 80.85 |
| FSR-Quality | 109 / 109 / 109 | 85.71 / 85.98 / 86.19 | 85.96 |
| FSR-Performance | 109 / 109 / 109 | 74.93 / 74.96 / 74.79 | 74.89 |
| **Total** | **1.635 amostras** | **15 execuções** | — |

As médias correspondem à Tabela 5 do TCC *Sustentabilidade Gráfica*, dentro do arredondamento adotado no texto.

## Índice e integridade

O arquivo [indice.csv](indice.csv) documenta as 15 execuções, nomes originais, quantidade de amostras, médias, hashes Git SHA-1 e SHA-256. Todos os blobs foram comparados com os hashes dos arquivos originais, confirmando identidade byte a byte antes da publicação.

As leituras representam **potência elétrica reportada pela GPU (W)**, não a energia total do computador. As amostras de uma mesma execução não são repetições independentes.
