#!/usr/bin/python3

import sys


def is_it_safe(board, row, col, n):
    "Check if a queen can be placed on the board[row][col]"

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    "Use backtracking to find all solutions for the N queens problem"
    # If all queens are placed, return True
    if col == n:
        print_solution(board, n)
        return

    # Consider a column and try placing the queens in all rows one by one
    for i in range(n):
        if is_it_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens(board, col + 1, n)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # remove the queen from board[i][col]
            board[i][col] = 0


def print_solution(board, n):
    "Print the chessboard with the queens placed"
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()
    print()


def nqueens(n):
    "Solve the N queens problem"
    board = [[0 for j in range(n)] for i in range(n)]
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
