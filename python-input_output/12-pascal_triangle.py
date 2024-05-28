#!/usr/bin/python3
"""
Function that returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n - 1)
        prev_row = triangle[- 1]
        current_row = [1]

    for i in range(len(prev_row)-1):
        value = prev_row[i] + prev_row[i+1]
        current_row.append(value)

    current_row.append(1)
    triangle.append(current_row)
    return triangle
