# 🔹 14. Matrix Transposition
# Given a 2D list, return its transpose.
# python
# CopyEdit
# transpose([[1, 2], [3, 4], [5, 6]])  # Output: [[1, 3, 5], [2, 4, 6]]

# Solution


def transpose(s):
    result = []
    
    if not s:
        return result
    
    for i in range(len(s)):
        subArray = []
        for j in range(len(s[i])):
            subArray.append(s[i][j])
        result.append(subArray)
        subArray = []
             
    return result



res = transpose([[1, 2], [3, 4], [5, 6]])
print(f"This is the fact ========> {res}")