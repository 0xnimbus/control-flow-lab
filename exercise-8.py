# exercise-8 The Farm Problem

# In this challenge, a farmer is asking you to tell 
# him how many legs can be counted among all his animals. 
# The farmer breeds three species:

# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs

# The farmer has counted his animals and he gives you a 
# subtotal for each species. You have to implement  
# code that returns the total number of legs of all the animals.

animals = input('Enter the amount of chickens, cows and pigs separated by a - : ')
animals= animals.split('-')
print(animals)

chickens = int(animals[0])
cows = int(animals[1])
pigs = int(animals[2])

legs = (chickens * 2) + (cows * 4 ) + (pigs * 4)
print(f"There are {legs} legs total in the farm")
