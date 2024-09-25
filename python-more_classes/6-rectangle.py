#!/usr/bin/python3
"""
Rectangle module
Defines a Rectangle class with tracking of instances.
"""


class Rectangle:
    """Defines a rectangle by width and height with area, perimeter,
    string representation, eval support, and deletion message.

    Class Attributes:
        number_of_instances (int): Tracks the number of instances created
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height.
        Also increments number_of_instances.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        Returns:
            0 if either width or height is 0, otherwise returns
            2 * (width + height).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle using
        the '#' character.

        If width or height is 0, it returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle to be
        able to recreate a new instance using eval().

        Format: Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted and
        decrements the instance count.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
