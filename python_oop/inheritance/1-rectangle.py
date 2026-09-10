#!/usr/bin/env python3
"""A module that implements the interface BaseGeometry
into the Rectangle class
"""

BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A simple class that implements BaseGeometry
    """

    def area(self) -> int:
        """Returns the area of this shape
        """
        return self.width * self.height

    def __init__(self, width: int, height: int):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height


if __name__ == "__main__":
    rect = Rectangle(10, 10)
    print(rect.area())
