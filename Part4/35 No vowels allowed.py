# Write your solution here
def no_vowels(my_string_local):
    new_string = my_string_local
    new_string = new_string.replace("a","")
    new_string = new_string.replace("e","")
    new_string = new_string.replace("i","")
    new_string = new_string.replace("o","")
    new_string = new_string.replace("u","")

    return new_string
