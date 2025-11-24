"""
PLANTILLA CRUD CON CSV — VERSION PARA EXAMEN
--------------------------------------------
Incluye:
- Cargar CSV
- Guardar CSV
- Crear / Leer / Actualizar / Eliminar
- Fusionar CSV
- Sobrescribir CSV
- Mostrar tabla tipo hoja de cálculo

Solo usa módulos estándar de Python.
"""

import csv


# ============================================================
# 1. CARGA Y GUARDADO DE ARCHIVOS CSV
# ============================================================

def cargar_csv(ruta):
    """
    Carga un archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un registro/filas del archivo.
    """
    registros = []
    try:
        with open(ruta, mode="r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                registros.append(dict(fila))  # Cada fila → dict
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
    return registros


def guardar_csv(ruta, registros):
    """
    Guarda la lista de registros (diccionarios) en un archivo CSV.
    Usa las claves del primer registro como encabezados.
    """
    if not registros:
        print("No hay registros para guardar.")
        return

    campos = list(registros[0].keys())  # Obtiene las columnas

    with open(ruta, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(registros)


# ============================================================
# 2. CRUD BÁSICO
# ============================================================

def generar_id(registros):
    """
    Genera un ID numérico consecutivo.
    """
    if not registros:
        return 1
    ids = [int(r["id"]) for r in registros]
    return max(ids) + 1


# CREATE
def agregar_registro(registros, name, price, quantity):
    """
    Crea un nuevo registro con ID automático y lo añade a la lista.
    """
    nuevo = {
        "id": str(generar_id(registros)),
        "name": str(name),
        "price": str(price),
        "quantity": str(quantity)
    }
    registros.append(nuevo)
    return registros


# READ
def buscar_por_id(registros, id_buscar):
    """
    Devuelve un registro con el ID indicado, o None si no existe.
    """
