from .catalogo import Catalogo
from .usuario import Usuario
from .admin import Admin
from .cliente import Cliente
from .carrito import Carrito


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = Catalogo()
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def iniciar_sesion(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        print("Usuario no encontrado")
        return None

    def mostrar_menu_cliente(self, cliente):
        while True:
            print("\n=== MENÚ CLIENTE ===")
            print("1. Ver catálogo")
            print("2. Buscar producto")
            print("3. Agregar al carrito")
            print("4. Ver carrito y total")
            print("5. Confirmar compra")
            print("0. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                self.catalogo.listar_productos()

            elif opcion == "2":
                term = input("Buscar por nombre: ")
                resultados = self.catalogo.buscar_producto(term)
                if not resultados:
                    print("Sin resultados.")
                else:
                    for p in resultados:
                        print(f"{p.product_id} | {p.name} | ${p.price} | Stock: {p.stock}")

            elif opcion == "3":
                pid = input("ID producto: ")
                try:
                    cantidad = int(input("Cantidad: "))
                except ValueError:
                    print("Cantidad inválida.")
                    continue

                # buscar producto por id (mínimo, sin cambiar tu modelo)
                producto = None
                for p in self.catalogo.productos:
                    if p.product_id == pid:
                        producto = p
                        break

                if not producto:
                    print("Producto no encontrado.")
                    continue

                try:
                    cliente.carrito.agregar_item(producto, cantidad)
                    print("Producto agregado al carrito.")
                except ValueError as e:
                    print(e)

            elif opcion == "4":
                if not cliente.carrito.items:
                    print("Carrito vacío.")
                    continue

                print("\n--- CARRITO ---")
                for producto, cantidad in cliente.carrito.items.items():
                    subtotal = producto.price * cantidad
                    print(f"{producto.name} | x{cantidad} | ${producto.price} | Subtotal: ${subtotal}")

                print(f"TOTAL: ${cliente.carrito.calcular_total()}")

            elif opcion == "5":
                cliente.confirmar_compra()

            elif opcion == "0":
                break

            else:
                print("Opción inválida.")

    def mostrar_menu_admin(self, admin):
        while True:
            print("\n=== MENÚ ADMIN ===")
            print("1. Listar productos")
            print("2. Crear producto")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Guardar catálogo")
            print("0. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                admin.listar(admin.catalogo)

            elif opcion == "2":
                admin.crear_producto()

            elif opcion == "3":
                pid = input("ID producto a actualizar: ")
                name = input("Nuevo nombre (enter para mantener): ").strip()
                description = input("Nueva descripción (enter para mantener): ").strip()
                price_txt = input("Nuevo precio (enter para mantener): ").strip()
                stock_txt = input("Nuevo stock (enter para mantener): ").strip()

                updated_info = {}
                if name:
                    updated_info["name"] = name
                if description:
                    updated_info["description"] = description
                if price_txt:
                    try:
                        updated_info["price"] = float(price_txt)
                    except ValueError:
                        print("Precio inválido.")
                        continue
                if stock_txt:
                    try:
                        updated_info["stock"] = int(stock_txt)
                    except ValueError:
                        print("Stock inválido.")
                        continue

                admin.actualizar_producto(pid, updated_info)

            elif opcion == "4":
                pid = input("ID producto a eliminar: ")
                admin.eliminar_producto(pid)

            elif opcion == "5":
                admin.guardar_catalogo("catalogo.txt")

            elif opcion == "0":
                break

            else:
                print("Opción inválida.")
