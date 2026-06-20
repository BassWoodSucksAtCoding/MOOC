# Write your solution here
import string

def separate_characters(my_string: str):
    parts = ["","",""]
    for letter in my_string:
        if letter in string.ascii_letters:
            parts[0] += letter
        elif letter in string.punctuation:
            parts[1] += letter
        else:
            parts[2] += letter
    

    return (parts[0],parts[1],parts[2])


