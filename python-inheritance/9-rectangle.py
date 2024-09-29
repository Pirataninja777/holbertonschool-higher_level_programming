#!/usr/bin/python3
"""
Class BaseGeometry
Full Rectangle Implementation
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""superclass import """


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGeometry.
    Represents a rectangle with width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: Informal string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

