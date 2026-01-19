# Ejemplo 14: Lectura/escritura en modo binario (imagen)

with open("M4\\L6\\D1\\data\\foto.png", "rb") as f:
    cabecera = f.read(16)  # primeros bytes (cabecera)

print(cabecera)