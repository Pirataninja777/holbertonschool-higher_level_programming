#!/usr/bin/python3
"""Define a Square class with a private size attribute."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
