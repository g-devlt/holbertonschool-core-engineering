#!/usr/bin/env python3

def replace_in_list(my_list, idx, element):
    if (idx >= len(my_list) or idx < 0):
        return my_list
    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    print(x)
    print(replace_in_list(x, 1, -2))
    print(x)
