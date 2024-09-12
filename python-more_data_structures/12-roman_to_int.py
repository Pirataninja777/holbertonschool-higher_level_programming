#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Diccionario con los valores de los números romanos
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100,
                  'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    # Iterar sobre la cadena en orden inverso
    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)

        if value < prev_value:
            # Restar si el valor actual es menor
            # que el anterior (casos como IV, IX)
            total -= value
        else:
            # Sumar si es mayor o igual
            total += value

        # Actualizar el valor previo
        prev_value = value

    return total
