# Utils - Utilidades.
# Creador: Yoruguin Lopez
# Creado: 2023-04-26
# Actualiza: Yorguin Lopez
# Actualizado: 2023-04-27
import os
import json

# Carga datos desde archivos con formato JSON
def cargar_datos(nombre_archivo):
    ruta_archivo = os.path.join('datos', nombre_archivo)
    try:
        with open(ruta_archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Guarda datos en formato JSON
def guardar_datos(datos, nombre_archivo):
    ruta_archivo = os.path.join('datos', nombre_archivo)
    with open(ruta_archivo, 'w') as f:
        json.dump(datos, f)
