def add(num1,num2):
    if num2==0:
        return num1
    else:
        return add(num1+1,num2-1)
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1>0 and num2>0:
    print("The sum of the two numbers is:",add(num1,num2))
else:
    print("Enter positive numbers")