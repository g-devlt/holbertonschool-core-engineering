#!/usr/bin/env python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    return True


if __name__ == "__main__":
    print(safe_print_integer("aaa"))
    print(safe_print_integer(3))
    print(safe_print_integer("4"))
