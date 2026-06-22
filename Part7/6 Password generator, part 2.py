# Write your solution here
from random import randint,sample

def generate_strong_password(length,numbers_bool,special_bool):
    password = [""] * length
    valid_chars = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "!?=+-()#"

    if numbers_bool:
        valid_chars += numbers
        password[randint(0, length-1)] = numbers[randint(0, len(numbers)-1)]
        password[2] = "0"

    if special_bool:
        valid_chars += special
        num = randint(0, length-1)
        if password[num] == "":
            password[num] = special[randint(0, len(special)-1)]
    
    for i in range(length):

        if password[i] == "":
            password[i] = valid_chars[randint(0, len(valid_chars)-1)]

    pass_str = ""

    for i in password:
        pass_str += i
    
    return pass_str



