# Project Euler Question 1
# Find the sum of all multiples of 3 and 5 below 1000


list1 = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        list1.append(i)

print(sum(list1))