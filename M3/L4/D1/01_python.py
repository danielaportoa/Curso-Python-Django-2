# 1) while básico: contador ascendente
"""
contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1
"""
from time import perf_counter

# Inicio de medición
inicio = perf_counter()

# 1) while básico: contador ascendente
contador = 1
while contador <= 500000:
    print("Contando:", contador)
    contador += 1

# Fin de medición
fin = perf_counter()

print(f"Tiempo de ejecución del while: {fin - inicio:.8f} segundos")
