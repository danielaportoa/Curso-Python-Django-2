class Producto:
    def __init__(self, product_id, name, description, price, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, product_id):
        pass

    def actualizar_producto(self, product_id, updated_info):
        pass

    def buscar_producto(self, search_term):
        pass

    def listar_productos(self):
        pass

class Carrito:
    def __init__(self):
        self.items = {}  # key: producto, value: cantidad

    def agregar_item(self, producto, cantidad):
        pass

    def eliminar_item(self, product_id):
        pass

    def actualizar_cantidad(self, product_id, cantidad):
        pass

    def calcular_total(self):
        pass

class Usuario:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Cliente(Usuario):
    def __init__(self, name, age, email, customer_id):
        super().__init__(name, age, email)
        self.customer_id = customer_id
        self.purchase_history = []
    
class Admin(Usuario):
    def __init__(self, name, age, email, admin_id):
        super().__init__(name, age, email)
        self.admin_id = admin_id

    def listar_productos(self):
        pass

    def crear_producto(self, producto):
        producto_id = input("Ingrese el ID del producto: ")
        name = input("Ingrese el nombre del producto: ")
        description = input("Ingrese la descripción del producto: ")
        price = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        producto = Producto(producto_id, name, description, price, stock)
        return producto

    def actualizar_producto(self, product_id, updated_info):
        pass

    def eliminar_producto(self, product_id):
        pass

    def guardar_catalogo(self, filename):
        pass

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = Catalogo()
        self.usuarios = []

    def registrar_usuario(self, usuario):
        pass

    def iniciar_sesion(self, email):
        pass

    def mostrar_menu_cliente(self, cliente):
        pass

    def mostrar_menu_admin(self, admin):
        pass

ecommerce_tienda = Tienda("Mi Tienda Online")
juan_admin = Admin("Juan", 30, "juan@gmail.com", "admin001")