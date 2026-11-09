# HITMAN World of Assassination — verificação complementar FSR Quality

**Data:** 09/11/2026. **Configuração informada pelo pesquisador:** FSR Quality, execução 1.

Os arquivos `01/profiledata.txt` e `01/profiledata.csv` são saídas **da mesma execução** do benchmark integrado. Foram copiados antes de o HITMAN substituir seus arquivos `profiledata` em uma nova execução.

## Resultado registrado

| Métrica | CPU | GPU |
|---|---:|---:|
| Quadros | 6.716 | 6.717 |
| FPS médio | **60,00** | 129,39 |
| FPS mínimo | 26,88 | 28,23 |
| FPS máximo | 149,78 | 274,62 |

**Ambiente:** RTX 4080; driver 616.92; 2560 × 1440; V-Sync desligado; ray tracing desligado; frame generation desligado. O arquivo indica `SSAAMethod = 3` e `SSAAQuality = 3`; a denominação *FSR Quality* foi informada pelo pesquisador.

O FPS médio de CPU caracteriza a execução limitada a aproximadamente **60 FPS**. O FPS médio de GPU é uma métrica específica da GPU, **não** a taxa efetiva de quadros exibidos.

**Distinção metodológica:** a execução complementar de 09/11/2026 não integra as medições originais de potência de outubro.

## Integridade dos arquivos

Conteúdo publicado idêntico ao recebido, incluindo as quebras de linha originais. Verificação por SHA do blob Git:

- `01/profiledata.txt`: `8e5dca3030aa12bbc8db67fa2a45ec2677cde533`
- `01/profiledata.csv`: `db3740cdd204786c23f3c3ec809d0af4c4b22887`

Manter novas execuções em `02/`, `03/` etc., sem substituir os resultados desta pasta.
