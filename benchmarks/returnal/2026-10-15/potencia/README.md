# Returnal — medições originais de potência da GPU

Medições de potência elétrica da GPU no benchmark integrado do Returnal, obtidas em **15/10/2026**, com cinco configurações gráficas e três repetições por configuração (15 arquivos CSV).

Estes são **dados originais de potência**, separados dos [registros complementares de FPS de novembro](../../2026-11-09/README.md). Os dados daqui foram utilizados para calcular as médias de potência da pesquisa, enquanto os registros posteriores documentam a proximidade da meta de 60 FPS. Não misturar essas execuções.

## Condições

- GPU NVIDIA GeForce RTX 4080, resolução 2560×1440 e limite de 60 FPS configurado no próprio Returnal.
- Preset gráfico Epic, sem Ray Tracing, V-Sync, Frame Generation ou escalonamento dinâmico de resolução.
- Cinco configurações: Nativo, DLSS Quality, DLSS Performance, FSR Quality e FSR Performance.
- Coleta por script Python com NVML; colunas `timestamp,elapsed_s,power_w,gpu_util_percent`.
- Os arquivos originais foram mantidos integralmente, incluindo finais de linha CRLF, nomes e todas as amostras. **Não houve exclusão ou filtragem de amostras**.

## Organização

Cada arquivo está em `<configuracao>/<execucao>/<nome-original>.csv`, com `01`, `02` e `03` como números de repetição. Os nomes originais dos CSVs foram preservados.

## Resumo dos dados originais

Amostras e potência média por execução estão em ordem 1 / 2 / 3. A média por configuração é a média aritmética das três médias de execução.

| Configuração | Amostras por execução | Potências médias 1 / 2 / 3 (W) | Média das três (W) |
|---|---|---|---:|
| Nativo | 121 / 121 / 120 | 147.16 / 149.86 / 150.72 | 149.25 |
| DLSS-Quality | 121 / 119 / 121 | 108.57 / 109.98 / 108.95 | 109.17 |
| DLSS-Performance | 120 / 121 / 120 | 92.95 / 92.29 / 92.62 | 92.62 |
| FSR-Quality | 121 / 121 / 121 | 100.64 / 100.98 / 99.69 | 100.43 |
| FSR-Performance | 121 / 121 / 121 | 84.43 / 84.60 / 84.94 | 84.66 |
| **Total** | **1.810 amostras** | **15 execuções** | — |

Essas médias reproduzem os valores do artigo *Sustentabilidade Gráfica* dentro do arredondamento informado.

## Reprodutibilidade e integridade

O arquivo [indice.csv](indice.csv) reúne as 15 execuções, seus nomes originais, quantidades de amostras, médias individuais e hashes Git SHA-1 (do blob) e SHA-256, permitindo verificar a integridade dos arquivos publicados. Os 15 blobs Git foram conferidos contra hashes calculados diretamente dos arquivos originais antes da publicação.

As leituras aproximadamente a cada segundo não são repetições experimentais independentes. Os números representam a **potência elétrica reportada pela GPU em watts**, não a energia total do computador.
