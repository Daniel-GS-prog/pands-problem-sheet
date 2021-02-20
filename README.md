# pands-problem-sheet

Week 2 --
- bmi.py:


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