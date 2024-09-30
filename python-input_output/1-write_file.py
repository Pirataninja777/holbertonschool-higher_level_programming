#!/usr/bin/python3
"""implementa funcion write_file"""


def write_file(filename="", text=""):
    """Escribe una cadena de texto en un archivo y devuelve
    el número de caracteres escritos."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
