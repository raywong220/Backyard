# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


diagonal_list = [1]
current = 1
grid_size = 1001

# As there is a difference of multiples of 2 (each occurs 4 times)
# eg. 1 (+2) 3 (+2) 5 (+2) 7 (+2) 9   <--- 4 times of +2
#     9 (+4) 13 (+4) 17 (+4) 21 (+4) 25 <---- 4 times of +4
# Next outer squares will be +6, +8 etc
for i in range(2, grid_size, 2):
    times = 0
    while times < 4:
        current += i
        times += 1
        diagonal_list.append(current)

print(sum(diagonal_list))
