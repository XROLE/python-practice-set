# ✅ 4. Guess the Number Game
# Generate a random number between 1 and 10. Let the user guess until they get it right.
# python
# CopyEdit
# Output:
# Guess the number: 4
# Try again!
# Guess the number: 7
# Correct


# ==================================================>
# solution

import random

numToGuess = random.randint(1, 10)
print(f"Random number to guess {numToGuess}")

guessedNum = int(input("Enter guess: "))
while guessedNum != numToGuess:
    print(f"Oops you guessed wrongly for {guessedNum}")
    guessedNum = int(input("Enter guess again: "))

print(f"Correct!!! You did it, {guessedNum} is the answer")