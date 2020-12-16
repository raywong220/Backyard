# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

from time import process_time

sum = 0
# Since even number always ends with 0 in binary, not Palindromic
for i in range(1, 1000001, 2):
    b = bin(i)[2:]
    if str(i) == str(i)[::-1] and b == b[::-1]:
        sum += i
print(sum)
print(process_time())