#!/usr/bin/python3
"""MyList module."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort).
        Assumes all elements in the list are of the same type (integers).
        """
        print(sorted(self))
