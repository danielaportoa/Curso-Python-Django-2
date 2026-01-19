# generar_origen.py
import os

TAM_ARCHIVO = 1024 * 1024  # 1 MB

with open("M4\\L6\\D1\\data\\origen.bin", "wb") as f:
    f.write(b"ARCHIVO BINARIO DE PRUEBA\n")
    f.write(b"-" * 1024)
    f.write(os.urandom(TAM_ARCHIVO - 1049))  # bytes aleatorios

print("origen.bin creado correctamente")
