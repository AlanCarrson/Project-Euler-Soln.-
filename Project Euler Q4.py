# Project Euler Question 4
# A palindrome is a number that is identical when read in both ways (left to right/ right to left)
# Find the largest palindrome which is a product of 2 3-digit numbers

def is_palindrome(number):

    list1 = list(str(number))

    list2 = list(str(number))

    list1.reverse()

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    else:
        return True


list3 =[]

for i in range(100,999):
    for j in range(100,999):
        if is_palindrome(i*j):
            list3.append(i*j)

list3.sort(reverse=True)

print(list3[0])