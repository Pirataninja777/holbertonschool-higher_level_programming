#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Crear una nueva matriz, aplicando la operación
    # de elevar al cuadrado cada elemento
    return [[element ** 2 for element in row] for row in matrix]
