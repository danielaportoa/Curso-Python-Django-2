frutas_precios = {"manzana": 500, "pera": 600, "naranja": 450}

# Por defecto
for default in frutas_precios:
    print("Fruta:", default)

# Por Items Clave y Valor
for fruta, precio in frutas_precios.items():
    print(f"{fruta} cuesta {precio}")

# Por Clave
for fruta in frutas_precios.keys():
    print("Fruta:", fruta)

# Por Valor
for precio in frutas_precios.values():
    print("Precio:", precio)