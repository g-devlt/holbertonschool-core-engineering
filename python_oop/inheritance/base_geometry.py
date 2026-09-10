#!/usr/bin/env python3
"""A module that defines the interface BaseGeometry:
"""

class BaseGeometry():
    """The interface that provides a building block and
    polymorphism to your projects !
    """

    def area(self):
        """Returns the area of this shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks wether a value is a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    