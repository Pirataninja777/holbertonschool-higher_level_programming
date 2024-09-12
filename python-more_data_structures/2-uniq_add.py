#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convertir la lista a un conjunto
    # para eliminar duplicados y luego sumar sus elementos
    return sum(set(my_list))
