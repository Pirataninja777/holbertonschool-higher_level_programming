#!/usr/bin/python3
"""
Class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle
"""Superclass import """


class Square(Rectangle):
    """
    Class Square inherits from Rectangle.
    Represents a square with a specific size.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        super().integer_validator("size", size)  # Validate size
        self.__size = size                       # Private attribute

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: Informal string representation of the square.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
