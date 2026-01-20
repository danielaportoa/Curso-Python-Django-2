from .models.catalogo import Catalogo
from .models.usuario import Usuario
from .models.admin import Admin
    

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = Catalogo()
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def iniciar_sesion(self, email):
        pass

    def mostrar_menu_cliente(self, cliente):
        pass

    def mostrar_menu_admin(self, admin):
        pass

ecommerce_tienda = Tienda("Mi Tienda Online")
juan = Usuario("Juan", 30, "juan@gmail.com")
juan_admin = Admin("admin001", ecommerce_tienda.catalogo, juan)
ecommerce_tienda.registrar_usuario(juan_admin)
juan_admin.crear_producto()
juan_admin.listar(juan_admin.catalogo)