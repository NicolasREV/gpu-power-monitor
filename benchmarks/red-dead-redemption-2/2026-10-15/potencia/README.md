# Red Dead Redemption 2 — medições originais de potência da GPU

Este diretório contém os **15 arquivos CSV originais de potência e utilização da GPU** dos experimentos do jogo, com **cinco configurações × três execuções**. Os arquivos originais foram preservados **byte a byte**, inclusive com finais de linha CRLF, e conferidos por hash Git SHA-1 dos blobs.

Os logs TXT do benchmark integrado (dados de FPS) estão nas outras pastas do diretório superior. Os CSVs aqui presentes têm colunas `timestamp,elapsed_s,power_w,gpu_util_percent` e se destinam à análise da potência elétrica registrada pelo script de monitoramento.

## Organização
Cada CSV está na pasta `<configuracao>/<execucao>/<nome_original>.csv`, com `Nativo`, `DLSS-Quality`, `DLSS-Performance`, `FSR-Quality` e `FSR-Performance` como configurações e `01`, `02`, `03` como repetições. O nome original de cada arquivo foi mantido.

## Tratamento analítico informado no TCC

Na análise do Red Dead Redemption 2 foram descartadas, **apenas dos cálculos derivados**, as amostras com potência elétrica **estritamente inferior a 80 W** (`power_w < 80`). Esse limiar foi adotado após inspeção de quedas de potência associadas aos carregamentos do benchmark. As amostras com potência igual ou superior a 80 W foram mantidas. A análise é reproduzível aplicando esse filtro a cada CSV, mas a identificação dos carregamentos por esse valor é um **critério operacional**, e não uma marcação explícita de cenas nos dados.

**Total de registros:** 4.183 amostras brutas; **668** abaixo de 80 W e excluídas dos cálculos de potência tratada; **3.515** amostras válidas. Nenhuma linha foi removida dos CSVs de origem.

## Contagens por execução e efeito sobre as médias

A coluna de exclusões e a coluna de amostras válidas mostram as contagens nas execuções 1 / 2 / 3. As médias por configuração são as médias aritméticas das **três médias de execução**, não a média direta de todas as amostras agregadas.

| Configuração | Excluídas 1 / 2 / 3 | Válidas 1 / 2 / 3 | Média bruta (W) | Média tratada (W) |
|---|---|---|---:|---:|
| Nativo | 41 / 42 / 47 | 234 / 233 / 234 | 127.83 | 145.41 |
| DLSS-Quality | 46 / 50 / 44 | 232 / 234 / 238 | 101.18 | 115.08 |
| DLSS-Performance | 44 / 44 / 48 | 233 / 230 / 233 | 94.37 | 106.43 |
| FSR-Quality | 44 / 43 / 44 | 233 / 232 / 234 | 102.74 | 116.12 |
| FSR-Performance | 43 / 44 / 44 | 246 / 235 / 234 | 90.47 | 101.69 |
| **Total** | **668** | **3.515** | — | — |

Os valores tratados reproduzem os resultados apresentados na Tabela 2 do artigo, dentro do arredondamento. O arquivo [indice.csv](indice.csv) detalha **cada uma das 15 execuções**, incluindo contagens, médias brutas, médias filtradas e o hash Git do arquivo original.

## Interpretação

As leituras de potência foram obtidas pelo script com NVML, aproximadamente uma por segundo. As três execuções de cada configuração representam repetições do experimento; amostras dentro de uma execução não são repetições independentes. Os valores descritos são de **potência elétrica da GPU (W)**, não consumo energético total do computador.
