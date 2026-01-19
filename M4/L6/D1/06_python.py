# Ejemplo 6: Uso de seek() y tell() para mover el puntero

with open("M4/L6/D1/data/texto.txt", "r+", encoding="utf-8") as f:
    inicio = f.tell()
    linea = f.readline()
    posicion_despues = f.tell()
    f.seek(inicio)  # volver al comienzo

print("Posición inicial:", inicio)
print("Línea leída:", linea.strip())
print("Posición después de leer la línea:", posicion_despues)
