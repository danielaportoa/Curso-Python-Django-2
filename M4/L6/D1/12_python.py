# Ejemplo 12: Modo 'a+' para leer y luego seguir agregando

with open("M4\\L6\\D1\\data\\historial.txt", "a+", encoding="utf-8") as f:
    f.seek(0)  # necesario para leer desde el inicio
    contenido = f.read()
    f.write("Nueva entrada\n")

print(contenido)