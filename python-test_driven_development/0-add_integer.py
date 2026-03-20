#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if a is not an integer or float
        TypeError: if b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
