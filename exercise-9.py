# exercise-9 The Coin Problem

# Write code that accepts an input of a dollar amount
# and returns to the user the FEWEST amount of
# coins that will add up to that total. Coins available:
# $2
# $1
# $0.25
# $0.10
# $0.05
# $0.01

dollars = input("Enter a dollar amount (eg, 29.84): ")

# Print out: "$x can be made with x Twonies, x Loonies, x quarters...."

dollars = float(dollars) 
print(f"DOLLARS {dollars}")
total = dollars 

toonies = 0 
loonies = 0 
quarters = 0 
dimes = 0
nickels = 0 
pennies = 0 

while dollars > 0:
    if dollars >= 2.00: 
        dollars = dollars - 2
        toonies = toonies + 1
    elif dollars >= 1.00: 
        dollars = dollars - 1
        loonies = loonies + 1 
    elif dollars >= 0.25:
        dollars = dollars - 0.25
        quarters = quarters + 1
    elif dollars >= 0.1: 
        dollars = dollars - 0.1
        dimes = dimes + 1
    elif dollars >= 0.05:
        dollars = dollars - 0.05
        nickels = nickels + 1
    else:
        dollars = dollars - 0.01 
        pennies = pennies + 1
print(f"${total} can be made with {toonies} toonies, {loonies} loonies, {quarters} quarters, {dimes} dimes, {nickels} nickels and {pennies} pennies")
