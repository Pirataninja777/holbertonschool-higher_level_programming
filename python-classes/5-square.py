#!/usr/bin/python3
"""Define un cuadrado con un atributo privado, métodos de acceso y una
función para imprimir el cuadrado.

La clase `Square` permite la creación de un cuadrado con un tamaño opcional,
validado mediante getter y setter. También permite imprimir el cuadrado en la
salida estándar usando el carácter '#'.

Attributes:
    __size (int): Tamaño del cuadrado.
"""

class Square:
    """Representa un cuadrado.

    Attributes:
        __size (int): El tamaño del cuadrado.
    """

    def __init__(self, size=0):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int, opcional): El tamaño del cuadrado. Debe ser un entero
            no negativo. El valor predeterminado es 0.

        Raises:
            TypeError: Si `size` no es un entero.
            ValueError: Si `size` es menor que 0.
        """
        self.size = size

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado.

        Returns:
            int: El tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado.

        Args:
            value (int): El nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si `value` no es un entero.
            ValueError: Si `value` es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula el área del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado en la salida estándar usando el carácter '#'.

        Si el tamaño es 0, imprime una línea en blanco.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
