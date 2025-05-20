# ✅ 2. Simple Calculator
# Ask the user to enter two numbers and an operator (+, -, *, /) and print the result.
# python
# CopyEdit
# Input: 5, 3, *
# Output: 5 * 3 = 15


# ======================================>
# solution
num1 = int(input("Enter first number \n"))
operand = input("Enter an operand e.g (+, -, *, /)  \n")
num2 = int(input("Enter second number \n"))


if operand == '=':
    result = num1 + num2
elif operand == '*':
    result = num1 * num2
elif operand == '-':
    result = num1 - num2
elif operand == '/':
    if num2 != 0:
        result = num1 / num1
    else :
        result = "Error: can not be divided by zero"
else:
    result = "Invalid operator"



print(f"{num1} {operand} {num2} = {result}")