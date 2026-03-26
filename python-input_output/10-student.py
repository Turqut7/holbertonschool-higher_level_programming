#!/usr/bin/python3
"""Module that defines a Student class with JSON filtering."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, optionally filtered."""
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__
