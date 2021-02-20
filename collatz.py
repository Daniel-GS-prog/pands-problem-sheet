# Asks the user to input any positive integer.
# If it is even, divide it by two. If it is odd, multiply it by three and add one.
# Program ends if value is 1.
# References:
# https://www.mathworks.com/matlabcentral/answers/246944-while-loop-nested-within-for-loop
# https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python/36843356

# Author: Daniel Gonzalez




i = int(input(': ')) # takes input from user
numbers = []        # empty list to be populated by the loop
numbers.append(i)   # first character of the list
x = i               # sets user's input to variable in loop

while x != 1:
    if x % 2 == 0:          #condition one
        numbers.append(x/2) # list appends character
        x = x/2             # updates value of x
    else:                           # condition two
        numbers.append(x * 3 + 1)   # list appends character
        x= x * 3 + 1                # updates the value of x
    
print(numbers) # Prints results

   