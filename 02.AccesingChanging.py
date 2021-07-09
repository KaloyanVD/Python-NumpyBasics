import numpy as np

# Initialize two dimensional array
a = np.array([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]])
print(a)

# Get a specific element row:col
print(a[1, 4])

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 0])

# get every other element from the first row from index 1 to index 5
print(a[0, 1:6:2])

# change elements using indexes
a[1, 5] = 20
print(a)

# change the 3rd element of each row to 1 and 2
a[:, 2] = [1, 2]
print(a)
