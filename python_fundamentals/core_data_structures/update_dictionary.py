#!/usr/bin/env python3


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    d = {
        "name": "Jacques",
        "age": 19,
        "code": ['C/C++', 'Py', 'JS']
    }
    print(d)
    print(update_dictionary(d, 'a', 'lpha'))
    print(update_dictionary(d, 'name', 'Gabriel'))