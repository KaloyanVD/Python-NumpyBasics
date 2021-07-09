import numpy as np


a = np.genfromtxt('data.txt', delimiter=',')

# Checks each element if it's greater than 50 and prints in boolean
print(a > 50)

# prints only elements larger than 10
print(a[a > 10])
