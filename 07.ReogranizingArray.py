import numpy as np

before = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(before)

# changes the array into 4 rows 2 columns
after = before.reshape((4, 2))
print(after)

# Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([4, 5, 6, 7])

print(np.vstack([v1, v2]))
