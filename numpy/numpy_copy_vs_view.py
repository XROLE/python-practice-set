import numpy as np

# Copy Vs. view
np1 = np.array([1, 2, 3, 4, 5])

# Create a view 
# np2 = np1.view()

# print(f"Original np1 {np1}")
# print(f"Original np2 {np2}")

# np1[0] = 41


# print(f"Changed np1 {np1}")
# print(f"Original np2 {np2}")

np2 = np1.copy()
print(f"Original np1 {np1}")
print(f"Original np2 {np2}")

np1[0] = 41


print(f"Changed np1 {np1}")
print(f"Original np2 {np2}")