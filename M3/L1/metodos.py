# ================================
# LISTAS (list)
# ================================
lista = [1, 2, 3]

lista.append(4)
lista.extend([5, 6])
lista.insert(0, 0)

lista.remove(3)
eliminado = lista.pop()
eliminado_index = lista.pop(0)

indice = lista.index(2)
conteo = lista.count(2)

lista.sort()
lista.reverse()

copia_lista = lista.copy()
lista.clear()


# ================================
# TUPLAS (tuple)
# ================================
tupla = (1, 2, 2, 3)

indice_tupla = tupla.index(2)
conteo_tupla = tupla.count(2)


# ================================
# CONJUNTOS (set)
# ================================
conjunto = {1, 2, 3}

conjunto.add(4)
conjunto.update([5, 6])

conjunto.remove(3)
conjunto.discard(10)  # no lanza error

elemento = conjunto.pop()

copia_set = conjunto.copy()

conjunto = {1, 2, 3, 4}
otro_set =          {4, 5, 6, 7}

union = conjunto.union(otro_set)
interseccion = conjunto.intersection(otro_set)
diferencia = conjunto.difference(otro_set)
diferencia = otro_set.difference(conjunto)
diferencia_simetrica = conjunto.symmetric_difference(otro_set)

conjunto.intersection_update(otro_set)
conjunto.difference_update(otro_set)
conjunto.symmetric_difference_update(otro_set)

es_subset = conjunto.issubset(otro_set)
es_superset = conjunto.issuperset(otro_set)
es_disjoint = conjunto.isdisjoint({100})

conjunto.clear()


# ================================
# DICCIONARIOS (dict)
# ================================
diccionario = {"a": 1, "b": 2}

diccionario["c"] = 3
diccionario.update({"d": 4})

valor = diccionario.get("a")
valor_default = diccionario.get("x", 0)

claves = diccionario.keys()
valores = diccionario.values()
items = diccionario.items()

eliminado = diccionario.pop("b")
eliminado_item = diccionario.popitem()

existe = "a" in diccionario

copia_dict = diccionario.copy()

diccionario.setdefault("e", 5)

diccionario.clear()


# ================================
# STRING (str)
# ================================
texto = " Python es genial "

texto_mayus = texto.upper()
texto_minus = texto.lower()
texto_cap = texto.capitalize()
texto_titulo = texto.title()

texto_strip = texto.strip()
texto_lstrip = texto.lstrip()
texto_rstrip = texto.rstrip()

texto_replace = texto.replace("genial", "poderoso")

texto_split = texto.split()
texto_join = "-".join(["python", "rocks"])

empieza = texto.startswith(" Python")
termina = texto.endswith(" ")

posicion = texto.find("es")
conteo_letra = texto.count("o")

es_numero = "123".isdigit()
es_letra = "abc".isalpha()
es_alnum = "abc123".isalnum()


# ================================
# OPERACIONES COMUNES
# ================================
longitud = len([1, 2, 3])
maximo = max([1, 5, 2])
minimo = min([1, 5, 2])
suma = sum([1, 2, 3])

ordenado = sorted([3, 1, 2])

enumerado = list(enumerate(["a", "b", "c"]))
zippeado = list(zip([1, 2], ["a", "b"]))

convertir_lista = list("abc")
convertir_set = set([1, 1, 2])
convertir_tupla = tuple([1, 2, 3])
convertir_dict = dict(a=1, b=2)
