def is_valid_mobile_number(number):
    '''
    Function to check if a mobile number is valid.
    :param number:
    :return: True if number is valid, else False
    '''
    if len(number)==10 and number[0] in "987":
        return True
    return False
mobile_number = input("Enter the mobile_number: ")
if is_valid_mobile_number(mobile_number):
    print(f"The mobile number is {mobile_number} valid")
else:
    print(f"The mobile number is {mobile_number} is invalid")