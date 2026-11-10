# GPU Power Monitor

Ferramenta de monitoramento em Python desenvolvida para coletar a potência elétrica reportada por uma GPU NVIDIA e a utilização da GPU durante benchmarks de jogos digitais.

Código de coleta do artigo **Sustentabilidade Gráfica: O papel das tecnologias de upscaling na redução da potência elétrica demandada por uma placa de vídeo em jogos digitais** (2026).

## Ambiente utilizado

- Windows 11 Pro, 64 bits
- NVIDIA GeForce RTX 4080, driver 616.92
- Python 3.15.0
- `nvidia-ml-py` 13.615.71
- `keyboard` 0.13.5

A reprodução exige Windows, Python, driver NVIDIA e uma GPU compatível com NVML.

## Instalação

```bash
python -m pip install -r requirements.txt
```

## Execução

```bash
python gpu_monitor.py
```

| Atalho global | Ação |
| --- | --- |
| `Ctrl + Shift + F9` | Iniciar a coleta |
| `Ctrl + Shift + F10` | Finalizar a coleta |
| `Ctrl + Shift + F11` | Encerrar o programa |

O programa seleciona a GPU de índice 0 (`nvmlDeviceGetHandleByIndex(0)`).

## Dados coletados

As consultas são agendadas em intervalos de aproximadamente um segundo:

- `nvmlDeviceGetPowerUsage(gpu)`: potência reportada em miliwatts, dividida por 1.000 para conversão a watts;
- `nvmlDeviceGetUtilizationRates(gpu).gpu`: utilização da GPU em percentual.

Cada execução gera um arquivo CSV dentro da pasta `resultados/`, com as colunas:

| Campo | Significado |
| --- | --- |
| `timestamp` | Data e horário da leitura, com milissegundos |
| `elapsed_s` | Tempo decorrido desde o início da coleta, em segundos |
| `power_w` | Potência elétrica reportada pela GPU, em W |
| `gpu_util_percent` | Utilização da GPU, em % |

Ao terminar, o programa exibe duração, quantidade de amostras, potência média, mínima e máxima e utilização média. As médias são aritméticas e consideram as amostras da execução.

## Observações e limitações

- A frequência nominal de consulta é de 1 Hz. Se uma leitura atrasar, o próximo agendamento é reajustado para evitar leituras acumuladas.
- Os CSVs são gravados sem exclusão automática de amostras. Qualquer filtragem posterior faz parte da análise, não deste programa.
- Uma falha de consulta à NVML não é recuperada automaticamente.
- O monitor não registra FPS, temperatura ou frequência da GPU.
- Os valores representam a potência da GPU reportada pela NVML, não o consumo elétrico de todo o computador.
- A pasta `resultados/`, gerada pela ferramenta de monitoramento, está excluída do controle de versão. Entretanto, os 75 arquivos CSV originais utilizados na análise de potência elétrica estão publicados no diretório `benchmarks/`, organizados por jogo, configuração gráfica e execução. Os registros de FPS disponíveis estão documentados separadamente, distinguindo as medições originais das verificações complementares.

## Documentação

[NVIDIA — NVML Device Queries](https://docs.nvidia.com/deploy/nvml-api/latest/api/group__nvmlDeviceQueries.html)
