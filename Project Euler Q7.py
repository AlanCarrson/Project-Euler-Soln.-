# Project Euler Question 7
# Find the 10001 st prime number

from math import sqrt


def prime_check(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True


list1 = []

for i in range(2, 110001):
    if prime_check(i):
        list1.append(i)


print(list1[10000])