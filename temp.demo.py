"""
Author:Abhishek
Date:28-10-2024
Description:a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
"""
while True:
    print("\n1.\tCelsius to Fahrenheit")
    print("2.\tFahrenheit to Celsius")
    print("3.\tExit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        celsius = float(input("Enter the Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in fahrenheit:{fahrenheit}")
    elif choice == 2:
        fahrenheit = float(input("Enter the Fahrenheit:"))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Temperature in celsius:{celsius}")
    elif choice == 3:
        break
