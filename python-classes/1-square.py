#!/usr/bin/python3
"""Define a square class with a private size attribute."""

class Square:
    """Class that defines a square by size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
