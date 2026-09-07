#!/usr/bin/env python3

class Rectancle():

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, sz):
        if not isinstance(sz, int):
            raise TypeError("width must be an integer")
        if sz < 0:
            raise ValueError("width must be >= 0")
        self.__width = sz

    @height.setter
    def height(self, sz):
        if not isinstance(sz, int):
            raise TypeError("height must be an integer")
        if sz < 0:
            raise ValueError("height must be >= 0")
        self.__height = sz

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height


if __name__ == "__main__":
    rec1 = Rectancle(1, 2)