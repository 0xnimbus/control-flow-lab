# exercise-7 Seconds to Minutes, Hours

# Write code that will take in an input from the user
# in seconds. Convert that number into minutes, and print:
# "x seconds is equal to x minutes and x seconds"



# Bonus:
# if the total minutes is more than an hour, calculate the number
# of hours as well
# "x seconds is equal to x hours, x minutes, and x seconds"

seconds = input('Input an amount of seconds and it will be converted into minutes: ')
seconds = int(seconds)
minutes = 0 

while seconds >= 60:
    minutes = minutes + 1
    seconds = seconds - 60 
    

print(f"This converts to {minutes} minutes and {seconds} seconds")
    
