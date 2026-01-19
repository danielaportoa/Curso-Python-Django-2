import random

# La computadora elige un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

intentos = 0
adivinado = False

print("🎯 Bienvenido al juego: Adivina el número")
print("He pensado un número entre 1 y 100")

while not adivinado:
    intento = input("👉 Ingresa tu número: ")

    # Validar que sea un número
    if not intento.isdigit():
        print("⚠️ Por favor ingresa un número válido")
        continue

    intento = int(intento)
    intentos += 1

    if intento < numero_secreto:
        print("🔻 Muy bajo")
    elif intento > numero_secreto:
        print("🔺 Muy alto")
    else:
        print(f"✅ ¡Correcto! El número era {numero_secreto}")
        print(f"🎉 Lo adivinaste en {intentos} intentos")
        adivinado = True
