import numpy as np

# 1Create Array

# Transfer from list
alist = [1, 2, 3]
arr = np.array(alist)
print(arr)

# np.arange()
arr1 = np.arange(2, 30)
print(arr1)

# np.zeros()
cube = np.zeros((5, 5)).astype(int) + 1
print(cube)

# reshape
arr1d = np.arange(64)
arr3d = arr1d.reshape((4, 16))
# arr3d = np.reshape(arr1s, (10, 10, 10))
print(arr3d)

