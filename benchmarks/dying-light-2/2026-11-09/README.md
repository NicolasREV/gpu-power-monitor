# Dying Light 2 — benchmarks complementares de 09/11/2026

Foram preservados **cinco arquivos JSON originais** gerados pelo benchmark do Dying Light 2, com **uma execução para cada modo gráfico**. A identificação do modo gráfico foi confirmada pelo pesquisador com base na **ordem em que realizou os testes**; não consta como um campo de configuração explícito dentro dos arquivos JSON.

## Correspondência confirmada pelo pesquisador

| Ordem | Configuração | Arquivo original | Quadros registrados |
|---:|---|---|---:|
| 1 | Native | `Native/01/benchmark-2026.11.09-20.20.12.json` | 6.911 |
| 2 | DLSS Quality | `DLSS-Quality/01/benchmark-2026.11.09-20.24.40.json` | 6.912 |
| 3 | DLSS Performance | `DLSS-Performance/01/benchmark-2026.11.09-20.27.23.json` | 6.884 |
| 4 | FSR Quality | `FSR-Quality/01/benchmark-2026.11.09-20.42.42.json` | 6.880 |
| 5 | FSR Performance | `FSR-Performance/01/benchmark-2026.11.09-20.45.25.json` | 6.879 |

Os horários são aqueles presentes nos nomes dos arquivos. Os JSON originais foram **movidos** da raiz da pasta para as subpastas correspondentes **sem alterar seus bytes**. Veja também `indice.csv`.

## O que os arquivos registram

- `num_frames`: quantidade de quadros registrados;
- `timestamps_us`: marcas temporais em microssegundos;
- `frame_times_us`: tempos por quadro, em microssegundos;
- `logic_frame_times_us`, `render_frame_times_us` e `gpu_frame_times_us`: tempos de processamento detalhados.

A mediana dos intervalos entre timestamps nas cinco execuções está próxima de **16,67 ms**, correspondente a cerca de **60 FPS**. As sequências também incluem variações pontuais de tempo; **não interpretar a mediana como garantia de 60 FPS constantes ou mínimos**.

### Distinção metodológica

Estes cinco benchmarks foram executados em **09/11/2026**, para fornecer **evidências complementares de FPS**. **Não são os mesmos testes utilizados na coleta principal de potência elétrica de outubro**, que permanece documentada nos arquivos originais do monitor Python.

Os logs de outubro, em `../2026-10-15/`, comprovam o histórico de inicializações de benchmarks, mas não apresentavam esses JSON individuais de tempo por quadro.

## Integridade — SHA-256 dos arquivos originais

| Configuração | SHA-256 |
|---|---|
| Native | `96dd8ad778021e2076117a600aa2a39cbafa544e841f035ac7adebe22af90811` |
| DLSS Quality | `c695eca8864256d53b7329cf61414e8211b959d2647c6fc3d56c49ea8b4da4a7` |
| DLSS Performance | `dd7a05b890539924884fee496514dae06810ee9ebf09b14215fec1d63d322aa3` |
| FSR Quality | `27b06cad52c3178f8616e2b287c853edbed0701f132e6eb8ae01dfbb13ad10f0` |
| FSR Performance | `dcb10aa75c4c5bafd8e95f0d55db281f66d018e5400a58564cd181e772ed9a77` |
