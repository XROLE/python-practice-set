# 🔹 13. Roman Numerals to Integers
# Convert a Roman numeral string to an integer.
# python
# CopyEdit
# roman_to_int("XIV")  # Output: 14


# Solution ChatGPT

def roman_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total


# Example usage
print(roman_to_int("XIV"))  # Output: 14
