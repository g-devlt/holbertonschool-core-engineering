#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            length += 1
    except IndexError:
        print()
    else:
        print()
    return length


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(safe_print_list(lst, 5))
