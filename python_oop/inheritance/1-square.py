#!/usr/bin/env python3
"""A module that implements the interface BaseGeometry
into the Square class
"""

BaseGeometry = __import__("base_geometry").BaseGeometry


class Square(BaseGeometry):
    """A simple class that implements BaseGeometry
    """

    def area(self) -> int:
        """Returns the area of this shape
        """
        return self.__size ** 2

    def __init__(self, size: int):
        super().__init__(self, size, size)

if __name__ == "__main__":
    sq = Square(10, 10)
    print(sq.area())
