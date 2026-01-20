from .producto import Producto


class Catalogo:
    def __init__(self):
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def eliminar_producto(self, product_id):
        pass

    def actualizar_producto(self, product_id, updated_info):
        pass

    def buscar_producto(self, search_term):
        pass

    def listar_productos(self):
        boleta = input("Nombre de la boleta: ")
        with open(f"{boleta}.txt", "w", encoding="utf-8") as f:
            for producto in self.productos:
                f.write(f"{producto.product_id}: {producto.name} - ${producto.price} (Stock: {producto.stock})")
                f.write("=====================================\n")
                f.write("            BOLETA DE VENTA           \n")
                f.write("=====================================\n")