#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
ld = (number % 10) if (number >= 0) else (number % -10) # Modulo 10 gets the last digit in base 10

if (ld > 5):
    print(f'Last digit of {number} is {ld} and is greater than 5')
elif (ld < 6 and ld != 0):
    print(f'Last digit of {number} is {ld} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is 0 and is 0')