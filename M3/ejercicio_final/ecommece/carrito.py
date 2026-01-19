from data import carrito


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
