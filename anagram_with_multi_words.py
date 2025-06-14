# 🔹 11. Anagram Checker with Multiple Words
# Write a function are_anagrams(list1, list2) that takes two lists 
# of strings and returns True if every word in list1 is an anagram 
# of the corresponding word in list2.
# python
# CopyEdit
# are_anagrams(["listen", "rail", "god"], ["silent", "liar", "dog"])  # True

# Bare Code ==============================
# def are_anagrams(list1, list2) :
#     if len(list1) != len(list2) :
#         return False
#     else :
#         for i in range(len(list1)) :
#             for l in range(len(list1[i])) :
#                 hasLetter = list1[i][l] in list2[i]
#                 if hasLetter == False :
#                     print("it's not anagram")
#                     return
#         print("Anagram correct ")
             
             
             
# are_anagrams(["listen", "rail", "god"], ["silent", "liar", "dog"])   


def are_anagrams(list1, list2):
    if len(list1) != len(list2):
        return False

    for word1, word2 in zip(list1, list2):
        if sorted(word1) != sorted(word2):
            return False

    return True

# Test example
print(are_anagrams(["listen", "rail", "god"], ["silent", "liar", "dog"]))  # True
