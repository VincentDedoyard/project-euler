# coding=utf-8

"""
Factors
"""

from util import primes


primes_obj = primes.Primes()


def factors(number):
    """

    :param number:
    :return:
    """


def prime_factors(number):
    """

    :param number:
    :return:
    """

    prime_factors_list = []
    current_prime = primes_obj.first_prime()

    while number != 1:
        if number % current_prime == 0:
            prime_factors_list.append(current_prime)
            number /= current_prime
        else:
            current_prime = primes_obj.prime_after(current_prime)

    return prime_factors_list
