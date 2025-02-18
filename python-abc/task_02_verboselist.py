#!/usr/bin/env python3

class VerboseList(list):
    """
    Clase que extiende la clase lista de Python para agregar
    comportamientos personalizados con notificaciones cada vez
    que se realiza una modificación en la lista.
    """

    def append(self, item):
        """
        Agrega un elemento a la lista y muestra un mensaje de notificación.

        :param item: Elemento a agregar a la lista.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extiende la lista con los elementos de un iterable y muestra un
        mensaje de notificación indicando cuántos elementos fueron agregados.

        :param iterable: Un iterable cuyos elementos serán agregados a lalista.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Elimina el primer elemento de la lista que coincide con el valor
        especificado y muestra un mensaje de notificación.

        :param item: Elemento a eliminar de la lista.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Elimina y retorna un elemento de la lista en el índice especificado,
        mostrando un mensaje de notificación con el valor del elemento.

        :param index: Índice del elemento a eliminar. Si no se especifica,
                      se elimina el último elemento.
        :return: El elemento eliminado de la lista.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
