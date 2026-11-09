# Índice — benchmarks de Cyberpunk 2077 (14/10/2026)

Este índice documenta **26 execuções originais** do benchmark integrado de Cyberpunk 2077 (v2.31), coletadas em 14/10/2026, incluindo os testes pilotos e as execuções candidatas às 15 medições principais (5 modos × 3 repetições). Os **6 benchmarks de 09/11/2026 foram excluídos** da seleção.

**Status do acervo:** este documento é o índice; os 52 arquivos brutos (`summary.json` e `frames.csv` de cada execução) estão no pacote de distribuição preparado separadamente, mas **ainda não foram publicados neste repositório**.

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

## Interpretação e preservação

- Os registros originais contêm `summary.json` (configurações e FPS) e `frames.csv` (dados por quadro); nenhuma execução deve ser descartada do acervo histórico por ser piloto.
- Para a **análise principal do artigo**, somente as três execuções definitivas de cada configuração devem ser associadas aos CSVs originais de potência. O vínculo ainda precisa ser validado pelos horários, sobretudo em Nativo e DLSS Quality.
- A presença de `FSR2Sharpness=0.5` em um `summary.json` **não** significa nitidez ativa se `FSR2Enabled=false`.
- Os benchmarks registram resolução de 2560×1440, limite de 60 FPS, V-Sync desligado, ray tracing desligado, frame generation desligado e resolução dinâmica desligada.
- Estes dados descrevem FPS; o monitor Python registra potência da GPU separadamente.

**Pacote original filtrado (preparado para publicação, ainda não enviado ao GitHub):** 26 pastas de 14/10/2026, com 52 arquivos brutos, mais `indice.csv`, `SHA256SUMS.txt` e `README.md`. SHA-256 do pacote ZIP preparado: `986925a6cfec3e66959403cbc7dc5179b8c0831ac838b73e7d3c9649b138f312`.
