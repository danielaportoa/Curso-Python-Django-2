from .models.tienda import Tienda
from .models.usuario import Usuario
from .models.admin import Admin
from .models.cliente import Cliente


def main():
    ecommerce_tienda = Tienda("Mi Tienda Online")

    # Usuario base (como tú lo haces)
    juan = Usuario("Juan", 30, "juan@gmail.com")

    # Admin usando SOLO posicionales (tu modelo)
    juan_admin = Admin("admin001", ecommerce_tienda.catalogo, juan)
    ecommerce_tienda.registrar_usuario(juan_admin)

    # Cliente ejemplo
    maria = Cliente("Maria", 25, "maria@gmail.com", "cli001")
    ecommerce_tienda.registrar_usuario(maria)

    while True:
        print("\n=== LOGIN ===")
        print("1. Entrar como ADMIN")
        print("2. Entrar como CLIENTE")
        print("0. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            email = input("Email ADMIN: ")
            usuario = ecommerce_tienda.iniciar_sesion(email)
            if usuario and hasattr(usuario, "admin_id"):
                ecommerce_tienda.mostrar_menu_admin(usuario)
            else:
                print("No es un ADMIN válido.")

        elif opcion == "2":
            email = input("Email CLIENTE: ")
            usuario = ecommerce_tienda.iniciar_sesion(email)
            if usuario and hasattr(usuario, "customer_id"):
                ecommerce_tienda.mostrar_menu_cliente(usuario)
            else:
                print("No es un CLIENTE válido.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
