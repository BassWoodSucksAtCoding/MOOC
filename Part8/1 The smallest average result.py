# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):

    avg = []
    people = [person1,person2,person3]

    for person in people:
        total = 0
        for key, values in person.items():
            if key == "name":
                continue
            else:
                total += values
        
        avg.append(total/3)
    
    return people[avg.index(min(avg))]



# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))
