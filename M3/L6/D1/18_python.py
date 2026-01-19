# 18) Variable global (escritura con global)
contador = 0
contador_global = 0

def incrementar():
    global contador
    contador += 1

def local():
    contador_local = 1
    print("Local", contador_local)

print("Antes", contador)
incrementar()
print("despues", contador)
print("Global", contador_global)
local()