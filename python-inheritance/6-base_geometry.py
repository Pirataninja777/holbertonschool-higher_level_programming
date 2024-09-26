#!/usr/bin/python3
"""more Geometry"""


class BaseGeometry:
    """
    A class named BaseGeometry with an area method that is not implemented.
    """
    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
