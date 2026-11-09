# Dying Light 2 — logs originais de 15/10/2026

Três logs do jogo coletados no mesmo dia dos experimentos com a NVIDIA GeForce RTX 4080. O nome `crash_*.log` **não comprova, por si só, que ocorreu uma falha**; esses arquivos também registram inicialização, configurações, sessões e encerramento do jogo.

| Arquivo | Conteúdo relevante |
| --- | --- |
| `crash_20261015_214815848.log` | Inicialização do jogo em **DirectX 11**; não representa o conjunto principal de 15 benchmarks. |
| `crash_20261015_215129741.log` | Inicialização em **DirectX 12** e registros preliminares de benchmark. |
| `crash_20261015_220725301.log` | Sessão principal em **DirectX 12**, registrando **15 inicializações de benchmark** em cinco sequências cronológicas de três execuções, além de alterações nos parâmetros de upscaling. |

O registro principal informa RTX 4080, driver 616.92, DirectX 12 e suporte às tecnologias de upscaling. As opções são armazenadas em códigos internos, portanto **a correspondência exata entre códigos e nomes das configurações deve ser confirmada** com a cronologia experimental e os CSVs de potência.

**Limitação:** os logs não contêm FPS médio individual de cada benchmark. Valores globais de FPS registrados no encerramento do programa referem-se à sessão inteira (incluindo menus e intervalos), e **não devem ser usados como FPS dos 15 testes**.

O monitor Python capturou potência elétrica independentemente do mecanismo de logging do jogo. Arquivos originais publicados sem alteração dos valores; quebras de linha podem ser normalizadas pelo GitHub.
