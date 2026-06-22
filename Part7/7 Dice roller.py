# Write your solution here

from random import randint

def roll(dice_name):
    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }   

    return dice[dice_name.upper()][randint(0,5)]

def play(die1: str, die2: str, times: int):
    results = [0,0,0]
    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)

        if result1 > result2:
            results[0] += 1
        elif result2 > result1:
            results[1] += 1
        else:
            results[2] += 1
    
    return (results[0], results[1], results[2])
    


# for i in range(20):
#     print(roll("A"), " ", end="")
# print()
# for i in range(20):
#     print(roll("B"), " ", end="")
# print()
# for i in range(20):
#     print(roll("C"), " ", end="")

# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)
