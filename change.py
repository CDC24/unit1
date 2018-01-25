#Caleb Callaway
#1/24/17
#change.py- converts an input to numbers of smaller parts


allMoney = float(input("Enter an amount of money.  $"))

cents= (allMoney*100)

quarters= int(cents//25)
print ("quarters:",quarters)

dimes = int((cents-(quarters*25))//10)
print ("dimes:",dimes)

nickels = int((cents-(quarters*25)-(dimes*10))//5)
print ("nickels:",nickels)

pennies = int((cents-(quarters*25)-(dimes*10)-(nickels*5))/1)
print ("pennies:",pennies)