#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Verificar si el índice es negativo
    # o fuera del rango de la lista
    if idx < 0 or idx >= len(my_list):
        # Si el índice no es válido,
        # devolver la lista sin cambios
        return my_list
# Usar del para eliminar el elemento en la posición idx
    del my_list[idx]
    # Retornar la lista modificada
    return my_list
