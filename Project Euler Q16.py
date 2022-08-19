# Project Euler Question 16
# Find the sum of digits of 2^1000

result = 2 ** 1000

list1 = list(str(result))

answer = 0

for i in list1:
    answer = answer + int(i)

print(answer)