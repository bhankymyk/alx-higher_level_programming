#!/usr/bin/python3
""""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """it inherit from base geometry class"""
    def __init__(self, width, height):

        """initialization
        Args:
            width (int): width
            height (int): height
        """
        self.integer_validator("width, width")
        self.__width = width
        self.integer_validator("height, height")
        self.__height = height
