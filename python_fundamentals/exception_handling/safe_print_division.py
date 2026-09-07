#!/usr/bin/env python3

def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except Exception:
        return None
    finally:
        if res is not None:
            print("Inside result: {:.1f}".format(res))
        else:
            print("Inside result: None")
    return res


if __name__ == "__main__":
    print(safe_print_division(1, 2))
    print(safe_print_division(1, 0))
    print(safe_print_division(1, 10))
