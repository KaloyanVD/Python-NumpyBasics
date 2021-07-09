import numpy as np

# Build the following array
#   1   1   1   1   1
#   1   0   0   0   1
#   1   0   9   0   1
#   1   0   0   0   1
#   1   1   1   1   1


output = np.ones((5, 5))

z = np.zeros((3, 3))
z[1, 1] = 9
output[1:4, 1:4] = z


print(output)
