#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Intentamos imprimir el valor como entero
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Si ocurre un ValueError o TypeError, no es un entero
        return False

