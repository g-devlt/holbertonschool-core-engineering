#!/usr/bin/env python3

def common_elements(set_1, set_2):
    if(not (isinstance(set_1, set) and isinstance(set_2, set))):
        return None
    return set_1 & set_2


if __name__ == "__main__":
    print(common_elements({1, 2, 3}, {3, 4, 5}))
    print(common_elements({0, 1, 100}, {100, 0, 1}))
