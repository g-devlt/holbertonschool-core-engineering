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

    def __init__(self, sz: int):
        if not isinstance(sz, int):
            raise TypeError("size must be an integer")
        if sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz
