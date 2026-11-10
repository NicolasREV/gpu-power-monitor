# Returnal — benchmarks complementares de 09/11/2026

Cinco arquivos CSV do benchmark integrado do **Returnal**, executados em ordem de criação: **Native → DLSS Quality → DLSS Performance → FSR Quality → FSR Performance**. Esta associação foi **confirmada pelo pesquisador**; os CSVs não contêm o nome do modo gráfico em uma coluna própria.

## Resultados e arquivos

| Ordem de criação | Configuração | Horário no nome do arquivo | Amostras de FPS | FPS mínimo registrado | FPS médio registrado | FPS máximo registrado |
|---:|---|---|---:|---:|---:|---:|
| 1 | Native | 20:58:13 | 298 | 60 | 60,00 | 60 |
| 2 | DLSS Quality | 21:00:59 | 298 | 60 | 60,00 | 60 |
| 3 | DLSS Performance | 21:04:00 | 298 | 60 | 60,00 | 60 |
| 4 | FSR Quality | 21:08:12 | 298 | 60 | 60,00 | 60 |
| 5 | FSR Performance | 21:10:47 | 298 | 60 | 60,00 | 60 |

Cada arquivo está em sua respectiva pasta `<modo>/01/`, **com o nome original**, por exemplo `Native/01/BenchmarkResult 2026.11.09-20.58.13.csv`. Veja também `indice.csv`.

Os arquivos contêm as colunas **`FPS,GPU,CPU`**. Todas as 298 linhas de dados em cada um dos cinco arquivos reportam **FPS = 60**, compatível com o **limitador nativo de 60 FPS**, cuja utilização foi confirmada pelo pesquisador. Os arquivos não trazem timestamps por amostra nem legenda detalhando as unidades de GPU e CPU; **não são suficientes para demonstrar que cada quadro foi entregue em exatamente 16,67 ms ou que não houve quedas instantâneas de FPS entre as amostras**.

### Distinção metodológica

Os cinco benchmarks de **09/11/2026** são **verificações complementares de FPS**, separadas das medições de potência elétrica originais realizadas em outubro de 2026. Não substituir os registros históricos de consumo pelos arquivos desta pasta.

### Integridade dos arquivos originais

Os conteúdos publicados no GitHub foram verificados como **idênticos byte a byte** aos CSVs recebidos, incluindo o caractere de nova linha ao final. Hashes SHA-256:

| Configuração | SHA-256 |
|---|---|
| Native | `e97034afb5a77d2d8da8a82b7cff2082636a3dccd814dc3656e32f247a7cc83d` |
| DLSS Quality | `6858ba10fd11eab553429d8a7351ac1ab029dc6eb30227836abb0118e778054d` |
| DLSS Performance | `b1a168cc9507a799ee3a323752cfb55e9cfe5b630002be88528e152415b235e7` |
| FSR Quality | `9d12b15afa4ab324b310de5d11e3e97536464dfaffd6e883fbce91803b612426` |
| FSR Performance | `02a9cb8935290e99fce160a7dcead39b8b35cbb1c02e3a3e13ec9154729afdb3` |
