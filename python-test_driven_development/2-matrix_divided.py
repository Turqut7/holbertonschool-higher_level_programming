#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): list of lists of integers/floats
        div (int/float): divisor

    Returns:
        list: new matrix with divided values rounded to 2 decimals

    Raises:
        TypeError: if matrix is invalid or div is not a number
        ZeroDivisionError: if div is zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix == [[]]:
        return [[]]

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(item, (int, float)) for item in row)
                    for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
