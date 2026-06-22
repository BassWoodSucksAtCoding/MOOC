# Write your solution here
from random import randint

def generate_password(length):
    password = ""
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in range(length): 
        password += alphabets[randint(0, 25)]
    
    return password


# for i in range(10):
#     print(generate_password(8))
