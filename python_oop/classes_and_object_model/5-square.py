#!/usr/bin/env python3
"""This module is used for defining the Square class.
The square class allows for multiple different patterns of use
mostly a structure of data with helper functions
@author g-devlt
"""


class Square():
    """The square class is the main attraction of
    the module, bascially a helper class for geometry
    """

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, sz):
        if not isinstance(sz, int):
            raise TypeError("size must be an integer")
        if sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz

    def area(self):
        """Returns the area of the square
        basically : length*length
        """
        return self.__size ** 2

    def my_print(self):
        """A pretty print function for the
        square class
        """
        if (self.size == 0):
            print()
        else:
            for y in range(self.size):
                print("#" * self.size)

    def __init__(self, sz: int = 0):
        self.size = sz


if __name__ == "__main__":
    sq = Square(10, (2, 3))
    try:
        sq = Square(-1)
    except Exception as e:
        print(e)
    try:
        sq = Square("Abc")
    except Exception as e:
        print(e)
    sq.my_print()
