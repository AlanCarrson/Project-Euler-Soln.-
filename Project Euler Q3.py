# Project Euler Question 3
# Find the largest prime factor of 600851475143

import math

number = 600851475143

list1 = []

for i in range(2, int(math.sqrt(number))):  #
    if number % i == 0:
        list1.append(i)


def prime_test(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    else:
        return True


list2 = []

for k in list1:
    if prime_test(k):
        list2.append(k)


print(list2[len(list2)-1])
