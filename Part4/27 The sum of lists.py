# Write your solution here

def list_sum(list_1,list_2):
    new_list = []
    for i in range(len(list_1)):
        new_list.append(list_1[i]+list_2[i])
    
    return new_list
