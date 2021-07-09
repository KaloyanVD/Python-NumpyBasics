import numpy as np

a = np.array([1, 2, 3, 4, 5])

# We can add, subtract, multiply and divide the elements of the array
# a += 2
# a -= 2
# a *= 2
# a /= 2


# Take the sin/cos
# np.sin(a)
# np.cos(a)
print(a)

# Multiply two matrices
b = np.ones((2, 3))
c = np.full((3, 2), 2)

result = np.matmul(b, c)
print(result)

# Find the determinant
c = np.identity(3)
np.linalg.det(c)
