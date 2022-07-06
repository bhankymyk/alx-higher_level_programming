#!/usr/bin/python3
"""It implements a Square object"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implementation"""

    def __init__(self, size):
        """Initialization

        Args:
        size (int): size
        """

        super().__init__(size, size)
