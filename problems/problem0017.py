# coding=utf-8
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

names = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def split_number(number):
    hundreds = number / 100
    sub_hundred = number % 100

    tens = (sub_hundred / 10) * 10
    units = sub_hundred % 10

    return hundreds, tens, units


total = 0

for i in range(1, 1000):
    hundreds, tens, units = split_number(i)
    written_out = []

    if hundreds:
        written_out.append(names[hundreds])
        written_out.append('hundred')
        if tens or units:
            written_out.append('and')

    if tens == 10:
        written_out.append(names[i % 100])
    else:
        if tens:
            written_out.append(names[tens])
        if units:
            written_out.append(names[units])

    total += sum(len(x) for x in written_out)

total += len('one') + len('thousand')

print total
