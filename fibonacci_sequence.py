# ✅ 10. Fibonacci Series
# Write a function to generate the first n numbers of the Fibonacci series.
# python
# CopyEdit
# # Input: 5
# # Output: [0, 1, 1, 2, 3]


fibonacciSequence = []

rangeToCompute = int(input("What range do you have in mind : \n"))

if rangeToCompute < 1 :
    print(f"{rangeToCompute} is not a valid range")
else :
    for num in range(rangeToCompute) :
        if num == 0 : 
            fibonacciSequence.append(0)
        elif num == 1 :
            fibonacciSequence.append(1)
        else :
            nextVal = fibonacciSequence[num - 2] + fibonacciSequence [num - 1]
            fibonacciSequence.append(nextVal)
            
print(f"The sequence ===> {fibonacciSequence}")