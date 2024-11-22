list_1 = []
n = int(input("Enter the number of elements in list_1: "))
for i in range(n):
    num = int(input("Enter the elements: "))
    list_1.append(num)
list_2 = []
m = int(input("Enter the number of elements in list_2: "))
for i in range(m):
    num = int(input("Enter the elements: "))
    list_2.append(num)
list = list_1 + list_2
even_list = []
odd_list = []
for i in list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
list_3 = []
list_3 = even_list + odd_list
print(list_1)
print(list_2)
print(list_3)

