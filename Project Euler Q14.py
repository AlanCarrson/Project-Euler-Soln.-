# Project Euler Question 14
# A Collatz Sequence is said to have an iterative sequence where n -> n // 2 (if n is even)
# or n -> 3n+1 (if n is odd). Find the number smaller than 1,000,000 that has the longest Collatz Sequence

import sys


def Collatz_Seq(n):

    if n == 1:
        return 1
    if n % 2 == 0:
        x = n // 2
    else:
        x = (n*3)+1
    return Collatz_Seq(x)+1


def function():
    sys.setrecursionlimit(3000) # To reduce computation time, we set a limit to the times of recursion
    list1 = []
    count = 1
    for i in range(1,1000001):
        list1.append(Collatz_Seq(i))
    result = max(list1)
    for j in list1:
        if j != result:
            count += 1
        else:
            return count


print(function())  # A considerable wait-time ahead