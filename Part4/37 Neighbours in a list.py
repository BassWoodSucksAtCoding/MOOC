# Write your solution here
def longest_series_of_neighbours(my_list_local):
    longest_temporary_local = 0
    true_longest_local = 0
    for i in range(len(my_list_local)-1):
        
        if abs(my_list_local[i] - my_list_local[i+1]) == 1:
            longest_temporary_local += 1
        else:
            if longest_temporary_local > true_longest_local:
                true_longest_local = longest_temporary_local + 1
            longest_temporary_local = 0
        
    if longest_temporary_local > true_longest_local:
        true_longest_local = longest_temporary_local + 1
        
    
    return true_longest_local


