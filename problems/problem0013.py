# coding=utf-8

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    74324986199524741059474233309513058123726617309629
    91942213363574161572522430563301811072406154908250
    23067588207539346171171980310421047513778063246676
    (...)

PS : full data included in problem0013.txt
"""

__author__ = 'Vincent Dedoyard'

data = []
with open('problem0013.txt', 'r') as f:
    for line in f:
        data.append(line[:15])  # the rest isn't useful here

print str(sum(map(int, data)))[:10]
