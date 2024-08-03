# Project Euler Question 15
# Starting at the top left corner of a 2 X 2 grid, being able to move only downward and rightwards, there are exactly
# 6 routes that can reach the bottom right corner. Find the number of ways to reach the bottom right corner if the 2X2
# grid is replaced by a 20 X 20 grid

# A deceivingly easy question. Regardless of route taken, one always have to move 20 steps downward and 20 steps
# rightwards. If we denote 1 being a downward step and 0 being a rightward step, then the route taken can be expressed
# as a vector of 40 numbers, where 20 of them are ones. Then the question is how do we place the 20 "1"s. This is just
# a combination of choosing 20 from 40

from math import factorial

result = factorial(40)/(factorial(20)**2)

print(int(result))
