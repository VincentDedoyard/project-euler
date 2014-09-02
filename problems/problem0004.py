# coding=utf-8

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

__author__ = 'Vincent Dedoyard'


def is_palindrome(number):
    forward = str(number)
    backward = str(number)[::-1]

    return forward == backward


print max(filter(is_palindrome, [a * b for a in range(100, 1000) for b in range(100, 1000)]))
