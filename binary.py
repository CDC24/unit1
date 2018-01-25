#Caleb Callaway
#1/25/18
#binary.py- converts 8 digit binary numbers to base 10

num = (input("Enter an 8-digit binary number with spaces between each digit: "))

a, b, c, d, e, f, g, h = num.split()

print (h*10**0 + g*10**1 + f*10**2 + e*10**3 + d*10**4 + c*10**5 + b*10**6 + a*10**7)