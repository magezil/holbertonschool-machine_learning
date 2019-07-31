#!/usr/bin/env python3


def matrix_transpose(matrix):
    """
        Get the transpose of a 2D matrix
        matrix: matrix to calculate

        Return: 2D transpose of matrix
    """
    new_matrix = []
    
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i == 0:
                new_matrix.append([])
            new_matrix[j].append(col)

    return new_matrix
