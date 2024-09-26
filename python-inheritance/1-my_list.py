#!/usr/bin/python3
"""a class that inherits from list"""


class MyList(list):
    """
    A subclass of list that has a method to print the
    list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order (sorted).
        Assumes that all elements in the list are integers.
        """
        print(sorted(self))
