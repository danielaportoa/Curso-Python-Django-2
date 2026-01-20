from .usuario import Usuario
from .catalogo import Catalogo
from .producto import Producto


class Admin(Usuario):
    def __init__(self, admin_id, catalogo: Catalogo, usuario):
        super().__init__(usuario.name, usuario.age, usuario.email)
        self.admin_id = admin_id
        self.catalogo = catalogo

    def listar(self, catalogo: Catalogo):
        catalogo.listar_productos()

    def crear_producto(self):
        producto_id = input("Ingrese el ID del producto: ")
        name = input("Ingrese el nombre del producto: ")
        description = input("Ingrese la descripción del producto: ")

        try:
            price = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
        except ValueError:
            print("Precio o stock inválido.")
            return

        producto = Producto(producto_id, name, description, price, stock)
        self.catalogo.agregar_producto(producto)

    def actualizar_producto(self, product_id, updated_info):
        try:
            self.catalogo.actualizar_producto(product_id, updated_info)
        except ValueError as e:
            print(e)

    def eliminar_producto(self, product_id):
        try:
            self.catalogo.eliminar_producto(product_id)
        except ValueError as e:
            print(e)

    def guardar_catalogo(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for producto in self.catalogo.productos:
                    f.write(
                        f"{producto.product_id},{producto.name},{producto.description},{producto.price},{producto.stock}\n"
                    )
            print("Catálogo guardado correctamente.")
        except OSError:
            print("Error al guardar el archivo.")
