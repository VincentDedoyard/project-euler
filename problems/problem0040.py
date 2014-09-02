# coding=utf-8

"""
An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

__author__ = 'Vincent Dedoyard'

decimal_string = '0'  # omit the . so that string indeces work as intended
current_integer = 1

while len(decimal_string) < 1000005:
    decimal_string += str(current_integer)
    current_integer += 1

print reduce(lambda x, y : x * y,
             map(int, [decimal_string[1], decimal_string[10], decimal_string[100], decimal_string[1000], decimal_string[10000], decimal_string[100000], decimal_string[1000000]]),
             1)
