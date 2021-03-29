
# Takes the user's height in (meters) and weight (in kg).
# returs the body mass index and classification.
# Author: Daniel Gonzalez


def main():
    # Calls all other functions
    # Returs user's BMI index and classification
    print(('\n-------------------------------'))
    name = get_name()
    height = get_height()
    weight = get_weight()
    userBmi = bmi(height, weight)
    bmiRange = bmiClassification(userBmi, name)
    return bmiRange
    

def get_name():
    # Requests and returns user's name
    return input("Enter name: ")


def get_height():
    # Requests and returns user's height
    return float(input("Enter height in meters: "))


def get_weight():
    # Requests and returns user's weight
    return float(input("Enter weight in kg: "))


def bmi(height, weight):
    # calculates bmi index from user's input (height and weight)
    # Retuns index limited to 2 decimal places
    a = weight / (height**2)
    return round(a, 2)


def bmiClassification(bmi, name):
    # Compares user's bmi with range.
    # Retuns low, normal or hight bmi index
    if bmi < 18.5: 
        return "\n{}, your bmi is {}. It's a little too low. Please go eat something.\n.".format(name, bmi)
    elif 18.5 <= bmi <= 24.9:
        return "\n{}, your bmi is {}. It's at healthy levels! Congrats.\n".format(name, bmi)
    else:
        return "\n{}, your bmi is {}. It's a bit too high.\n".format(name, bmi)


print(main())
