# pands-problem-sheet

Week 2 -- bmi.py:
    Takes height(meters) and weight(kg) from user and returns the Body Mass Index Calculation with range.

    A. Steps:
        1. Takes in values from user.
        2. Performs calculations.
        3. Returns results.

    B. References:
        1. Calculations:
            https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php

        2. Code and comparison:
            https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx



Week 3 -- secondstring.py
    Takes in a string and returns the reverse skipping one position.

    A: Steps:
        1. Takes the variable string.
        2. Creates a slice from the end of the string

    B. References:
        1. https://www.w3schools.com/python/python_howto_reverse_string.asp



Week 4 -- collatz.py
    Takes integer from user. Performs calculation depending on wheter it's odd or even until result is 0.

    A. Steps:
        1. Takes input from the user.
        2. empty list to be populated by the loop .
        3. Assigns the input as the first character of the list.
        4. sets user's input to variable in loop.
        5. Condition 1, addition to list and updat the value of x.
        6. Condition 2, addition to list and updat the value of x.

    B. References:
        1. https://www.mathworks.com/matlabcentral/answers/246944-while-loop-nested-within-for-loop

        2.https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python/36843356



week 5 -- weekday.py:
    Returns whether or not today is a weekday.

    A. steps: 
        1. Import datetime module.
        2. Define the days of the week in a tupple (immutable) for comparison.
        3. Define today's day of the week using datetime.today(), 
            and strftime('%A') for Capitalized names.
        4. Comparison between today's day of the week the last two days
            of the tupple (Weekend days). Simpler than going through the other five days.

    B. References:
        1. Documentation:
            1.1 https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
            1.2 https://docs.python.org/3/library/datetime.html
        
        2. Example of code:
            https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date



week 6 -- squareroot.py:
    Calculates the square root of a positive integer.

    A. steps:
        1. Make sure the number is a positive float.
        2. defines first candidate (number/2).
        3. Defines parameter for calculations.
        4. Reduces the gap between first and final candidate.
        5. Brings python built-in function to compare both results.
        6. Returns both values

    B. References:
        1. Calculations:
            1.1 https://www.school-for-champions.com/algebra/square_root_approx.htm#.YDbjvGj7QuU

            1.2 https://docs.python.org/3/library/decimal.html

            1.3 Defining accuracy: 
                https://duckduckgo.com/?q=tolerance+in+python&atb=v262-2&ia=web

            1.4 https://pythonhealthcare.org/2018/04/15/64-numpy-setting-width-and-number-of-decimal-places-in-numpy-print-output/

            1.5 https://www.codespeedy.com/print-floats-to-a-specific-number-of-decimal-points-in-python/

            1.6 Python square root function: 
                https://realpython.com/python-square-root-function/


        2. Example of code:

            2.1 Specifically comparing with python buil-in function:
                https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots