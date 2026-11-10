# Arquivos brutos de FPS — Cyberpunk 2077 (14/10/2026)

Este diretório preserva as **26 execuções originais** do benchmark integrado de Cyberpunk 2077 (v2.31), incluindo os testes-piloto. Não inclui as verificações complementares de 09/11/2026.

Cada pasta `benchmark_2026-10-14_HH-MM-SS/` contém dois arquivos **preservados byte a byte**:

- `summary.json`: configuração gráfica e estatísticas do benchmark, incluindo FPS médio, mínimo e máximo;
- `frames.csv`: dados por quadro registrados pelo jogo.

## Distribuição das 26 execuções

| Configuração | Execuções | Observação |
| --- | ---: | --- |
| Nativo | 9 | 2 pilotos com textura Medium e 7 com textura High |
| DLSS Quality | 4 | Inclui um teste anterior às 3 repetições principais |
| DLSS Performance | 3 | |
| FSR 2.1 Quality | 7 | 4 pilotos com nitidez 0,50 e 3 finais com nitidez 0,00 |
| FSR 2.1 Performance | 3 | Nitidez 0,00 |

As **15 execuções principais** (5 configurações × 3 repetições) e seu cruzamento temporal com os CSVs de consumo estão detalhados no [índice de benchmarks](../README.md) e em [`indice.csv`](../indice.csv). A correspondência entre FPS e potência foi inferida a partir dos horários e da sequência de execução: não existe um identificador comum entre os registros do jogo e a ferramenta NVML.

O arquivo [`SHA256SUMS.txt`](SHA256SUMS.txt) contém um hash SHA-256 de cada um dos 52 arquivos, com caminho relativo a este diretório, para permitir a verificação da integridade dos originais.

Os [CSVs de potência da GPU](../potencia/README.md) foram coletados por outra ferramenta e estão preservados separadamente. A ferramenta de monitoramento da potência não mede FPS.
