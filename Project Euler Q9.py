# Project Euler Question 9
# A pythagorean triplet are 3 numbers a,b,c that a^2+b^2=c^2 where a < b < c and there is exactly 1 such triplet that
# a + b + c = 1000. Find a*b*c.

for a in range(1, 1001):
    for b in range(a+1, 1001):
        if a**2+b**2 == (1000-a-b)**2:
            print(a*b*(1000-a-b))

