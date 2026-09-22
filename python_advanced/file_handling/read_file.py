#!/usr/bin/env python3
"""This modules provides a function
that reads and returns the content of a file
"""

def read_file(filename=""):
    """Reads and returns the content of a file
    """
    with open(filename) as f:
        print(f.read(), end="")


if __name__ == "__main__":
    print(read_file(__file__))
