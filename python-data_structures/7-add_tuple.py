#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Desempaquetar los primeros dos elementos de las tuplas,
    # usando 0 por defecto si faltan valores
    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]

    # Empaquetar los resultados en una nueva tupla
    return (a1 + b1, a2 + b2)
