#!/usr/bin/python3
"""9-rectangle: class rectangle from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry
    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    Methods:
        __init__ initializes the Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Returns a string of rectangle details"""
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
