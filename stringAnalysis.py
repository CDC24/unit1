#Caleb Callaway
#1/19/18
#stringAnalysis.py- report words and characters of a sentence


sentence = input("Type a sentence. ")
character = input("what character do you want to search for? ")
print ("The letter",character,"appears",sentence.count(character),"times in your sentence.")

word = input("what word do you want to search for? ")
print ("Your sentence has",sentence.count(word),"of the word",word)