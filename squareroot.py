 # Returns the square root of a floating positive number.
 # Author: Daniel Gonzalez

import math

def squareRoot(number):

    while number <= 0:
    # Makes sure the number is a positive float
        print('number must be positive float')
        number = float(input('Calculate the square root of: '))

    candidate = number/2
    # Starting point

    difference = 1
    accuracy = 0.000001
    # Parameters for calculation

    while difference > accuracy:
    # Loop to determine the candidate
        x = 0.5* (candidate + (number/candidate))
        difference = candidate - x
        # Reducing the gap between the initial candidate and final result
        candidate = x
        # Reassigning value to candidate

    pythonFunction = math.sqrt(number)
    # Brings python in-built function to compare results

    print('\nPython function says: {}.'.format(pythonFunction))
    return 'Our function says: {}.\n'.format(candidate)


print(squareRoot(float(input('Calculate the square root of (positive float): '))))

