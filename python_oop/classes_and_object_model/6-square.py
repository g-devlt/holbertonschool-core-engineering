#!/usr/bin/env python3

class Square():

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) and not len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integer")
        if (not isinstance(value[0], int) and not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    @size.setter
    def size(self, sz):
        if not isinstance(sz, int):
            raise TypeError("size must be an integer")
        if sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz

    def area(self):
        return self.__size ** 2

    def my_print(self):
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
