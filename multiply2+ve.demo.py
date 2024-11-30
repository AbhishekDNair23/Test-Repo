def multiplication(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+multiplication(num1,num2-1)
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number"))
if num1>0 and num2>0:
    print(f"The product of two given number is:{multiplication(num1,num2)}")
else:
    print("Enter positive number")