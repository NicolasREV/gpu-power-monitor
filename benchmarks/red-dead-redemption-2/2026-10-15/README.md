# Red Dead Redemption 2 — benchmarks originais de 15/10/2026

Registro completo dos **18 arquivos TXT** recuperados do benchmark integrado de Red Dead Redemption 2. São **15 execuções principais** (cinco configurações × três repetições) e **3 registros preliminares**, publicados com seus nomes originais.

## Estrutura

| Pasta | Configuração | Arquivos | Horários (15/10/2026) |
|---|---|---:|---|
| `Nativo/` | Renderização nativa | 3 | 09:40:49, 09:46:11, 09:52:26 |
| `DLSS-Quality/` | DLSS Quality | 3 | 10:16:13, 10:21:55, 10:27:56 |
| `DLSS-Performance/` | DLSS Performance | 3 | 10:47:35, 10:52:55, 10:58:25 |
| `FSR-Quality/` | FSR Quality | 3 | 11:07:41, 11:13:04, 11:19:10 |
| `FSR-Performance/` | FSR Performance | 3 | 11:32:24, 11:37:48, 11:43:11 |
| `preliminares/` | Testes exploratórios/abandonados | 3 | 09:29:17, 09:34:29, 10:42:05 |

A associação entre grupos e tecnologias segue a cronologia dos testes documentada no TCC; os arquivos TXT do benchmark **não identificam nominalmente o modo DLSS/FSR usado**. A comprovação desse vínculo depende dos registros de configuração e de potência correspondentes.

## O que os logs comprovam

- **API gráfica:** Vulkan (campo `API: VULKAN`).
- **GPU:** NVIDIA GeForce RTX 4080; **CPU:** AMD Ryzen 7 5800X3D.
- Os registros principais têm resultados por passagem, com FPS mínimo, máximo e médio, frametimes, percentis e contagem de quadros.
- Nas **15 execuções principais**, a média de FPS da passagem 5 ficou próxima de 60. A passagem 5 é apresentada como uma passagem específica do benchmark, **não como uma média agregada comprovada das demais passagens**.

## Como interpretar

- Em muitos logs, `Pass 0` tem `0/0 frames`, média `inf` e valores inválidos. **Não utilizar esse registro para resumir FPS.**
- `Pass 1` até `Pass 5` são passagens do benchmark; não confundir a taxa de quadros exibida por passagem com uma média de todas as passagens.
- O registro preliminar de 09:29:17 apresenta testes sem limite de 60 FPS e não faz parte da análise principal.
- O log de 11:43:11 apresenta variações pontuais acentuadas na passagem 5 (média de 59,794 FPS); conservar o valor tal como registrado e não ocultar essas variações.
- Estes são **resultados do benchmark integrado**, separados dos CSVs de medição de potência elétrica obtidos com o monitor Python.
- O uso do limitador de FPS de 60 pelo Painel de Controle NVIDIA é uma condição metodológica documentada externamente; o log TXT não contém um parâmetro explícito de configuração do limitador.

## Integridade

Os arquivos foram enviados como texto UTF-8 preservando seus conteúdos e nomes. O GitHub pode normalizar quebras de linha; o texto e os valores de benchmark não foram recalculados ou editados.

Dados de 15/10/2026 — evidências para o artigo *Sustentabilidade Gráfica: O papel das tecnologias de upscaling na redução da potência elétrica demandada por uma placa de vídeo em jogos digitais*.
