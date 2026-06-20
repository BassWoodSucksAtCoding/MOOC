# Write your solution here
def new_person(name: str, age: int):
    incorrect = False
    if name.find(" ") == -1 or len(name) > 40 or not (0 < age <= 150):
        raise ValueError("An error has occurred")
    else:
        return (name,age)
