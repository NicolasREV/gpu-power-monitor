# Cyberpunk 2077 — medições originais de potência da GPU

Esta pasta contém os **15 arquivos CSV originais** de potência elétrica e utilização da GPU coletados em **14/10/2026** durante o benchmark integrado de *Cyberpunk 2077*, divididos em cinco configurações gráficas, com três repetições por configuração.

**Atenção à separação das fontes:** estes CSVs são os registros da ferramenta Python/NVML utilizados para calcular a potência elétrica do TCC. Os dados de FPS do benchmark integrado (`summary.json` e `frames.csv`, contendo também testes pilotos) têm um [índice próprio](../README.md) e não devem ser confundidos com estas medições. Os benchmarks de novembro não fazem parte dos dados de potência originais.

## Condições experimentais

- GPU NVIDIA GeForce RTX 4080; resolução 2560×1440; limite de 60 FPS no próprio Cyberpunk 2077.
- Preset gráfico Ultra, textura High; Ray Tracing, V-Sync, Frame Generation e resolução dinâmica desativados.
- Condições: renderização nativa, DLSS Quality, DLSS Performance, FSR 2.1 Quality e FSR 2.1 Performance.
- Sharpening FSR desativado (0) nas condições finais. Medições preliminares com sharpening 0,5 não integram os 15 arquivos desta pasta.
- Colunas de coleta: `timestamp,elapsed_s,power_w,gpu_util_percent`.
- **Nenhuma amostra foi removida ou filtrada.** Os arquivos foram preservados com os nomes originais e quebras de linha CRLF.

## Organização

Os arquivos estão em `<configuracao>/<execucao>/<nome-original>.csv`, com pastas de execução `01`, `02` e `03` representando cada repetição.

## Resumo das medições

Quantidade de amostras e médias individuais na ordem de execução (1 / 2 / 3). A média da configuração é a média aritmética das três médias de execução.

| Configuração | Amostras 1 / 2 / 3 | Potências médias 1 / 2 / 3 (W) | Média das três (W) |
|---|---|---|---:|
| Nativo | 69 / 69 / 69 | 190.87 / 191.01 / 191.59 | 191.16 |
| DLSS-Quality | 69 / 69 / 69 | 168.65 / 169.14 / 170.52 | 169.44 |
| DLSS-Performance | 69 / 69 / 69 | 104.94 / 105.83 / 104.02 | 104.93 |
| FSR-Quality | 69 / 69 / 69 | 146.91 / 148.87 / 148.13 | 147.97 |
| FSR-Performance | 69 / 69 / 69 | 95.36 / 96.94 / 96.02 | 96.11 |
| **Total** | **1.035 amostras** | **15 execuções** | — |

As médias por configuração são compatíveis com a Tabela 1 do artigo *Sustentabilidade Gráfica*, considerando o arredondamento utilizado na apresentação dos resultados.

## Índice, integridade e interpretação

O [indice.csv](indice.csv) contém os nomes originais, o modo gráfico, a execução, a quantidade de amostras, a potência média individual e os hashes Git SHA-1 e SHA-256. A integridade byte a byte dos 15 CSVs foi validada comparando os hashes dos arquivos de origem com os blobs Git.

A coleta reporta **potência elétrica da GPU em watts (W)**, não energia total do computador. As 69 leituras aproximadas de cada execução são observações dentro da mesma repetição experimental, e não 69 repetições independentes.
