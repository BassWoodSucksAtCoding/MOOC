# Write your solution here
my_list = []
count = 0
while True:
    word = str(input("Word: "))
    
    if word in my_list:
        print(f"You typed in {count} different words")
        break
    else:
        my_list.append(word)
        count += 1
