#Caleb Callaway
#1/18/18
#age.py -count letters and numbers

name = input("What is your name (first and last only)? ")
age = int(input("how old are you? "))
name1, name2= name.split( )
print("You have",len(name1),"letters in your first name.")
print("You have",len(name2),"letters in your first name.")
print("Next year you will be",(age)+1,"years old.")