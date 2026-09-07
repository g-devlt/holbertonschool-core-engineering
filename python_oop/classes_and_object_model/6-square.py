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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int) or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for off_y in range(self.position[1]):
                print()
            for y in range(self.size):
                print((" " * self.position[0]) + ("#" * self.size))

    def __init__(self, sz: int = 0, position: tuple[int, int] = (0, 0)):
        self.position = position
        self.size = sz

    def __str__(self):
        res = ""
        if (self.size == 0):
            res += "\n"
        else:
            for off_y in range(self.position[1]):
                res += "\n"
            for y in range(self.size):
                res += (" " * self.position[0]) + ("#" * self.size) + "\n"
        return res


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
    print(sq)
