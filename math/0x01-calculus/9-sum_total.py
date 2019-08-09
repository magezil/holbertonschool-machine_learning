#!/usr/bin/env python3
"""Implement summation_i_squared function"""


def summation_i_squared(n):
    """
        Calculates the sum of i^2 from i = 1 to n
        n: integer to stop sum

        Return: integer
    """
    if n <= 1:
        return n**2
    return n**2 + summation_i_squared(n - 1)
