#!/usr/bin/python3
"""Define una clase Square con validación de tamaño."""

class Square:
    """Clase que define un cuadrado con un tamaño validado."""

    def __init__(self, size=0):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int, opcional): El tamaño del cuadrado. Debe ser un entero
            no negativo. El valor predeterminado es 0.

        Raises:
            TypeError: Si `size` no es un entero.
            ValueError: Si `size` es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
