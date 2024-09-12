#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # verificar si indice esta dentro del rango
            if i < len(my_list):
            # Intentamos imprimir el valor en la posición i
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except (ValueError, TypeError):
        # Capturamos cualquier excepción que ocurra
        pass
    print()  # Imprime una nueva línea después de todos los enteros
    return count
