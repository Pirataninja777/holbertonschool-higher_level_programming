#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Verificar si el índice es negativo
    # o fuera del rango de la lista
    if idx < 0 or idx >= len(my_list):
        # Si el índice no es válido,
        # devolver la lista sin cambios
        return my_list

    # Si el índice es válido, eliminar
    # el elemento en la posición idx
    # Utilizamos el operador de "rebanado"
    # para crear una nueva lista
    # excluyendo el elemento en la posición idx.
    return my_list[:idx] + my_list[idx + 1:]
