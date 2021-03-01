
# Takes the user´s height in (meters) and weight (in kg) and returs the body mass index
# Author: Daniel Gonzalez




def bmi(name, height, weight):

    print(('\n-------------------------------'))
    bmi = weight / (height**2)
    userBmi = round(bmi, 2)
    # All values and calulations
    if userBmi < 18.5: 
    # Comparions and results returned
        return "{}, your bmi is {}. It's a little too low. Please go eat something.\n.".format(name, userBmi)
    elif 18.5 <= userBmi <= 24.9:
        return "{}, your bmi is {}. It's at healthy levels! Congrats.\n".format(name, userBmi)
    else:
        return "{}, your bmi is {}. It's a bit too high.\n".format(name, userBmi)
    print('------------------------------')
            

print(bmi(input('\nEnter your name: '), float(input('enter your height in meters: ')), float(input('enter your weight in kg: '))))




    
