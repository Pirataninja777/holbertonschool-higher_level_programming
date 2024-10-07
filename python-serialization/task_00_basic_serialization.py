#!/usr/bin/python3
import json
"""basic serialization module"""


def serialize_and_save_to_file(data, filename):
    """
    Serializa un diccionario de Python y lo guarda en un archivo JSON.

    Parámetros:
        data (dict): Un diccionario de Python con los datos a serializar.
        filename (str): El nombre del archivo de salida JSON. Si el
        archivo ya existe, será reemplazado.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as archivo_json:
            json.dump(data, archivo_json, indent=4)
        print(f"Los datos han sido serializados y guardados en '{filename}'.")
    except Exception as e:
        print(f"Ocurrió un error al serializar y guardar los datos: {e}")


def load_and_deserialize(filename):
    """
    Carga y deserializa datos desde un archivo JSON para recrear el
    diccionario de Python original.

    Parámetros:
        filename (str): El nombre del archivo JSON de entrada.

    Retorna:
        dict: Un diccionario de Python con los datos
        deserializados del archivo.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
        print(f"Datos cargados y deserializados desde '{filename}'.")
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: El archivo '{filename}' no contiene un JSON válido.")
        return {}
    except Exception as e:
        print(f"Ocurrió un error al cargar y deserializar los datos: {e}")
        return {}
