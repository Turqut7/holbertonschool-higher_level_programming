#!/usr/bin/python3
"""Square module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
