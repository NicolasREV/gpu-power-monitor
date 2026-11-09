# HITMAN World of Assassination — verificação complementar FSR Performance

**Data:** 09/11/2026. **Configuração informada pelo pesquisador:** FSR Performance, execução 1.

Os arquivos `01/profiledata.txt` e `01/profiledata.csv` são saídas **da mesma execução** do benchmark integrado, copiadas antes que o HITMAN substituísse os arquivos `profiledata` em um novo teste.

## Resultado registrado

| Métrica | CPU | GPU |
|---|---:|---:|
| Quadros | 6.716 | 6.717 |
| FPS médio | **60,00** | 146,62 |
| FPS mínimo | 28,40 | 28,71 |
| FPS máximo | 302,28 | 368,10 |

**Ambiente:** RTX 4080; driver 616.92; 2560 × 1440; V-Sync desligado; ray tracing desligado; frame generation desligado. O arquivo indica `SSAAMethod = 3` e `SSAAQuality = 1`; a denominação *FSR Performance* foi informada pelo pesquisador.

O FPS médio de CPU caracteriza a execução limitada a aproximadamente **60 FPS**. O FPS médio de GPU é uma métrica específica de processamento da GPU, **não** a taxa efetiva de quadros exibidos.

**Distinção metodológica:** a execução complementar de 09/11/2026 não integra as medições originais de potência de outubro.

## Integridade dos arquivos

Os arquivos foram publicados **idênticos byte a byte aos originais enviados**, incluindo quebras de linha. Verificação por SHA do blob Git:

- `01/profiledata.txt`: `9b998ea95ab661624e12e621f61df1826fe1c008`
- `01/profiledata.csv`: `41c4e21a1479749dcd298eb0c63cf92c8cfad0c6`

Manter novas execuções em `02/`, `03/` etc., sem sobrescrever os dados desta pasta.
