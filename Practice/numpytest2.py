import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
c = a - b
print(c)
b **= 2
print(b)

# a = 10 * np.sin(a)
print(a)
print(a % 20 == 0)

# A = np.array([[2, 1], [0, 1]])
# B = np.array([[2, 0], [3, 4]])
# print(A)
# print(B)
# print("---------------")
# print(A * B)
# print("---------------")
# print(A @ B)

b = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]
print(b.sum(axis=0))  # sum of each column
print(b.sum(axis=1))  #             row
print(b.min(axis=0))  # min of each column
print(b.min(axis=1))  #             row
print(b.cumsum(axis=0))  # cumulative sum along each column
print(b.cumsum(axis=1))  #                           row

print(np.sqrt(b))
