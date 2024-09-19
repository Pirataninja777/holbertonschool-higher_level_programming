#!/usr/bin/python3
"""
Este modulo contiene una funcion que suma dos enteros.
"""


def add_integer(a, b=98):
    """
    Suma dos enteros o flotantes y retorna el resultado como entero.
    Si a o b son flotantes, los convierte a enteros antes de la suma.

    Args:
        a (int, float): El primer número a sumar.
        b (int, float, opcional): El segundo número a sumar (por defecto 98).

    Returns:
        int: La suma de a y b convertida a entero.

    Raises:
        TypeError: Si a o b no son enteros ni flotantes.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convertir a y b a enteros si son flotantes
    a = int(a)
    b = int(b)
    # Retornar la suma de a y b
    return a + b
