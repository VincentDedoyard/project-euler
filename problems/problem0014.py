# coding=utf-8

"""
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

__author__ = 'Vincent Dedoyard'


def next_collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


def make_collatz_chain(number):
    chain = [number]
    while chain[-1] != 1:
        chain.append(next_collatz(chain[-1]))

    return chain


biggest_starting_number = None
biggest_chain_length = 0

for i in range(1, 1000001):
    chain = make_collatz_chain(i)

    if len(chain) > biggest_chain_length:
        biggest_chain_length = len(chain)
        biggest_starting_number = i

print biggest_starting_number
