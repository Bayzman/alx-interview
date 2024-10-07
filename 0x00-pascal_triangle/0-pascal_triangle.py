#!/usr/bin/python3

""" Pascal's Triangle """


def pascal_triangle(n):
    """ Function to compute the Pascal Triangle upto n """
    if (n <= 0):
        return []
    else:
        pascal_t = [[1]]
        for i in range(1, n):
            next_row = [1]
            for j in range(1, i):
                next_row.append(pascal_t[i - 1][j - 1] + pascal_t[i - 1][j])
            next_row.append(1)
            pascal_t.append(next_row)
        return pascal_t
