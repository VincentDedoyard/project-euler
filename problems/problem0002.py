# coding=utf-8

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

__author__ = 'Vincent Dedoyard'


fibonacci_1 = 1
fibonacci_2 = 1
fibonacci_3 = 2

even_fibonacci_numbers = []


def next_fibonacci():
    """
    Modifies the 3 global fibonacci numbers directly one step forward
    """

    global fibonacci_1, fibonacci_2, fibonacci_3

    next_fibonacci_number = fibonacci_2 + fibonacci_3

    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_3
    fibonacci_3 = next_fibonacci_number


while fibonacci_3 <= 4000000:
    if fibonacci_3 % 2 == 0:
        even_fibonacci_numbers.append(fibonacci_3)
    next_fibonacci()

print sum(even_fibonacci_numbers)