#Caleb Callaway
#1/25/18
#isItATriangle.py - determines if 3 numbers could be the sides of a triangle

A = float(input("Enter side A: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))

small = min(A,B,C)
large = max(A,B,C)
med = (A + B + C - small - large)

print(small + med > large)