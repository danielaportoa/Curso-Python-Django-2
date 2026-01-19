# 19) Sombreado de variables
x = 50

def prueba():
    x = 10
    return x

print("Local", prueba())
print("Global", x)
