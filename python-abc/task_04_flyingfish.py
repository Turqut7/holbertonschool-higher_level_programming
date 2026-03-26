#!/usr/bin/python3
"""Module that defines Fish, Bird and FlyingFish classes."""


class Fish:
    """Fish class."""

    def swim(self):
        """Fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class with multiple inheritance."""

    def swim(self):
        """Override swim."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat."""
        print("The flying fish lives both in water and the sky!")
