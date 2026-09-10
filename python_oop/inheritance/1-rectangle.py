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
        return self.__width * self.__height

    def __init__(self, width: int, height: int):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)
    
if __name__ == "__main__":
    rect = Rectangle(10, 10)
    print(rect.area())
    print(rect)
