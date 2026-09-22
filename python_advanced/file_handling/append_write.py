#!/usr/bin/env python3
"""This modules provides a function
that appends data to a file
"""


def append_write(filename="", text=""):
    """Appends text to a
    provided file path
    """

    with open(filename, mode="a") as f:
        return f.write(text)


if __name__ == "__main__":
    append_write("README.md", "# Python : File Handling !\n")
