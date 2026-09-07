#!/usr/bin/env python3

class Square():

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
        return self.__size ** 2


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
