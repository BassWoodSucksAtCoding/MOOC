# Write your solution here
def histogram(text_local):
    words= {}
    for letter in text_local:
        if letter not in words:
            words[letter] = 0
        words[letter] += 1
    
    for key, value in words.items():
        print(f"{key} " + "*"*value)


if __name__ == "__main__":
    histogram("abba")
