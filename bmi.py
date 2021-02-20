
# Takes the user´s height in (meters) and weight (in kg) and returs the body mass index
# Author: Daniel Gonzalez

print(('\n-------------------------------'))
print('Welcome to he BMI calculator!')

name = input('\nWhat´s your name: ')
print('Hello, {}. Nice to meet you!'. format(name))

#User´s values:
weight = float(input('\nPlease enter your weight in kg: '))
height = float(input('Please enter your height in meters: '))
bmi = weight / (height**2)

#Returns user´s BMI:
print('\nYour Body Mass Index is: {0:.2f}'. format(bmi))

#cathegories:
if bmi < 18.5:
    print('Your bmi is a little too low. Please go eat something.')
elif 18.5 <= bmi <= 24.9:
    print('Ypur bmi is at healthy levels! Congrats')
else:
    print('Your bmi is a bit too high.')
print('------------------------------')
    