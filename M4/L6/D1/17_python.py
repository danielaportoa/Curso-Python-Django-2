# Ejemplo 17: Control fino de codificación y errores

texto = "café ☕"

with open("M4\\L6\\D1\\data\\salida_latin1.txt", "w", encoding="latin-1", errors="replace") as f:
#with open("M4\\L6\\D1\\data\\salida_utf8.txt", "w", encoding="utf-8", errors="replace") as f:
    # 'errors="replace"' evita fallos de codificación
    f.write(texto)
