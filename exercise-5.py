# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

  
counter = 0 
cur_num = 0
num2 = 0
num3 = 0

while counter <= 50: 
    

    if cur_num == 0:
        print(f"Term: {counter}, Number: {cur_num} ")
        counter = counter + 1
        cur_num =+ 1 

    else:
        print(f"Term: {counter}, Number: {cur_num} ")
        
        num2 = cur_num
        cur_num = cur_num + num3
        num3 = num2
        
        
        counter = counter + 1