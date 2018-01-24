#Caleb Callaway
#1/24/17
#change.py- converts an input to numbers of smaller parts


allMoney = float(input("Enter an amount of money.  $"))

quarters= (allMoney//0.25)
print (quarters,"quarters")

dimes = ((allMoney-(quarters*0.25))//0.10)
print (dimes,"dimes")

nickels = ((allMoney-(quarters*0.25)-(dimes*0.10))//0.05)
print (nickels,"nickels")

pennies = ((allMoney-(quarters*0.25)-(dimes*0.10)-(nickels*0.05))//0.01)
print (pennies, "pennies")