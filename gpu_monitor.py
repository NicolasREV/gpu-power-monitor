import csv
import time
import queue
import keyboard
import pynvml

from pathlib import Path
from datetime import datetime
from statistics import mean

# Fila de comandos dos atalhos
comandos = queue.Queue()

keyboard.add_hotkey(
    "ctrl+shift+f9",
    lambda: comandos.put("iniciar")
)

keyboard.add_hotkey(
    "ctrl+shift+f10",
    lambda: comandos.put("parar")
)

keyboard.add_hotkey(
    "ctrl+shift+f11",
    lambda: comandos.put("sair")
)

# Inicializa a GPU
pynvml.nvmlInit()

try:
    gpu = pynvml.nvmlDeviceGetHandleByIndex(0)
    nome = pynvml.nvmlDeviceGetName(gpu)

    # Pasta de resultados
    pasta = Path(__file__).resolve().parent / "resultados"
    pasta.mkdir(exist_ok=True)

    print(f"GPU detectada: {nome}")
    print("\nCTRL + SHIFT + F9  = Iniciar")
    print("CTRL + SHIFT + F10 = Finalizar")
    print("CTRL + SHIFT + F11 = Sair")
    print("\nAguardando inicio da coleta...")

    while True:
        comando = comandos.get()

        if comando == "sair":
            break

        if comando != "iniciar":
            continue

        consumos = []
        utilizacoes = []

        data = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S-%f"
        )
        arquivo = pasta / f"gpu_{data}.csv"

        inicio = time.perf_counter()
        proxima_leitura = inicio
        encerrar = False

        print("\n===== COLETA INICIADA =====")

        with open(
            arquivo, "w", newline="", encoding="utf-8"
        ) as f:
            writer = csv.writer(f)

            writer.writerow([
                "timestamp",
                "elapsed_s",
                "power_w",
                "gpu_util_percent"
            ])

            while True:
                agora = time.perf_counter()

                if agora >= proxima_leitura:
                    consumo = (
                        pynvml.nvmlDeviceGetPowerUsage(gpu)
                        / 1000
                    )

                    utilizacao = (
                        pynvml.nvmlDeviceGetUtilizationRates(
                            gpu
                        ).gpu
                    )

                    tempo = time.perf_counter() - inicio

                    horario = datetime.now().isoformat(
                        timespec="milliseconds"
                    )

                    consumos.append(consumo)
                    utilizacoes.append(utilizacao)

                    writer.writerow([
                        horario,
                        round(tempo, 3),
                        consumo,
                        utilizacao
                    ])

                    f.flush()

                    print(
                        f"[{tempo:.1f}s] "
                        f"Consumo: {consumo:.2f} W | "
                        f"Utilizacao: {utilizacao}%"
                    )

                    proxima_leitura += 1.0

                    # Evita leituras acumuladas se houver atraso
                    if proxima_leitura < time.perf_counter():
                        proxima_leitura = (
                            time.perf_counter() + 1.0
                        )

                # Aguarda a próxima leitura ou um atalho
                espera = max(
                    0, proxima_leitura - time.perf_counter()
                )

                try:
                    comando = comandos.get(timeout=espera)
                except queue.Empty:
                    continue

                if comando == "parar":
                    break

                if comando == "sair":
                    encerrar = True
                    break

        duracao = time.perf_counter() - inicio

        print("\n===== RESULTADOS =====")
        print(f"GPU: {nome}")
        print(f"Duracao: {duracao:.2f} segundos")
        print(f"Amostras: {len(consumos)}")

        if consumos:
            print(f"Consumo medio: {mean(consumos):.2f} W")
            print(f"Consumo minimo: {min(consumos):.2f} W")
            print(f"Consumo maximo: {max(consumos):.2f} W")
            print(
                f"Utilizacao media: "
                f"{mean(utilizacoes):.2f}%"
            )

        print(f"\nCSV salvo em: {arquivo}")
        print("======================")

        if encerrar:
            break

        print("\nAguardando nova coleta...")

finally:
    keyboard.unhook_all_hotkeys()
    pynvml.nvmlShutdown()
    print("\nPrograma encerrado.")
