def check_right_triangle(sides):
   sides.sort()
   if sides[2]**2 ==sides[0]**2 + sides[1]**2:
     return True
   return False
sides=[]
sides.append(int(input("Enter the length of the first side:")))
sides.append(int(input("Enter the length of the second side:")))
sides.append(int(input("Enter the length of the third side:")))
if check_right_triangle(sides):
    print("The given sides are part of right triangle")
else:
    print("The given sides are not part of right triangle")