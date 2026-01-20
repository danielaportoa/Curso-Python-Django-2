from .producto import Producto


class Catalogo:
    def __init__(self):
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def eliminar_producto(self, product_id):
        for producto in self.productos:
            if producto.product_id == product_id:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        raise ValueError("Producto no encontrado")

    def actualizar_producto(self, product_id, updated_info):
        for producto in self.productos:
            if producto.product_id == product_id:
                producto.set_info(**updated_info)
                print("Producto actualizado correctamente.")
                return
        raise ValueError("Producto no encontrado")

    def buscar_producto(self, search_term):
        resultados = []
        for producto in self.productos:
            if search_term.lower() in producto.name.lower():
                resultados.append(producto)
        return resultados

    def listar_productos(self):
        if not self.productos:
            print("Catálogo vacío")
            return

        for producto in self.productos:
            print(f"{producto.product_id} | {producto.name} | ${producto.price} | Stock: {producto.stock}")
