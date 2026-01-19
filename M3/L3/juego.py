print("=== Juego de Rutas de Animales ===")
print("Movimientos válidos: arriba, abajo, izquierda, derecha\n")

mov1 = input("Nivel 1 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

if mov1 == "derecha":

    mov2 = input("Nivel 2 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

    if mov2 == "izquierda":

        mov3 = input("Nivel 3 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

        if mov3 == "arriba":

            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "abajo":

                print("\n🦋 ¡MARIPOSA! (Ruta completa en la orilla del río)")
            elif mov4 == "derecha":
                print("\n🐝 Abeja confundida entre las flores (no era la mariposa).")
            elif mov4 == "izquierda":
                print("\n🐌 Caracol lento en una hoja (camino alternativo).")
            else:
                print("\nCAMINO ROTO en nivel 4: pisaste una flor y espantaste a todos los insectos.")
        elif mov3 == "abajo":

            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "derecha":
                print("\n🐸 ¡RANA! Saltando entre las piedras.")
            else:
                print("\nCAMINO ROTO: te caíste al agua fría, fin del recorrido.")
        else:
            print("\nCAMINO ROTO en nivel 3: no encontraste ningún animal en la orilla.")
    
    elif mov2 == "derecha":

        mov3 = input("Nivel 3 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

        if mov3 == "abajo":

            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "derecha":
                print("\n🐬 ¡DELFIN! Jugando en las olas.")
            elif mov4 == "izquierda":
                print("\n🦈 ¡TIBURÓN! No era el animal que buscabas, pero lo encontraste.")
            else:
                print("\nCAMINO ROTO: corrientes demasiado fuertes, perdiste el rumbo.")
        else:
            print("\nCAMINO ROTO en nivel 3: te quedaste flotando sin ver animales.")
    
    elif mov2 == "arriba":

        mov3 = input("Nivel 3 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

        if mov3 == "arriba":

            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "arriba":
                print("\n🕊️ PALOMA volando sobre el agua.")
            else:
                print("\nCAMINO ROTO: te distraíste mirando las nubes.")
        else:
            print("\nCAMINO ROTO: el muelle estaba vacío.")
    
    else:
        print("\nCAMINO ROTO en nivel 2: resbalaste y volviste al inicio sin ver nada.")

elif mov1 == "izquierda":

    mov2 = input("Nivel 2 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

    if mov2 == "arriba":

        mov3 = input("Nivel 3 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

        if mov3 == "derecha":

            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "abajo":
                print("\n🐘 ¡ELEFANTE! Caminando lentamente por la sabana.")
            elif mov4 == "arriba":
                print("\n🦁 ¡LEÓN! Rugiendo en una roca.")
            else:
                print("\nCAMINO ROTO: la manada se alejó y te quedaste solo.")
        elif mov3 == "izquierda":
            print("Nivel 3: Árboles dispersos y pasto alto.")
            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "izquierda":
                print("\n🦒 JIRAFA comiendo hojas de los árboles.")
            else:
                print("\nCAMINO ROTO: no lograste ver bien entre el pasto alto.")
        else:
            print("\nCAMINO ROTO en nivel 3: el calor era demasiado fuerte.")
    
    elif mov2 == "abajo":

        mov3 = input("Nivel 3 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

        if mov3 == "izquierda":
  
            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "arriba":
                print("\n🐈 GATO durmiendo en la ventana.")
            elif mov4 == "derecha":
                print("\n🐕 PERRO ladrando en el patio.")
            else:
                print("\nCAMINO ROTO: las mascotas se escondieron.")
        else:
            print("\nCAMINO ROTO: nadie salió a pasear a sus mascotas.")
    
    else:
        print("\nCAMINO ROTO en nivel 2: caminaste sin rumbo por el campo.")

elif mov1 == "arriba":

    mov2 = input("Nivel 2 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

    if mov2 == "arriba":

        mov3 = input("Nivel 3 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

        if mov3 == "derecha":

            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "derecha":
                print("\n🦅 ÁGUILA volando muy alto.")
            else:
                print("\nCAMINO ROTO: perdiste la corriente de aire.")
        else:
            print("\nCAMINO ROTO: las nubes taparon tu vista.")
    else:
        print("\nCAMINO ROTO: no lograste ganar altura suficiente.")

elif mov1 == "abajo":

    mov2 = input("Nivel 2 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

    if mov2 == "derecha":

        mov3 = input("Nivel 3 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

        if mov3 == "abajo":

            mov4 = input("Nivel 4 - Movimiento (arriba/abajo/izquierda/derecha): ").lower()

            if mov4 == "izquierda":
                print("\n🐜 HORMIGA trabajando sin parar.")
            else:
                print("\nCAMINO ROTO: pisaste una rama y todos se escondieron.")
        else:
            print("\nCAMINO ROTO: la tierra estaba demasiado seca.")
    else:
        print("\nCAMINO ROTO: no encontraste ningún insecto interesante.")

else:
    print("\nMovimiento inicial inválido. Debías usar: arriba, abajo, izquierda o derecha.")
