# HITMAN World of Assassination — verificação complementar DLSS Quality

**Data:** 09/11/2026. **Configuração informada pelo pesquisador:** DLSS Quality, execução 1.

Os arquivos `01/profiledata.txt` e `01/profiledata.csv` são duas saídas **da mesma execução** do benchmark, salvas antes que o HITMAN substituísse os arquivos `profiledata` em uma nova execução.

## Resultado registrado

| Métrica | CPU | GPU |
|---|---:|---:|
| Quadros | 6.719 | 6.720 |
| FPS médio | **60,00** | 134,09 |
| FPS mínimo | 26,33 | 26,62 |
| FPS máximo | 310,59 | 284,05 |

**Ambiente:** RTX 4080; driver 616.92; 2560 × 1440; V-Sync desligado; Ray Tracing desligado; Frame Generation desligado. O arquivo indica `SSAAMethod = 2` e `SSAAQuality = 3`; o nome *DLSS Quality* foi informado pelo pesquisador.

O campo FPS médio de CPU caracteriza o benchmark com limitação aproximada de **60 FPS**. O FPS médio de GPU reporta uma medida própria da GPU e **não** deve ser interpretado como FPS efetivamente exibidos.

**Distinção metodológica:** esta execução de 09/11/2026 é **complementar**. Não pertence aos testes originais de potência realizados em outubro.

## Integridade dos arquivos

Os arquivos foram publicados com as **mesmas sequências de bytes** dos enviados pelo pesquisador, incluindo quebras de linha CRLF, e verificados pelo SHA do blob Git:

- `01/profiledata.txt`: `5f15f2a383763ea5d2475536684156fa70570954`
- `01/profiledata.csv`: `ee51e542eebaae1c820a48e4c25f5cfcf15856c6`

Salvar execuções adicionais em `02/`, `03/` etc., sem sobrescrever a primeira.
