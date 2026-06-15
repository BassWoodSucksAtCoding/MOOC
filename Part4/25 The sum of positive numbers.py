# Write your solution here
def sum_of_positives(my_list):
    total = 0
    for i in my_list:
        if i > 0:
            total += i

    return total
