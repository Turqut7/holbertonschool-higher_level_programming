#!/usr/bin/env python3
"""
Task 01: Duck Typing with Shapes
This module demonstrates duck typing and abstract base classes in Python.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, radius):
        """
        Initialize a circle with given radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of any shape object.
    
    This function uses duck typing - it doesn't check the type of the object,
    it just assumes the object has area() and perimeter() methods.
    
    Args:
        shape: Any object with area() and perimeter() methods
    """
    area_value = shape.area()
    perimeter_value = shape.perimeter()
    
    print(f"Area: {area_value}")
    print(f"Perimeter: {perimeter_value}")


# Test the implementation
if __name__ == "__main__":
    # Create instances of Circle and Rectangle
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)
    
    # Test shape_info with both objects
    shape_info(circle)
    shape_info(rectangle)
