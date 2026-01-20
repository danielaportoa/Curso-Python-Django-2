from .usuario import Usuario
from .carrito import Carrito


class Cliente(Usuario):
    def __init__(self, name, age, email, customer_id):
        super().__init__(name, age, email)
        self.customer_id = customer_id
        self.purchase_history = []
        self.carrito = Carrito()

    def confirmar_compra(self):
        if not self.carrito.items:
            print("Carrito vacío, no se puede comprar.")
            return

        total = self.carrito.calcular_total()
        self.purchase_history.append(total)

        try:
            with open("ordenes.txt", "a", encoding="utf-8") as f:
                f.write(f"Cliente: {self.name} | Total: ${total}\n")
            print("Compra registrada correctamente.")
        except IOError:
            print("Error al registrar la compra.")

        self.carrito.items.clear()
