# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(text):
    centre = len(text) // 2
    length = len(text)

    for i in range(centre):
        if text[i] != text[length-i-1]:
            return False
    return True

is_palindrome = False

while not is_palindrome:
    text = str(input("Please type in a palindrome: "))
    is_palindrome = palindromes(text)

    if not is_palindrome:
        print("that wasn't a palindrome")
    else:
        print(f"{text} is a palindrome!")
