#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except Exception:
            pass
        else:
            length += 1
    print()
    return length


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(safe_print_list_integers(lst, 5))
