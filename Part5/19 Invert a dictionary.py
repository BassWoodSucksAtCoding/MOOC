# Write your solution here
def invert(dictionary: dict):
    temporary = {}
    for key,value in dictionary.items():
        temporary[key] = value

    for key,value in temporary.items():
        dictionary[value] = key
        del dictionary[key]


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
