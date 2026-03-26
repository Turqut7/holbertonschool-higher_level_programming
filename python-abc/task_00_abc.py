#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Subclass representing a dog."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
