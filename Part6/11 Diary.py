# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        with open("diary.txt", "a") as my_file:
            entry = input("Diary entry: ")
            my_file.write(f"{entry}\n")
    elif function == 2:
        with open("diary.txt") as my_file:
            for line in my_file:
                print(line.strip())
    else:
        print("Bye now!")
        break
