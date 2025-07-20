import numpy as np 
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# for x in np1:
#     print(x)

# 2 - D array 
# np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# for x in np2:
#     print("Stating ====================> ")
#     for y in x:
#         print(y)
        
        
# 3 - D array 
np3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
# for x in np3:
#     print("Firs Dimension print out ======>")
#     for y in x:
#         print("second dimension print out ==============> ")
#         for z in y:
#             print(z)

# Use np.nditer()
for x in np.nditer(np3):
    print(x)