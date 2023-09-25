# Larry Hurley
# 9/25/2023
# Calculate cost of driving

# Get input from user as float
mpg = float(input("How many mpg does the car get"))
gas_price = float(input("How much does one gallon of gas cost"))

# Calculate cost
twenty_miles = (20/mpg) *gas_price
seventyfive_miles = (75/mpg) *gas_price
fivehundred_miles = (500/mpg) *gas_price

#Display to user 
print(f'The cost to drive 20 miles:_{twenty_miles:.2f}')
print(f'The cost to drive 75 miles:_{seventyfive_miles:.2f}')
print(f'The cost to drive 500 miles:_{fivehundred_miles:.2f}')
