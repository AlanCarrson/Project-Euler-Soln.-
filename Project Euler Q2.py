# Project Euler Question 2
# Find the sum of all even terms of the Fibonacci Sequence whose value is smaller than 4 million

list1 = [0, 1, 1]

while list1[(len(list1)-1)] <= 4000000:
    list1.append(list1[len(list1)-1]+list1[len(list1)-2])


if list1[(len(list1)-1)] >= 4000000:
    list1.pop()

list2 = []

for i in list1:
    if i % 2 ==0:
        list2.append(i)

print(sum(list2))
