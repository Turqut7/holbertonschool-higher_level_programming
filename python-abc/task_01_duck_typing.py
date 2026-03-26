#!/usr/bin/python3
"""Module for Shape, Circle, Rectangle and shape_info."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Abstract method area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Init circle."""
        self.radius = radius

    def area(self):
        """Circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Init rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Duck typing shape_info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
