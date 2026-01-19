"""
# 22) Álgebra de conjuntos
{1, 2,  3,  4}
       {3,  4,  5}
{1, 2,  3,  4,  5}
       {3,  4}
{1, 2}
               {5}
{1, 2,          5}
"""
A = {1, 2, 3, 4}
B = {3, 4, 5}

union = A | B
union = A.union(B)
interseccion = A & B
interseccion = A.intersection(B)
diferencia_a = A - B
diferencia_a = A.difference(B)
diferencia_b = B - A
diferencia_b = B.difference(A)
dif_simetrica = A ^ B
dif_simetrica = A.symmetric_difference(B)

print(union)
print(interseccion)
print(diferencia_a)
print(diferencia_b)
print(dif_simetrica)
