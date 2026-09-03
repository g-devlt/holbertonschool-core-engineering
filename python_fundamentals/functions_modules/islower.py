#!/usr/bin/env python3

def islower(c):
    """Checks wether an object is a lowercase character"""
    if (isinstance(c, str) and len(c) == 1):
        return ord('a') <= ord(c) <= ord('z')
    return False


if __name__ == "__main__":
    print("'a'  :", islower('a'))
    print("'f'  :", islower('f'))
    print("'z'  :", islower('z'))
    print("'A'  :", islower('A'))
    print("'Z'  :", islower('Z'))
    print("'-'  :", islower('-'))
    print("'3'  :", islower('3'))
    print("3    :", islower(3))
    print("None :", islower(None))
