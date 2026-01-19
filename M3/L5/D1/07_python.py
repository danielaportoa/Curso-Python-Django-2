# 7) Lista como pila (stack LIFO)
pila = []
pila.append("A")
pila.append("B")
pila.append("C")
print(f"Mis Documentos: {pila}")
b = pila.pop(1)
papelera = []
print(f"Papelera: {papelera}")
papelera.append(b)
print(f"Mis Documentos: {pila}")
print(f"Papelera: {papelera}")
restauracion = papelera.pop()
pila.insert(1, restauracion)
print(f"Mis Documentos: {pila}")
print(f"Papelera: {papelera}")

"""
while pila:
    elemento = pila.pop()
    print("Sacando:", elemento)
"""