#!/usr/bin/python3
"""append function"""


def append_write(filename="", text=""):
    """Añade una cadena de texto al final de un
    archivo y devuelve el número de caracteres agregados."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
