#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        result.append(new_row)
    return result
