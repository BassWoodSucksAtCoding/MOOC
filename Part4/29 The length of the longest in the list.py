# Write your solution here

def length_of_longest(my_list):
    longest = len(my_list[0])
    for i in range(len(my_list)):
        if len(my_list[i]) > longest:
            longest = len(my_list[i])
    
    return longest
