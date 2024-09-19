#!/usr/bin/python3
"""
This module define a square
"""


class Square:
    """
    Class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with optional size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square as a
            tuple of two positive integers (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square as a +integer.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square, ensuring it is
        a tuple of two positive integers.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 +integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
