import numpy as np

# Slicing numpy arrays 
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Return 2, 3, 4, 5
print(np1[1:5])

# Return from something till the end of the Array 
print(np1[3:])

# Return negative slices 
print(np1[-3: -1])

# steps 
print(np1[1:5])
print(np1[1: 5: 2])

# steps on the entire array 
print(np1[::2])
print(np1[::3])


# Slice a 2d array 
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# pull out a single item
print(np2[1, 2])
