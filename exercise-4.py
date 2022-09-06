# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the lengths of three sides of a triangle in cm ')

a = input("a: ")
b = input("b: ")
c = input("c: ")
triangle = ''

if a == b: 
    #If A = B = C 
    if b == c:
        triangle = 'equalateral'
        print(f"A triangle with sides of {a}cm, {b}cm & {c}cm is a {triangle} triangle")
    else: 
        triangle = 'isocoles'
        print(f"A triangle with sides of {a}cm, {b}cm & {c}cm is a {triangle} triangle")

elif b == c: 
    #If B = C = A 
    if c == a:
        triangle = 'equalateral'
        print(f"A triangle with sides of {a}cm, {b}cm & {c}cm is a {triangle} triangle")
    #If B = C != A
    else: 
        triangle = 'isocoles'
        print(f"A triangle with sides of {a}cm, {b}cm & {c}cm is a {triangle} triangle")

elif c == a: 
    #If C = A = B 
    if a == b:
        triangle = 'equalateral'
        print(f"A triangle with sides of {a}cm, {b}cm & {c}cm is a {triangle} triangle")
    #If C = A != B 
    else: 
        triangle = 'isocoles'
        print(f"A triangle with sides of {a}cm, {b}cm & {c}cm is a {triangle} triangle")

else: 
    triangle = 'scalene'
    print(f"A triangle with sides of {a}cm, {b}cm & {c}cm is a {triangle} triangle")

