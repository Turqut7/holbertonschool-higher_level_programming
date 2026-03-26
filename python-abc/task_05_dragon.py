#!/usr/bin/python3
"""Module that defines mixins and Dragon class."""


class SwimMixin:
    """Mixin for swimming capability."""

    def swim(self):
        """Swim method."""
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying capability."""

    def fly(self):
        """Fly method."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with multiple abilities."""

    def roar(self):
        """Roar method."""
        print("The dragon roars!")
