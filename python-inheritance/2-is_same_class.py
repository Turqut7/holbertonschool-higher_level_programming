#!/usr/bin/python3
"""is_same_class module."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    return type(obj) is a_class
