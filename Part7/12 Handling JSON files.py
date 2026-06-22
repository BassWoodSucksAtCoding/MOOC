# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as new_file:
        persons = json.loads(new_file.read())
    
    for people in persons:
        hobby_str = ""
        for hobby in people["hobbies"]:
            hobby_str += f"{hobby}, "
    
        print(f"{people["name"]} {people["age"]} years ({hobby_str[:-2]})")


