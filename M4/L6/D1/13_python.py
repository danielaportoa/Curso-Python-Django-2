# Ejemplo 13: Modo 'x' para creación exclusiva

from pathlib import Path

ruta = Path("M4\\L6\\D1\\data\\config_inicial.json")

try:
    with open(ruta, "x", encoding="utf-8") as f:
        f.write("{}\n")
except FileExistsError:
    # archivo ya existe, no se pisa
    print(f"El archivo {ruta} ya existe y no se ha sobrescrito.")
