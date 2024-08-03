from math import sqrt


def prime_check(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True


list1 =[2]

for j in range(3, 2000001, 2):
    if prime_check(j):
        list1.append(j)

print(sum(list1))
