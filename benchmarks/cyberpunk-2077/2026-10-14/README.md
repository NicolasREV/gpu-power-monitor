# Índice — benchmarks de Cyberpunk 2077 (14/10/2026)

Este índice documenta **26 execuções originais** do benchmark integrado de Cyberpunk 2077 (v2.31), coletadas em 14/10/2026, incluindo os testes pilotos e as execuções candidatas às 15 medições principais (5 modos × 3 repetições). Os **6 benchmarks de 09/11/2026 foram excluídos** da seleção.

**Arquivos de potência:** as [15 medições originais da GPU (CSV)](potencia/README.md) estão publicadas em pasta separada, com três execuções por configuração e índices de integridade.

**Status do acervo:** os **52 arquivos brutos** (`summary.json` e `frames.csv` de cada execução) estão publicados em [`fps/`](fps/README.md), com verificação de integridade em [`fps/SHA256SUMS.txt`](fps/SHA256SUMS.txt).

| Horário em 14/10 | Configuração | FPS médio | Classificação |
|---|---|---:|---|
| 17:24:33 | Nativo — textura Medium | 60,0002 | Piloto |
| 17:26:14 | Nativo — textura Medium | 60,0002 | Piloto |
| 17:31:25 | Nativo — textura High | 60,0004 | Cruzar com CSV de potência |
| 17:33:45 | Nativo — textura High | 60,0001 | Cruzar com CSV de potência |
| 17:36:49 | Nativo — textura High | 59,7739 | Cruzar com CSV de potência |
| 17:38:24 | Nativo — textura High | 60,0003 | Cruzar com CSV de potência |
| 17:41:00 | Nativo — textura High | 60,0000 | Cruzar com CSV de potência |
| 17:48:12 | Nativo — textura High | 59,9999 | Cruzar com CSV de potência |
| 17:49:48 | Nativo — textura High | 60,0000 | Cruzar com CSV de potência |
| 17:55:22 | DLSS Quality | 60,0001 | Cruzar com CSV de potência |
| 17:59:21 | DLSS Quality | 60,0000 | Cruzar com CSV de potência |
| 18:00:56 | DLSS Quality | 60,0003 | Cruzar com CSV de potência |
| 18:02:29 | DLSS Quality | 59,9998 | Cruzar com CSV de potência |
| 18:08:00 | DLSS Performance | 60,0004 | Candidato a teste definitivo |
| 18:09:43 | DLSS Performance | 60,0000 | Candidato a teste definitivo |
| 18:11:14 | DLSS Performance | 59,9998 | Candidato a teste definitivo |
| 18:18:57 | FSR 2.1 Quality — nitidez 0,50 | 60,0000 | Piloto |
| 18:20:31 | FSR 2.1 Quality — nitidez 0,50 | 60,0003 | Piloto |
| 18:22:01 | FSR 2.1 Quality — nitidez 0,50 | 59,9998 | Piloto |
| 18:23:30 | FSR 2.1 Quality — nitidez 0,50 | 59,9998 | Piloto |
| 18:31:27 | FSR 2.1 Quality — nitidez 0,00 | 60,0003 | Candidato a teste definitivo |
| 18:32:57 | FSR 2.1 Quality — nitidez 0,00 | 60,0001 | Candidato a teste definitivo |
| 18:34:26 | FSR 2.1 Quality — nitidez 0,00 | 59,9987 | Candidato a teste definitivo |
| 18:41:38 | FSR 2.1 Performance — nitidez 0,00 | 60,0003 | Candidato a teste definitivo |
| 18:43:28 | FSR 2.1 Performance — nitidez 0,00 | 60,0001 | Candidato a teste definitivo |
| 18:45:01 | FSR 2.1 Performance — nitidez 0,00 | 60,0001 | Candidato a teste definitivo |

## Associação temporal com as 15 medições originais de potência

Os 15 CSVs de potência contêm timestamps de início de coleta. A comparação com os horários dos benchmarks listados no índice permite identificar, por correspondência temporal e ordem de execução, os seguintes pares **candidatos fortes**. A coleta de potência começou aproximadamente 15–17 segundos após o horário indicado no identificador do respectivo benchmark.

| Configuração | Execução | Horário do benchmark (índice FPS) | Início da coleta NVML | FPS médio no índice |
|---|---:|---|---|---:|
| Nativo | 1 | 17:41:00 | 17:41:16 | 59,999973 |
| Nativo | 2 | 17:48:12 | 17:48:28 | 59,999939 |
| Nativo | 3 | 17:49:48 | 17:50:04 | 59,999973 |
| DLSS Quality | 1 | 17:59:21 | 17:59:37 | 60,000027 |
| DLSS Quality | 2 | 18:00:56 | 18:01:12 | 60,000301 |
| DLSS Quality | 3 | 18:02:29 | 18:02:44 | 59,999832 |
| DLSS Performance | 1 | 18:08:00 | 18:08:16 | 60,000351 |
| DLSS Performance | 2 | 18:09:43 | 18:09:59 | 59,999985 |
| DLSS Performance | 3 | 18:11:14 | 18:11:30 | 59,999817 |
| FSR 2.1 Quality (nitidez 0) | 1 | 18:31:27 | 18:31:42 | 60,000256 |
| FSR 2.1 Quality (nitidez 0) | 2 | 18:32:57 | 18:33:13 | 60,000134 |
| FSR 2.1 Quality (nitidez 0) | 3 | 18:34:26 | 18:34:42 | 59,998749 |
| FSR 2.1 Performance (nitidez 0) | 1 | 18:41:38 | 18:41:53 | 60,000309 |
| FSR 2.1 Performance (nitidez 0) | 2 | 18:43:28 | 18:43:44 | 60,000069 |
| FSR 2.1 Performance (nitidez 0) | 3 | 18:45:01 | 18:45:17 | 60,000057 |

**Limites da associação:** a proximidade temporal e a sequência dos modos fornecem evidência forte de correspondência, mas os CSVs de potência não contêm FPS, nem incluem uma chave comum de execução. Os `summary.json` e `frames.csv` originais estão publicados em [`fps/`](fps/README.md) para auditoria independente. Não confundir essa associação com uma medição de FPS realizada pela ferramenta NVML.

## Interpretação e preservação

- Os registros originais contêm `summary.json` (configurações e FPS) e `frames.csv` (dados por quadro); nenhuma execução deve ser descartada do acervo histórico por ser piloto.
- Para a **análise principal do artigo**, somente as três execuções definitivas de cada configuração foram consideradas. O cruzamento dos horários com os CSVs de potência permitiu identificar os 15 pares prováveis, documentados acima. Os arquivos originais de FPS estão disponíveis para conferência; a associação com os dados de potência continua baseada nos horários, pois não existe identificador comum entre ambos.
- A presença de `FSR2Sharpness=0.5` em um `summary.json` **não** significa nitidez ativa se `FSR2Enabled=false`.
- Os benchmarks registram resolução de 2560×1440, limite de 60 FPS, V-Sync desligado, ray tracing desligado, frame generation desligado e resolução dinâmica desligada.
- Estes dados descrevem FPS; o monitor Python registra potência da GPU separadamente.

**Arquivos brutos publicados:** 26 pastas de 14/10/2026 em [`fps/`](fps/README.md), totalizando 52 arquivos originais e o manifesto [`SHA256SUMS.txt`](fps/SHA256SUMS.txt). O índice das execuções permanece em [`indice.csv`](indice.csv).
