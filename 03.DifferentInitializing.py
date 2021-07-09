import numpy as np

# ALL 0's array
a = np.zeros((2, 3))
print(a)

# ALL 1's array
b = np.ones((2, 3))
print(b)

# Any other number
c = np.full((2, 2), 10)
print(c)

# Using full_like
d = np.full_like(a, 4)
print(d)

# Random decimal numbers
e = np.random.rand(1, 3)
print(e)

# Create array with numbers between 0 and 7 with 4 rows and cols
f = np.random.randint(7, size=(4, 4))
print(f)
