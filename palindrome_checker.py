# ✅ 5. Palindrome Checker
# Check if a word is a palindrome (reads the same forwards and backwards).
# python
# CopyEdit
# Input: madam
# Output: True

# ======================================================> 
# solution

whisperedWord = input("Whisper to me: ")
if whisperedWord == whisperedWord[::-1]:
    print("True")
else:
    print("False")
