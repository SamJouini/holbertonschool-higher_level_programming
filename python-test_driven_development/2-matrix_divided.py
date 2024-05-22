#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists representing the matrix.
        div (int or float): The number to divide the matrix elements by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If matrix is empty.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list: A new matrix with all elements divided
        by div and rounded to 2 decimal places.
    """
    # TypeError: If matrix is not a list of lists of integers or floats.
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    # TypeError: If matrix is empty.
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    # TypeError: If each row of the matrix does not have the same size.
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # TypeError: If div is not a number (integer or float).
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # ZeroDivisionError: If div is equal to 0.
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            # TypeError: If elements of the matrix are numbers"
            if not isinstance(elem, int):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            new_row += [round(elem / div, 2)]
        new_matrix.append(new_row)

    return new_matrix
