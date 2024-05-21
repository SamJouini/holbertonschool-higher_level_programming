#!/usr/bin/python3
"Divides all elements of a matrix by a given number"


def matrix_divided(matrix, div):
    "TypeError: If matrix is not a list of lists of integers or floats."
    if not isinstance(matrix, list)
    or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix of integers/floats")

    "TypeError: If each row of the matrix does not have the same size."
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    "TypeError: If div is not a number (integer or float)."
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    "ZeroDivisionError: If div is equal to 0."
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
    """Returns: a new matrix with all elements divided
    by div and rounded to 2 decimal places."""
