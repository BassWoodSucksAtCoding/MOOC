# Write your solution here
operation = ""
my_list = []
index = -1

while operation.lower() != "x":
    print(f"The list is now {my_list}")
    operation = str(input("a(d)d, (r)emove or e(x)it: "))

    if operation.lower() == "d":
        if my_list == []:
            my_list.append(1)
            index = 0
        else:
            my_list.append(my_list[index]+1)
            index += 1
    elif operation.lower() == "r":
        my_list.pop(index)
        index -= 1
    elif operation.lower() == "x":
        print("Bye!")
    else:
        print("Invalid")
