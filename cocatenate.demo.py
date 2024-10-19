"""
Author:Abhishek
Date:19-10-2024
description:Write a Python program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between and store the result in a new variable.

    Print the concatenated string.

    From the concatenated string:
"""
first_name = input("enter your first name ")
last_name = input("enter your last name ")
name = first_name+" "+last_name
print(name)
first_name_length = len(first_name)
sub_string =name[first_name_length]
print(sub_string)
