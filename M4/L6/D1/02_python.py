import time

TAMANIO_BLOQUE = 1024 * 1024  # 1 MB

with open("M4/L6/D1/data/logs_grandes.txt", "r", encoding="utf-8") as f:
    while True:
        bloque = f.read(TAMANIO_BLOQUE)
        if not bloque:
            break

        print(bloque)       # procesar / mostrar bloque
        time.sleep(1)       # espera 1 segundo entre bloques
