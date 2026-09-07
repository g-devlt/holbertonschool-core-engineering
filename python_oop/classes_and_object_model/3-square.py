#!/usr/bin/env python3

class Square():
    __size: int

    def area(self):
        return self.__size ** 2

    def __init__(self, sz: int):
        if not isinstance(sz, int):
            raise TypeError("size must be an integer")
        if sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz
