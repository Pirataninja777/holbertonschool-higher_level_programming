#!/usr/bin/python3
"""Triangulo Pascal"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    :param n: The number of rows of Pascal's triangle to generate.
    :return: A list of lists representing Pascal's triangle.
    """
    triangle = []  # Initialize the triangle

    if n <= 0:
        return triangle  # Return an empty list if n <= 0

    for i in range(n):
        # Create a new row with all elements initialized to 0
        row = [0] * (i + 1)  # The i-th row has i + 1 elements
        row[0], row[-1] = 1, 1  # Set the first and last element to 1

        # Each triangle element (except the first and last) is the sum of
        # the two elements above it in the previous row.
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Append the row to the triangle

    return triangle  # Return the completed triangle
