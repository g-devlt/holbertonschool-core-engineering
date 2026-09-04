#!/usr/bin/env python3

def print_list_integer(my_list=[]):
    if (not isinstance(my_list, list)):
        return
    [print("{:d}".format(x)) for x in my_list]


if __name__ == "__main__":
    print_list_integer([1, 2, 3, 4, 5, -1, 3, 6, 0])
