# Write your solution here
def dict_of_numbers():
    units_digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens_digits = ["none","teen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    numbers = {}


    for tens in range(0,10):
        for units in range(0,10):
            if tens == 0:
                numbers[units] = units_digits[units]
            elif tens == 1:
                numbers[tens*10+units] = teens[units]  
            else:
                if units == 0:
                    numbers[tens*10+units] = tens_digits[tens]
                else:
                    numbers[tens*10+units] = f"{tens_digits[tens]}-{units_digits[units]}"
            

    return numbers


