# coding=utf-8

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from util import primes

__author__ = 'Vincent Dedoyard'

primes_object = primes.Primes()

number = 600851475143
prime_factors = set()
current_prime = 2

while number != 1:
    if number % current_prime == 0:
        prime_factors.add(current_prime)
        number /= current_prime
    else:
        current_prime = primes_object.prime_after(current_prime)

print max(prime_factors)
