#Increasing Triangle
num = int(input("Enter the no of rows: "))
for i in range(1,num+1):
    print("*\t"*i)
#Decreasing triangle
num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    print("*\t"*i)
#hill pattern
num = int(input("Enter the number of rows:"))
for i in range(1,num+1):
    for k in range(num-i):
        print(" ",end=" ")
    for k in range(i*2-1):
        print("*",end=" ")
    print()
#Reverse hill pattern
num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for k in range(num-i):
        print(" ",end=" ")
    for k in range(i*2-1):
        print("*",end=" ")
    print()