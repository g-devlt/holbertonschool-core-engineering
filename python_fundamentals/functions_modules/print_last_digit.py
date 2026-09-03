#!/usr/bin/env python3

def print_last_digit(number):
    print(x := number % 10 if number >= 0 else (-number) % 10, end='')
    return x


if __name__ == "__main__":
    print_last_digit(1007)
    print_last_digit(0)
    print_last_digit(-293)
    print_last_digit(-20)
    print_last_digit(20)
