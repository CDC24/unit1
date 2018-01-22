#Caleb Callaway
#1/22/18
#additionGameDemo.py- how to use random numbers

from random import randint
#randint is random integer

num1 = randint(-10,10)
#parentheses give upper and lower limit
num2 = randint(-10,10)
ans = int(input(str(num1)+"+"+str(num2)+"= "))
#connect strings with pluses instead of commas to put together

print (ans == num1 + num2)
# == checks truth
