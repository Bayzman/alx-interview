#!/usr/bin/env python3

""" N-Queens puzzle """

import sys


def is_safe(row, col, queens):
    """ Check if a queen can be placed in a given row and column """
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(row, N, queens, solutions):
    """ Solve the N-Queens puzzle """
    if row == N:
        solutions.append(queens[:])
        return
    for col in range(N):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve_nqueens(row + 1, N, queens, solutions)
            queens.pop()  # Backtrack


def main():
    """ Main function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = []
    solutions = []
    solve_nqueens(0, N, queens, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
