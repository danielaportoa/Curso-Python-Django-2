from data import productos_disponibles, carrito
from ui import mostrar_producto


def buscar():
    opcion = int(input("Desea buscar por Nombre (1) o por Categoría (2): "))

    if opcion == 1:
        buscando = input("Ingrese el nombre: ")
        for product_id, producto in productos_disponibles.items():
            if producto["nombre"] == buscando:
                mostrar_producto(product_id, producto)
                return
        print("Producto no encontrado.")

    elif opcion == 2:
        buscando = input("Ingrese la categoría: ")
        encontrado = False
        for product_id, producto in productos_disponibles.items():
            if producto["categoria"] == buscando:
                mostrar_producto(product_id, producto)
                encontrado = True
        if not encontrado:
            print("No hay productos en esa categoría.")

    else:
        print("Opción incorrecta.")


def agregar():
    product_id = int(input("Ingresa el ID del producto seleccionado: "))

    if product_id not in productos_disponibles:
        print("ID de producto inválido.")
        return

    cantidad = int(input("Ingrese cantidad del producto: "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    producto = productos_disponibles[product_id]
    carrito.append((producto["nombre"], producto["precio"], cantidad))
    print("Producto agregado al carrito.")
