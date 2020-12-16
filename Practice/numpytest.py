import numpy as np
from numpy import pi
import sys

a = np.arange(20).reshape(4, 5)
print(a)
# dimensions of the array
print("Shape:", a.shape)
# number of axes
print("Axes/Dimensions:", a.ndim)
# number of elements
print("Size:", a.size)
# data type of the element - int 32
print("Data type:", a.dtype.name)
# byte size of each element - 4 byte in int 32
print("Byte size:", a.itemsize)
# Class - ndarray
print(type(a))
# b = np.array([6, 7, 8, 9]).reshape(2, 2)
# c = np.arange(25, 125, 5).reshape(4, 5)

# b = np.array([[1, 2], [3, 4]], dtype=complex)
# print(b)
# print(b.ndim)

# b = np.zeros((3, 4), dtype=np.int16)
# c = np.ones((2, 3, 4), dtype=np.int16)
# d = np.empty((2, 4), dtype=np.int16)

# d = np.linspace(0, 1 * pi, 10)

# print(np.arange(10000).reshape(100, 100))
