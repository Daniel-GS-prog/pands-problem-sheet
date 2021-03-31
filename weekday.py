# outputs whether or not today is a weekday.
# Author: Daniel Gonzalez


from datetime import datetime


def is_it_weekday(a):
    today = datetime.today().strftime('%A')
    # Gets today's day of the week

    if today in a[5:6]:
    # Compares today's day of the week with the last two days of the week.
        return '\nIt is the weekend, yay!\n'
    # If they match, today is Saturday or Sunday.

    else:
        return '\nYes, unfortunately today is a weekday.\n'
    # No match before. It's a weekday



daysOfTheWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday")
# Tuple (immutable) for the days of the week.


print(is_it_weekday(daysOfTheWeek))