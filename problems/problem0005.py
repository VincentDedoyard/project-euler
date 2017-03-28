# coding=utf-8
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (no remainder) by all of the numbers from 1 to 20?
"""

from collections import Counter

from util import factors

final = {x: 0 for x in range(2, 21)}
for i in range(2, 21):
    prime_factors = Counter(factors.prime_factors(i))

    for number, count in prime_factors.iteritems():
        if count > final[number]:
            final[number] = count

result = 1

for number, count in final.iteritems():
    result *= number ** count

print result
