# Write your solution here
def first_word(sentence):
    for letter in range(len(sentence)):
        if sentence[letter] == " ":
            return sentence[0:letter]

def second_word(sentence):
    counter = 0
    start_index = 0
    for letter in range(len(sentence)):
        if sentence[letter] == " " and counter == 1:
            return sentence[start_index:letter]
        
        if (letter == len(sentence)-1) and counter == 1:
            return sentence[start_index:letter+1]
        
        if sentence[letter] == " " and counter == 0:
            counter += 1
            start_index = letter+1
        
def last_word(sentence):
    for letter in range(len(sentence)-1,0,-1):
        if sentence[letter] == " ":
            return sentence[letter+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    #sentence = "once upon a time there was a programmer"
    sentence = "first second"
    #print(first_word(sentence))
    print(second_word(sentence))
    #print(last_word(sentence))
