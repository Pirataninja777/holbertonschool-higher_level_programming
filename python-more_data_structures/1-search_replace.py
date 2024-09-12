#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Crear una nueva lista donde se reemplazan
    # los elementos iguales a 'search' por 'replace'
    return [replace if element == search else element for element in my_list]

