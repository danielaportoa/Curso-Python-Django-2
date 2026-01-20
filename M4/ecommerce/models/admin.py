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
        price = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        producto = Producto(producto_id, name, description, price, stock)
        self.catalogo.agregar_producto(producto)

    def actualizar_producto(self, product_id, updated_info):
        pass

    def eliminar_producto(self, product_id):
        pass

    def guardar_catalogo(self, filename):
        pass