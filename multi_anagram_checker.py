# 🔹 11. Anagram Checker with Multiple Words
# Write a function are_anagrams(list1, list2) that takes two lists of strings and returns True if every word in list1 is an anagram of the corresponding word in list2.
# python
# CopyEdit
# are_anagrams(["listen", "rail", "god"], ["silent", "liar", "dog"])  # True

# Solution 1
# def are_anagrams(list1, list2):
#     # If the lists are not the same length, they can't match pairwise
#     if len(list1) != len(list2):
#         return False
    
#     # Compare each pair
#     for word1, word2 in zip(list1, list2):
#         if sorted(word1) != sorted(word2):
#             return False
    
#     return True

# # Example usage
# print(are_anagrams(["listen", "rail", "god"], ["silent", "liar", "dog"]))  # True
# print(are_anagrams(["hello", "world"], ["world", "hello"]))  # False


# Solution 1

def are_anagrams(list1, list2):
   isAnagram = True
   
   
   for i in range(len(list1)):
    for j in range(len(list1[i])):
        if len(list1[i]) != len(list2[i]) :
            isAnagram = False
            break
        
        if list1[i][j] in list2[i]:
            continue
        else:
            isAnagram = False
           
   return isAnagram

ans = are_anagrams(["listen", "rail", "god"], ["silent", "liar", "dog"])

print(f"The ans is finally here ==========> {ans}")