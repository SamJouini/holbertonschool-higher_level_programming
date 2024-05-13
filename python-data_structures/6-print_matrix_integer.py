#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = ""
        for col in row:
            row_str += "{:d}".format(col) + " "
        print(row_str.strip())
