#Caleb Callaway
#1/25/18
#binary.py- converts 8 digit binary numbers to base 10

num = (input("Enter an 8-digit binary number with spaces between each digit: "))

a, b, c, d, e, f, g, h = num.split()

print (a*2**7 + b*2**6 + c*2**5 + d*2**4 + e*2**3 + f*2**2 + g*2**1 + h*2**0)