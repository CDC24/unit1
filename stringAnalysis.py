#Caleb Callaway
#1/19/18
#stringAnalysis.py- report words and characters of a sentence


sentence = input("Type a sentence. ")
space= (" ")
period=(".")
comma=(",")
apostrophe=("'")

print ("There are",len(sentence),"characters in your sentence.")
print ("There are",int(len(sentence))- int(sentence.count(space)+sentence.count(period)+sentence.count(comma)+sentence.count(apostrophe)),"letters in your sentence.")
print ("There are", int(sentence.count(space))+1,"words in your sentence.")

character = input("What character do you want to search for? ")
print ("The letter",character,"appears",sentence.count(character),"times in your sentence.")

word = input("What word do you want to search for? ")
print ("Your sentence has",sentence.count(word),"of the word",word)