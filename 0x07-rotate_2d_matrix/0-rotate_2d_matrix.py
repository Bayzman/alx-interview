#!/usr/bin/python3

""" Rotate a 2D square matrix 90 degrees clockwise """

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """" Rotate matrix 90 degrees clockwise """
    rows = len(matrix)

    for i in range(rows):
        for j in range(i + 1, rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
