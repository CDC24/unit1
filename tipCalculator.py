#Caleb Callaway
#1/18/18
#tipCalculator.py- calculates and adds a tip

price = int(input("What is the price of your meal in dollars? $"))
percentTip = int(input("what is the percentage you plan to tip? "))
tip = (percentTip/100)
total = ((tip*price)+price)
print("you should tip $",tip*price,".")
print("your total is $",(total),".")