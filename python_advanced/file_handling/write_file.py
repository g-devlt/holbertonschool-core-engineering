#!/usr/bin/env python3
"""This modules provides a function
that writes to a file
"""


def write_file(filename="", text=""):
    """Writes text to a 
    provided file path
    """

    with open(filename, mode="w") as f:
        return f.write(text)


if __name__ == "__main__":
    write_file("README.md", "# Python : File Handling !\n")
