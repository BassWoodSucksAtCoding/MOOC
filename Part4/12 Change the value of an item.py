# Write your solution here
my_list = [1, 2, 3, 4, 5]
index = 0

while index != -1:
    index = int(input("Index: "))
    if index != -1:
        value = int(input("New value: "))
        my_list[index] = value
        print(my_list)
