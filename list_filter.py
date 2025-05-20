# ✅ 7. List Filter
# Given a list of numbers, print only the even ones.
# python
# CopyEdit
# Input: [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]

# ==========================================>
# solution
nums = [1,2, 3, 4, 5, 6]
evenNums = []

for num in nums:
    if num % 2 == 0 :
        evenNums.append(num)

print(evenNums)
