# write your solution here
text = input("Write text: ")
split_text = text.split(" ")
recovered_text = ""
words = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        words.append(line.strip())
for word in split_text:
    if word.lower() not in words:
        recovered_text += f"*{word}* "
    else:
        recovered_text += f"{word } "

print(recovered_text)
