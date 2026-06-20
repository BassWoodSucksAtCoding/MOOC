# Write your solution here
def read_input(input_text,lower_bound,upper_bound):
    while True:
        try:
            number = int(input(input_text))
            if number > lower_bound and number < upper_bound:
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {lower_bound} and {upper_bound}")
