# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

from math import factorial

sp_ls = []
upper_bound = 7 * factorial(9)
for i in range(3, upper_bound):
    m = str(i)
    ls = [int(d) for d in m]
    if i == sum(list(map(factorial, ls))):
        sp_ls.append(i)
print(sum(sp_ls))
