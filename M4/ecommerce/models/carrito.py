from .producto import Producto


class Carrito:
    def __init__(self):
        self.items: dict[Producto, int] = {}

    def agregar_item(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")

        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad

    def eliminar_item(self, product_id):
        for producto in list(self.items.keys()):
            if producto.product_id == product_id:
                del self.items[producto]
                return
        raise ValueError("Producto no encontrado en el carrito")

    def actualizar_cantidad(self, product_id, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")

        for producto in self.items:
            if producto.product_id == product_id:
                self.items[producto] = cantidad
                return
        raise ValueError("Producto no encontrado")

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.items.items():
            total += producto.price * cantidad
        return total
