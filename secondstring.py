# Takes in a string from the user. 
# Returns every second letter in reverse order.
# Author: Daniel Gonzalez


def get_string():
    # asks user for a string 
    return input("Enter string: ")

def second_string():
    # Prints the string backwards skiping one position
    string = get_string()
    a =  string[-1::-2]
    return a

print(second_string())

