#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes using ABC."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of circle: π * r²"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter of circle: 2 * π * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle: width * height"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle: 2 * (width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function that demonstrates duck typing.
    It accepts any object that has area() and perimeter() methods.
    No type checking is performed.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Test kodunu main faylda istifadə etmək üçün yalnız funksiyaları və classları export edirik
if __name__ == "__main__":
    # Test üçün (main fayl bunu import edəcək)
    pass
