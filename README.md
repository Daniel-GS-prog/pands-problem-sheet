# pands-problem-sheet

Week 2 -- bmi.py:
    Takes height(meters) and weight(kg) from user and returns the Body Mass Index Calculation with range.

    A. Steps:
        1. Takes in values from user.
        2. Performs calculations.
        3. Returns results.

    B. References:
        Alastair Hazell. “BMI Formula - How to Use the BMI Formula.” Thecalculatorsite.com, 2021, www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php. Accessed 19 Mar.2021.

        “Includehelp.” Includehelp.com, 2017, www.includehelp.com/python/bmi-body-mass-index-calculator.aspx. Accessed 19 Mar. 2021.



Week 3 -- secondstring.py
    Takes in a string and returns the reverse skipping one position.

    A: Steps:
        1. Takes the variable string.
        2. Creates a slice from the end of the string

    B. References:
        How to reverse a String in Python. (2021). Retrieved March 19, 2021, from W3schools.com website: https://www.w3schools.com/python/python_howto_reverse_string.asp

‌

Week 4 -- collatz.py
    Takes integer from user. Performs calculation depending on wheter it's odd or even until result is 0.

    A. Steps:
        1. Takes input from the user.
        2. empty list to be populated by the loop .
        3. Assigns the input as the first character of the list.
        4. Condition 1, addition to list and updat the value of x.
        5. Condition 2, addition to list and updat the value of x.

    B. References:
        “while” loop nested within “for” loop - MATLAB Answers - MATLAB Central. (2015). Retrieved March 19, 2021, from Mathworks.com website: https://www.mathworks.com/matlabcentral/answers/246944-while-loop-nested-within-for-loop

        LeBrun. (2016, April 25). While loop with if/else statement in Python. 
        Retrieved March 19, 2021, from Stack Overflow website: https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python/36843356

‌

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
        “8.1. Datetime — Basic Date and Time Types — Python 2.7.18 Documentation.” Python.org, 2013, docs.python.org/2/library/datetime.html#strftime-strptime-behavior. Accessed 19 Mar. 2021.

        “Datetime — Basic Date and Time Types — Python 3.9.2 Documentation.” Python.org, 2019, docs.python.org/3/library/datetime.html. Accessed 19 Mar. 2021.frazman. 

        “How Do I Get the Day of Week given a Date?” Stack Overflow, 23 Mar. 2012, stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date. Accessed 19 Mar. 2021.



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
        Allen, Michael. “64. NumPy: Setting Width and Number of Decimal Places in NumPy Print Output.” Python for Healthcare Modelling and Data Science, Python for healthcare modelling and data science, 15 Apr. 2018, pythonhealthcare.org/2018/04/15/64-numpy-setting-width-and-number-of-decimal-places-in-numpy-print-output/. Accessed 19 Mar. 2021.
        
        “Decimal — Decimal Fixed Point and Floating Point Arithmetic — Python 3.9.2 Documentation.” Python.org, 2021, docs.python.org/3/library/decimal.html. Accessed 19 Mar. 2021.
        
        Jianna. “Newton’s Method for Approximating Square Roots.” Stack Overflow, 19 Mar. 2019, stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots. Accessed 19 Mar. 2021.
        
        “Newton’s Square Root Approximation by Ron Kurtus - Succeed in Understanding Algebra: School for Champions.” School-For-Champions.com, 2012, www.school-for-champions.com/algebra/square_root_approx.htm#.YDbjvGj7QuU. Accessed 19 Mar. 2021.
        
        “Print Floats to a Specific Number of Decimal Points in Python - CodeSpeedy.” CodeSpeedy, 5 Sept. 2019, www.codespeedy.com/print-floats-to-a-specific-number-of-decimal-points-in-python/. Accessed 19 Mar. 2021.
        
        Real Python. “The Python Square Root Function.” Realpython.com, Real Python, 8 July 2019, realpython.com/python-square-root-function/. Accessed 19 Mar. 2021.



week 7 -- es.py:
    Counts the occurence of a character in a file.

    A. steps:
    1. Define file as variable "filename".
    define function with two parameters: "file", "letter to count".

    
    B. References:
        “Count Occurrence of Character in File Using Python - CodeSpeedy.” CodeSpeedy, 16 Mar. 2020, 
        www.codespeedy.com/count-occurrence-of-character-in-file-using-python/. Accessed 5 Mar. 2021.

        “Python – Count Number of Characters in Text File - Python Examples.” 
        Pythonexamples.org, 2021, pythonexamples.org/python-count-number-of-characters-in-text-file/. Accessed 5 Mar. 2021.Yamac Candan. 

        “Python - Counting the Number of Characters in Files.” Stack Overflow, 31 Aug. 2017, 
        stackoverflow.com/questions/45974386/python-counting-the-number-of-characters-in-files#45974638. Accessed 5 Mar. 2021.



week 8 -- plottask.py:
    Displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

    A. steps:
        1. Importing modules.
        2. Defining varibles
        3. Defining plots.
        4. Decoration.
    
    B. References:
        “API Overview — Matplotlib 3.3.4 Documentation.” Matplotlib.org, 2012, matplotlib.org/stable/api/index.html#usage-patterns. Accessed 12 Mar. 2021.Bhavika Kanani. 

        “Matplotlib - Graph Decoration - Machine Learning Tutorials.” Machine Learning Tutorials, 13 Sept. 2019, studymachinelearning.com/matplotlib-graph-decoration/. Accessed 12 Mar. 2021.

        “How to Change Background Color in Matplotlib with Python - CodeSpeedy.” CodeSpeedy, 24 Sept. 2019, www.codespeedy.com/change-background-color-in-matplotlib-with-python/. Accessed 12 Mar. 2021.

        “Matplotlib.pyplot.colors() in Python - GeeksforGeeks.” GeeksforGeeks, 20 Apr. 2020, www.geeksforgeeks.org/matplotlib-pyplot-colors-in-python/. Accessed 12 Mar. 2021.

        “Matplotlib.pyplot.plot — Matplotlib 3.3.4 Documentation.” Matplotlib.org, 2012, matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot. Accessed 12 Mar. 2021.

        “Matplotlib.pyplot.title() in Python - GeeksforGeeks.” GeeksforGeeks, 12 Apr. 2020, www.geeksforgeeks.org/matplotlib-pyplot-title-in-python/. Accessed 12 Mar. 2021.

        “Tutorials — Matplotlib 3.3.4 Documentation.” Matplotlib.org, 2012, matplotlib.org/stable/tutorials/index.html#tutorials. Accessed 12 Mar. 2021.