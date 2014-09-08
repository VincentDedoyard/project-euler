# coding=utf-8


"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from util import primes

__author__ = 'Vincent Dedoyard'

primes_obj = primes.Primes()

primes_under_two_million_sum = 2

for potential_prime in range(3, 2000000, 2):
    if primes_obj.is_prime(potential_prime):
        primes_under_two_million_sum += potential_prime

print primes_under_two_million_sum
