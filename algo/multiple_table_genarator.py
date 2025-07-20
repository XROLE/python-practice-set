# ✅ 6. Multiplication Table Generator
# Ask the user for a number and print its multiplication table up to 12.
# python
# CopyEdit
# Input: 3
# Output: 
# 3 x 1 = 3
# 3 x 2 = 6
# ...

# =========================================> 
# solution 
choiceNumber = int(input("Enter your prefered number: "))

count = 1
while count <= 12:
    print(f"{choiceNumber} x {count} = ", choiceNumber * count)
    count += 1