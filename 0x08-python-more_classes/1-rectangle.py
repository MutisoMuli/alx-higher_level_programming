#!/usr/bin/python3
""" A class that defines a rectangle"""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            Width: represents the width of the rectangle.
            height: represents the height of the rectangle.
        Raises:
            TypeError: If size is not integer.
            ValueError: If size is less than zero
        """
        self.width = width
        self.height = height

        @property
        def height(self):
            """retrieves height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets height attribute"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

