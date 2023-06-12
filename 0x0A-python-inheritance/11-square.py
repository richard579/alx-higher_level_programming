#!/usr/bin/python3
"""11-square: class square from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle
    Attributes:
        size (int): side of square
    Methods:
        __init__ initializes the square
    """
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Returns the area of square"""
        area = self.__size * self.__size
        return area

    def __str__(self):
        """Returns a string of square details"""
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))
