#Author: Niko Wesselson
#Date Modified: Feb 28, 2025
#Description: Variables, Math Operations, and Input

# Importing math
import math

# Variable types
string = "Blue"
boolean = False
integer = 3

# Printing example variables
print("An example string is:", string)
print("An example boolean:", boolean)
print("An example integer:", integer)

# Performing math equations
addition = 4 + 4
subtraction = 5 - 3
product = 5*2*9
quotient_integer = 24/6
quotient_float = 100/3
square = math.sqrt(36)
exponent = 6**9
rem_1 = 24%6
rem_2 = 24%5
rem_3 = 24%7

# Printing results of math equations
print("ADDITION OF 4+4 is:", addition) 
print("SUBTRACTION OF 5-3 is:", subtraction)
print("PRODUCT OF 5*2*9 is:", product)
print("QUOTIENT INTEGER OF 24/6 is:", quotient_integer)
print("QUOTIENT FLOAT OF 100/3 is:", quotient_float)
print("SQUARE ROOT OF 36 is:", square)
print("EXPONENT 6**9 is:", exponent)
print("MODULUS is:", rem_1)
print("MODULUS is:", rem_2)
print("MODULUS is:", rem_3)

# Getting inputs for discriminant calculation
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculating discriminant
delta = b**2 - 4*a*c 

# Printing discriminant
print("\nDiscriminant:", delta)

# Calculating volume of cube
A = float(input("Enter side length of cube:"))
side = A **3
print("\nVolume of cube:", side)

# Calculating volume of sphere
r = float(input("Enter radius of sphere:"))
radius = 4/3*math.pi*r**3
print("\nVolume of sphere:", radius)

# Calculating volume of cone
cr = float(input("Enter radius of cone:"))
ch = float(input("Enter height of cone:"))
cv = 1/3*math.pi*cr**2*ch
print("\nVolume of cone:", cv)

# Calculating volume of cylinder
cyr = float(input("Enter radius of cylinder:"))
cyh = float(input("Enter height of cylinder:"))
cyv = math.pi*cyr**2*cyh
print("\nVolume of cylinder:", cyv)
