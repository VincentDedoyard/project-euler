# coding=utf-8

"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

__author__ = 'Vincent Dedoyard'

print sum(map(int, str(2 ** 1000)))
