# Project Euler Question 6
# Find the difference between the sum of the squares of the first one hundred integers and the square of the sum.

result1 = 0

for i in range(101):
    result1 = result1 + (i**2)


result2 = 0

for j in range(101):
    result2 = result2 + j


print(abs(result1 - result2**2))
