def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1>0 and num2>0:
    print(f"The greatest common divisor of {num1} and {num2} is:", gcd(num1,num2))
else:
    print("Enter positive  numbers")