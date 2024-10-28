'''
Author:Abhishek
Date:28-10-2024
Description:program that simulates a simple bank ATM system
'''
balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice= int(input("Enter your choice:"))
    if choice == 1:
        print(f"The current balanace ${balance_amount}")
    elif choice == 2:
        deposit_amount = float(input("Enter the amount:"))
        balance_amount = balance_amount + deposit_amount
        print(f"The deposited amount ${deposit_amount}and"f"the current balance ${balance_amount}")
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw:"))
        balance_amount = balance_amount - withdraw_amount
        print(f"The withdrawn amount ${withdraw_amount}and"f" the current balance ${balance_amount}")
        if (withdraw_amount > balance_amount):
            print(f"insufficient balance")
        else:
            print(f"The withdrawn amount ${withdraw_amount}and"f" the current balance ${balance_amount}")
    elif choice == 4:
        break
