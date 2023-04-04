#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    def __init__(self, width=0, height=0):
        """initializing the rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero"""
            self.width = width
            self.height = height

    @property
    def width(self):
        """retrieves width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves height attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height attributes"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0)
        else:
            self.__height = value 
