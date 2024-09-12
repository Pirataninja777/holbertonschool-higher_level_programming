#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Devuelve un nuevo diccionario
    # con todos los valores multiplicados por 2.
    # Parámetros:
    # a_dictionary (dict): El diccionario con los
    # valores a multiplicar.
    # Retorna: dict: Un nuevo diccionario con los
    # valores multiplicados por 2.
    return {key: value * 2 for key, value in a_dictionary.items()}
