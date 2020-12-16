# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from time import process_time

timestart = process_time()
num_list = []
max_num = 6 * (9 ** 5)

for i in range(2, max_num):
    value = i
    dsum = 0
    while value > 0:
        dsum += (value % 10) ** 5
        value //= 10
    if dsum == i:
        num_list.append(i)
print(num_list)
print(sum(num_list))
print(process_time() - timestart)
