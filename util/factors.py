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

    return [x for x in range(2, (number + 2) / 2) if number % x == 0]


def factors2(number):
    s = int(number ** 0.5)

    number_factors = set()
    number_factors.update([x for x in range(2, s + 1) if number % x == 0])

    for n in set(number_factors):
        number_factors.add(number / n)

    return sorted(number_factors)


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


print factors(28), factors2(28)
