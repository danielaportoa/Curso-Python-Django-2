# Ejemplo 7: Inspección de atributos de archivo

with open("M4/L6/D1/data/config.yml", "r", encoding="utf-8") as f:
    nombre = f.name
    modo = f.mode
    codificacion = f.encoding
    cerrado = f.closed

print(f"Nombre del archivo: {nombre}")
print(f"Modo de apertura: {modo}")
print(f"Codificación: {codificacion}")
print(f"¿El archivo está cerrado?: {cerrado}")