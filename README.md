# pands-problem-sheet

Week 2 --
- bmi.py:


Week 4 -- collatz.py

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
    outputs whether or not today is a weekday.

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