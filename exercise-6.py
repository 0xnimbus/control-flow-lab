# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec): ')
day = input('Enter the day of the month: ')

# Winter 
if month in ('Dec', 'Jan', 'Feb', 'Mar'):
    if month == 'Mar':
        if day <= 19:
            print(f"{month} {day} is in Winter")
    elif month == 'Dec':
        if day >= 21: 
            print(f"{month} {day} is in Winter")
    elif month == 'Jan':
        print(f"{month} {day} is in Winter")
    elif month == 'Feb':
        print(f"{month} {day} is in Winter")

# Spring 
elif month in ('Mar', 'Apr', 'May', 'Jun'):
    if month == 'Mar':
        if day > 19:
            print(f"{month} {day} is in Spring")
    elif month == 'Jun':
        if day <= 20: 
            print(f"{month} {day} is in Spring")
    elif month == 'April':
        print(f"{month} {day} is in Spring")
    elif month == 'May':
        print(f"{month} {day} is in Spring")

# Summer 
elif month in ('Jun', 'Jul', 'Aug', 'Sep'):
    if month == 'Jun':
        if day > 20:
            print(f"{month} {day} is in Summer")
    elif month == 'Sep':
        if day <= 21: 
            print(f"{month} {day} is in Summer")
    elif month == 'Aug':
        print(f"{month} {day} is in Summer")
    elif month == 'Sep':
        print(f"{month} {day} is in Summer")

# Fall 
elif month in ('Sep', 'Oct', 'Nov', 'Dec'):
    if month == 'Sep':
        if day >= 22:
            print(f"{month} {day} is in Fall")
    elif month == 'Oct':
        if day <= 20: 
            print(f"{month} {day} is in Fall")
    elif month == 'Nov':
        print(f"{month} {day} is in Fall")
    elif month == 'Dec':
        print(f"{month} {day} is in Fall")
else: 
    print('ERROR INVALID INPUTS')