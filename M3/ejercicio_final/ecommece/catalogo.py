from data import productos_disponibles
from ui import mostrar_producto


def ver_productos():
    for product_id, producto in productos_disponibles.items():
        mostrar_producto(product_id, producto)
