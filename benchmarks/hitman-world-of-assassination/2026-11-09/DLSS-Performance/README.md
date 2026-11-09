# HITMAN World of Assassination — verificação complementar DLSS Performance

**Data:** 09/11/2026. **Configuração informada pelo pesquisador:** DLSS Performance, execução 1.

Os arquivos `01/profiledata.txt` e `01/profiledata.csv` são saídas **da mesma execução** do benchmark integrado. Foram copiados antes de o HITMAN substituir seus arquivos `profiledata` em uma nova execução.

## Resultado registrado

| Métrica | CPU | GPU |
|---|---:|---:|
| Quadros | 6.716 | 6.717 |
| FPS médio | **60,00** | 148,44 |
| FPS mínimo | 26,58 | 28,31 |
| FPS máximo | 150,47 | 340,27 |

**Ambiente:** RTX 4080; driver 616.92; 2560 × 1440; V-Sync desligado; ray tracing desligado; frame generation desligado. O arquivo indica `SSAAMethod = 2` e `SSAAQuality = 1`; a denominação *DLSS Performance* foi informada pelo pesquisador.

O FPS médio de CPU caracteriza a execução limitada a aproximadamente **60 FPS**. O FPS médio de GPU é uma métrica específica da GPU, **não** a taxa efetiva de quadros exibidos.

**Distinção metodológica:** a execução complementar de 09/11/2026 não integra as medições originais de potência de outubro.

## Integridade dos arquivos

Conteúdo publicado idêntico ao recebido, incluindo as quebras de linha originais. Verificação por SHA do blob Git:

- `01/profiledata.txt`: `9841919aa935081509763c33bad9d31e4fa2b030`
- `01/profiledata.csv`: `0bc47909608691725876b0b4661da9acf00859d8`

Manter novas execuções em `02/`, `03/` etc., sem substituir os resultados desta pasta.
