# Project Euler Question 5
# Find the smallest number divisible by 1 - 20 (inclusive)


# Note that 2520 is evenly divisible by 1-10,12,14,15,18,20. So we only need to find the smallest number divisible by
# the remaining factors, i.e. 11,13,16,17,19. As 11, 13, 17 and 19 are prime numbers, the smallest number divisible by
# these numbers is their product, i.e 11*13*17*19 = 46189. So we only need to investigate the smallest number divisible
# by 16 which is a product of 2520*46189

for i in range(2, 17):  # Largest number is 2520*46189*16
    if (2520*46189*i) % 16 == 0:
        print("The answer is :", 2520*46189*i)
        break




