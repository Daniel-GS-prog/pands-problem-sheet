# Asks the user to input any positive integer.
# If it is even, divide it by two. If it is odd, multiply it by three and add one.
# Program ends if value is 1.


# Author: Daniel Gonzalez


def collatz(n):
    numbers = []    
    # empty list to be populated by the loop 
    numbers.append(n)   
    # first character of the list


    while n != 1:
        if n % 2 == 0:         
            numbers.append(n/2) 
            # list appends character
            n = n/2             
            # updates value of x
        else:                           
            numbers.append(n * 3 + 1)   
            # list appends character
            n= n * 3 + 1                
            # updates the value of x
        
    return "list is: {}.".format(numbers) # Prints results



print(collatz(int(input('enter your number: '))))