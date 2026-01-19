# Ejemplo 3: Iteración línea a línea (forma recomendada)

with open("M4/L6/D1/data/datos.csv", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.rstrip("\n")
        # procesar linea
        print(linea)
