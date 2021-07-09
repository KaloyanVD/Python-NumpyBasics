import numpy as np

# initialize one dimensional array
a = np.array([1, 2, 3])
print(a)

# initialize two dimensional array
b = np.array([[1, 2, 3], [2, 3, 4], [5, 6, 7]])
print(b)

# get dimensions
print(a.ndim)
print(b.ndim)

# get shape
print(a.shape)
print(b.shape)

# Get Type
print(a.dtype)
print(b.dtype)

# Get Size in bytes single element
print(a.itemsize)
print(b.itemsize)

# Get Total Size in bytes
print(a.nbytes)
print(b.nbytes)
