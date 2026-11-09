# HITMAN World of Assassination — benchmark original (15/10/2026)

Dois arquivos de **uma mesma execução**, preservados do período dos experimentos:

- `profiledata.txt`: informações do hardware, configurações e resumo do benchmark; listas de FPS por frame para CPU e GPU.
- `profiledata.csv`: dados de tempo por frame nas seções `Frame, Time CPU (ms)` e `Frame, Time GPU (ms)`.

## Resultados registrados

| Indicador | CPU | GPU |
| --- | ---: | ---: |
| Quadros reportados | 6.718 | 6.719 |
| FPS médio | **60,00** | **146,94** |
| FPS mínimo | 42,82 | 65,07 |
| FPS máximo | 102,59 | 379,69 |

O tempo total do teste no eixo de CPU é aproximadamente **111,95 segundos**. Os 146,94 FPS no indicador de GPU são uma medida de processamento da GPU isoladamente, **não** a taxa efetivamente entregue ao jogador; o indicador de CPU registra média de **60,00 FPS**.

O arquivo identifica RTX 4080, driver 616.92, 2560×1440, V-Sync desligado, ray tracing desligado e frame generation desligado.

**Limitações:** são apenas dois formatos de saída **do mesmo benchmark**, não duas repetições. Os registros não identificam inequivocamente qual condição (nativa, DLSS ou FSR) foi usada, nem comprovam o FPS dos outros 14 testes. Não associar a um modo de upscaling ou CSV de potência sem evidência adicional.

Os arquivos foram publicados com os nomes originais. O conteúdo textual pode ter as quebras de linha normalizadas pelo GitHub; valores e medições não foram recalculados.
