#!/usr/bin/python3
"""System-specific parameters and functions"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import os

"""Nombre del archivo donde se guardará la lista"""
filename = "add_item.json"

"""Inicializa la lista"""
items = []

"""Si el archivo ya existe, carga el contenido en la lista"""
if os.path.exists(filename):
    items = load_from_json_file(filename)

"""Añade los argumentos (excluyendo
el nombre del script) a la lista"""
items.extend(sys.argv[1:])

"""Guarda la lista en el archivo JSON"""
save_to_json_file(items, filename)
