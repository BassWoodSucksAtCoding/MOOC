# Write your solution here
def spruce(height):
    print("a spruce!")
    left_space = height-1
    for row in range(height):
        print(" "*(left_space-row) + ("*"*row)*2 + "*")

    print(" "*left_space+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
