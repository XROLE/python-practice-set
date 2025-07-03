# 🔹 12. Custom String Compression
# Write a function compress_string(s) that replaces repeated characters with counts.
# python
# CopyEdit
# compress_string("aaabbccccdd")  # Output: "a3b2c4d2"


# solution ChatGPT
# def compress_string(s):
#     if not s:
#         return ""

#     result = []
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             result.append(s[i - 1] + str(count))
#             count = 1  # reset

#     # Add the last character group
#     result.append(s[-1] + str(count))

#     return "".join(result)


# # Example usage
# print(compress_string("aaabbccccdd"))  # Output: a3b2c4d2


# solution
def compress_string(s) :
    previousString = ""
    currentString = ""
    result = ""
    currentCount = 0
    print(s)
    
    if(len(s) == 0) :
        return ""
    
    for i in range(len(s)):
        currentString = s[i]
        
        if(len(previousString) < 1):
            previousString = currentString
            currentCount = 1
            continue
        
        if(currentString == previousString):
            currentCount = currentCount + 1
            previousString = currentString
        else:
            result = f"{result}{previousString}{currentCount}"
            previousString = currentString
            currentCount = 1
    return f"{result}{previousString}{currentCount}"


firstTest = compress_string("aaabbccccdd")

print(f"ans {firstTest}")


