#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    for i in range(x):
        try:
            # Intenta imprimir el elemento como entero
            print("{:d}".format(my_list[i]), end="")
            elements += 1
        except (ValueError, TypeError):
            # Captura el caso de índice fuera de rango
            # y errores de tipo
            continue
    print("")  # Imprime un salto de línea al final
    return elements
