#!/usr/bin/env python3
"""A module that implements the interface BaseGeometry
into the Square class
"""

Rectangle = __import__("1-rectangle").Rectangle


class Square(Rectangle):
    """A simple class that implements BaseGeometry
    """

    def area(self) -> int:
        """Returns the area of this shape
        """
        return self.__size ** 2

    def __init__(self, size: int):
        self.integer_validator(size)
        self.__size = size
        super().__init__(self, size, size)


if __name__ == "__main__":
    sq = Square(10, 10)
    print(sq.area())
