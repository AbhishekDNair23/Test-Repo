"""
Author:Abhishek
Date:18-10-2024
Desription:program that uses functions from the math module to perform the following operations
on a number provided by the user:
"""
import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("Square root of a number",number,":",square_root)
print("Factorial of",number,"=",math.factorial(number))
print(number,"Raised to power 2=",math.pow(number,2))