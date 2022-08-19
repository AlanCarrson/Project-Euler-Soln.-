# Project Euler Question 12
# A triangular number is a number formed by summing up natural numbers. Find the first triangular number that has over
# 500 factors

from math import sqrt

import itertools


def function():
    number = 0
    for i in itertools.count(1):
        number += i
        if factor_count(number) > 500:
            print(number)
            break


def factor_count(n):
    count = 0
    end = int(sqrt(n))
    for i in range(1,end+1):
        if n % i == 0:
            count += 2
    if end ** 2 == n:
        count = count-1
    return count

# A few seconds of wait-time ahead

function()
