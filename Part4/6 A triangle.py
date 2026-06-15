# Copy here code of line function from previous exercise
def line(times, text):
    if text == "":
        print("*"*times)
    else:
        print(text[0]*times)

def triangle(size):
    # You should call function line here with proper parameters
    for row in range(1,size+1):
        line(row, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
