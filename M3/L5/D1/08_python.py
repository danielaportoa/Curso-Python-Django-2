# 8) Lista usada como cola (cola ineficiente)
cola = ["t1", "t2", "t3"]
cola.append("t4")
primero = cola.pop(0)  # O(N)
print(primero, cola)

fila = ["p1", "p2", "p3", "p4"]
personas = fila.pop(0)
caja_1 = personas
personas = fila.pop(0)
caja_2 = personas
personas = fila.pop(0)
caja_1 = personas
print(caja_1, caja_2)