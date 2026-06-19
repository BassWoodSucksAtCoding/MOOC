# write your solution here
def list_checker(condition):
    with open("matrix.txt") as new_file:
        all_parts = []
        count = 0
        for line in new_file:
            line = line.replace("\n","")
            parts = line.split(",")
            
            if condition == "matrix":
                for item in parts:
                    all_parts.append(int(item))
            elif condition == "row":
                all_parts.append([])
                for item in parts:
                    all_parts[count].append(int(item))
            
                count += 1
    
    return all_parts
            
def matrix_sum():
    return sum(list_checker("matrix"))

def matrix_max():
    return max(list_checker("matrix"))

def row_sums():
    total = []
    for item in list_checker("row"):
        total.append(sum(item))
    
    return total

# matrix_sum() 
# matrix_max()
# row_sums()
