from .producto import Producto

class Carrito:
    def __init__(self):
        self.items: dict[Producto, int] = {}

    def agregar_item(self, producto: Producto, cantidad: int):
        pass

    def eliminar_item(self, product_id):
        pass

    def actualizar_cantidad(self, product_id, cantidad):
        pass

    def calcular_total(self):
        pass