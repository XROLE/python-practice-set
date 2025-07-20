# ✅ 8. Word Counter
# Take a sentence from the user and count how many times each word appears.
# python
# CopyEdit
# Input: "hello world hello"
# Output: {'hello': 2, 'world': 1}

# ===================================================> 
# solution

favoriteMantra = input("Enter your favourite mantra : ")
splittedMantra = favoriteMantra.split()
wordDictionary = {}

for word in splittedMantra:
    if word in wordDictionary:
        wordDictionary[word] += 1
    else:
        wordDictionary[word] = 1


print(wordDictionary)