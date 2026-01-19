productos_disponibles = {
    1: {"nombre": "producto1", "categoria": "ropa", "precio": 3000},
    2: {"nombre": "producto2", "categoria": "tecnologia", "precio": 10000},
    3: {"nombre": "producto3", "categoria": "ropa", "precio": 5000},
    4: {"nombre": "producto4", "categoria": "hogar", "precio": 8000},
    5: {"nombre": "producto5", "categoria": "tecnologia", "precio": 22000},
}

carrito = []


def mostrar_producto(product_id, producto):
    print(
        f"ID: {product_id} | "
        f"Nombre: {producto['nombre']} | "
        f"Precio: {producto['precio']}"
    )


def ver_productos():
    for product_id, producto in productos_disponibles.items():
        mostrar_producto(product_id, producto)


def buscar():
    opcion = int(
        input(
            "Desea buscar por Nombre (1) o por Categoría (2): "
        )
    )

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
    product_id = int(
        input("Ingresa el ID del producto seleccionado: ")
    )

    if product_id not in productos_disponibles:
        print("ID de producto inválido.")
        return

    cantidad = int(
        input("Ingrese cantidad del producto: ")
    )

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    producto = productos_disponibles[product_id]
    carrito.append(
        (producto["nombre"], producto["precio"], cantidad)
    )
    print("Producto agregado al carrito.")


def ver_carrito_total():
    if not carrito:
        print("Carrito vacío.")
        return

    total = 0
    for nombre, precio, cantidad in carrito:
        subtotal = precio * cantidad
        total += subtotal
        print(
            f"Nombre: {nombre} | "
            f"Precio: {precio} | "
            f"Cantidad: {cantidad} | "
            f"Subtotal: {subtotal}"
        )

    print(f"Total a pagar: {total}")


def vaciar_carrito():
    carrito.clear()
    print("Carrito vaciado.")


while True:
    print(
        "\nBienvenido/a a tu Ecommerce\n"
        "1) Ver catálogo de productos\n"
        "2) Buscar producto por nombre o categoría\n"
        "3) Agregar producto al carrito\n"
        "4) Ver carrito y total\n"
        "5) Vaciar carrito\n"
        "0) Salir"
    )

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        ver_productos()
    elif opcion == 2:
        buscar()
    elif opcion == 3:
        ver_productos()
        agregar()
    elif opcion == 4:
        ver_carrito_total()
    elif opcion == 5:
        vaciar_carrito()
    elif opcion == 0:
        print("Gracias por visitar nuestro Ecommerce. ¡Hasta luego!")
        break
    else:
        print("Opción incorrecta.")
