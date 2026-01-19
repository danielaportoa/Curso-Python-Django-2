import os

ARCHIVO = "logs_grandes.txt"
TAMANIO_OBJETIVO_MB = 100
TAMANIO_OBJETIVO_BYTES = TAMANIO_OBJETIVO_MB * 1024 * 1024

linea_log = (
    "2026-01-19 09:15:01,234 INFO  "
    "[document.upload] Upload completed | "
    "document_id=af23d1c4 | user_id=1023 | duration=15.88s\n"
)

tam_linea = len(linea_log.encode("utf-8"))

with open(ARCHIVO, "w", encoding="utf-8") as f:
    bytes_escritos = 0
    while bytes_escritos < TAMANIO_OBJETIVO_BYTES:
        f.write(linea_log)
        bytes_escritos += tam_linea

print(f"Archivo '{ARCHIVO}' creado con tamaño aproximado de {bytes_escritos / (1024 * 1024):.2f} MB")
print(f"Tamaño real en disco: {os.path.getsize(ARCHIVO) / (1024 * 1024):.2f} MB")
