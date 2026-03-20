#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix: list of lists of integers/floats
        div: integer or float

    Returns:
        New matrix with all values divided by div, rounded to 2 decimals

    Raises:
        TypeError: if matrix is invalid
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(len(row) > 0 for row in matrix) or
            not all(all(isinstance(x, (int, float)) for x in row)
                    for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in row] for row in matrix]
