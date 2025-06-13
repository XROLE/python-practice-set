
magicSentence = input("Make a sentence: \n")
wordsFromSentence = magicSentence.split(" ")

sentenceWordCount = {}

for word in wordsFromSentence :
    if word in sentenceWordCount :
        sentenceWordCount[word] += 1
    else : 
        sentenceWordCount[word] = 1

print(sentenceWordCount) 