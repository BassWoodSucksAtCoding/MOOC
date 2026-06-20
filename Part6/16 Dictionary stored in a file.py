# Write your solution here

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        word_fin = input("The word in Finnish: ")
        word_eng = input("The word in English: ")
        with open("dictionary.txt","a") as new_file:
            new_file.write(f"{word_fin} - {word_eng}\n")
        print("Dictionary entry added")
    elif function == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt") as new_file:
            for line in new_file:
                if line.lower().find(search_term) != -1:
                    print(line)
    else:
        print("Bye!")
        break
