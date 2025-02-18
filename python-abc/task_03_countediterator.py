#!/usr/bin/env python3

class CountedIterator:
    """
    Iterador que cuenta cuántos elementos han sido iterados.
    """

    def __init__(self, iterable):
        """
        Inicializa el iterador con un objeto iterable y un contador.

        :param iterable: El iterable sobre el que iteraremos (puede ser una lista, etc.).
        """
        self.iterator = iter(iterable)  # Convertir el iterable en un iterador
        self.count = 0  # Inicializar el contador

    def __next__(self):
        """
        Retorna el siguiente ítem del iterador y aumenta el contador.
        
        Si no hay más elementos, lanza StopIteration.
        """
        try:
            item = next(self.iterator)  # Obtener el siguiente ítem
            self.count += 1  # Incrementar el contador
            return item
        except StopIteration:
            raise StopIteration  # Lanzar StopIteration cuando no haya más ítems

    def get_count(self):
        """
        Devuelve el número de elementos que han sido iterados.
        """
        return self.count
