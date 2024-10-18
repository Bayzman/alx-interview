#!/usr/bin/python3

""" Computes the minimum operations needed to result in exactly
    n H characters
"""


def minOperations(n):
    """ Computes minimum operations """
    operations = 0
    factor = 2

    if n < 0:
        return 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

        if factor * factor > n:
            if n > 1:
                operations += n
            break

    return operations
