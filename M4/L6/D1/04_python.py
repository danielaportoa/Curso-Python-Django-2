# Ejemplo 4: Uso de readline() con bucle while

with open("M4/L6/D1/data/datos.csv", "r", encoding="utf-8") as f:
    while True:
        linea = f.readline()
        if linea == "":
            break  # EOF real
        # procesar linea
        print(linea)
