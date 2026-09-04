#!/usr/bin/env python3

def element_at(my_list, idx):
    try:
        return my_list[idx] if idx >= 0 else None
    except:
        return None


if __name__ == "__main__":
    print(element_at([1, 2], 2))
    print(element_at([1, 2], -1))
    print(element_at([1, 2, 3], 2))
    print(element_at([], 2))