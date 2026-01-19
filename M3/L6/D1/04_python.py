# 4) Parámetros con valor por defecto
def saludar(nombre, saludo="Hola", despedida="Adiós"):
    return f"{saludo}, {nombre}. {despedida}"

print(saludar("Luis"))
print(saludar("Luis", "Buenos días"))
print(saludar("Luis", despedida="Hasta luego"))
