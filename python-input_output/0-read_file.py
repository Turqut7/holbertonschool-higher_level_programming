#!/usr/bin/python3
"""Module that reads a file and prints its content."""


def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
