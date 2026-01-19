# Ejemplo 1: Lectura completa de archivo pequeño (modo texto)

with open("M4/L6/D1/data/hola.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

print(contenido)