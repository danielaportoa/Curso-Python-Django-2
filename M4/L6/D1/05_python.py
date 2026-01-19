# Ejemplo 5: readlines() para archivos pequeños con acceso aleatorio

with open("M4/L6/D1/data/mensajes.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

primera = lineas[0]
ultima = lineas[-1]

print("Primera línea:", primera)
print("Última línea:", ultima)
