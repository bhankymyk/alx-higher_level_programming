#!/usr/bin/python3
"""
Contains the class BaseGemetry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represent a Square"""

    def __init__(self, size):
        """A representation of a new square
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
