# Write your solution here

def filter_incorrect():
    with open("correct_numbers.csv","w") as correct_files:
        pass
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            continue_local = True
            line = line.strip()
            parts = line.split(";")
            parts_dict = {}

            try:
                week_no = int(parts[0][5:])
            except ValueError:
                continue_local = False
                continue

            

            parts_dict[parts[0]] = parts[1].split(",")
            

            if len(parts_dict[parts[0]]) != 7:
                continue_local = False
                continue 
            
            all_numbers = []

            for items in parts_dict[parts[0]]:
                try:
                    items = int(items)
                except ValueError:
                    continue_local = False
                    break
                
                if items < 1 or items > 39:
                    continue_local = False
                    break

                if items not in all_numbers:
                    all_numbers.append(items)
                else:
                    continue_local = False
                    break
            
            if continue_local:
                with open("correct_numbers.csv","a") as correct_files:
                    correct_files.write(f"{line}\n")




