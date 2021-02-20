# outputs whether or not today is a weekday.
# Author: Daniel Gonzalez

# 1.
from datetime import datetime

# 2.
daysOfTheWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday")
 # Tuple (immutable) for the days of the week.

# 3.
today = datetime.today().strftime('%A')
 # Gets today's day of the week

# 4.
if today in daysOfTheWeek[5:6]:
    # Compares today's day of the week with the last two days of the week.
    print('\nIt is the weekend, yay!\n')
    # If they match, today is Saturday or Sunday.

else:
    print('\nYes, unfortunately today is a weekday.\n')
    # No match before. It's a weekday

