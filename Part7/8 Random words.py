# Write your solution here
from random import sample

def words(n: int, beginning: str):

    with open("words.txt") as new_file:
        word_list = []
        for line in new_file:
            line = line.strip()
            if line.startswith(beginning):
                word_list.append(line)
        
        if len(word_list) < n:
            raise ValueError("Not enough words present")
        else:
            return sample(word_list,n)
        


# word_list = words(300000, "ca")
# for word in word_list:
#     print(word)
