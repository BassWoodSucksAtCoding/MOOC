# Write your solution here
def no_shouting(my_list_local):
    new_list_local = []
    for row in my_list_local:
        if row.isupper():
            continue
        else:
            new_list_local.append(row)

    return new_list_local
