# coding=utf-8


"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

__author__ = 'Vincent Dedoyard'

abc_product = 0

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - (a + b)
        if a ** 2 + b ** 2 == c ** 2:
            abc_product = max(abc_product, a * b * c)

print abc_product
