# need date time to find todays time
from datetime import datetime

# COnstattns of state tax and company discount
TAX = .06
DISCOUNT = .10

# Quick debug / test
# subtotal = 42.31

# Takes user imput for subtotal and turns it into a float
Subtotal = input("Enter subtotal: ")
subtotal = float(subtotal)

# This exspands the scope of sales_discount
sales_discount = 0.0

# Gets the date and time from the computer
time_and_date = datetime.now()
day_of_week = time_and_date.weekday()

# Checks if the user is viable for discount
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):

    # computes the discount
    sales_discount = round(subtotal * DISCOUNT, 2)
    print(f"disc: {sales_discount}")

# Calculates the sales tax
sales_tax = round((subtotal - sales_discount) * TAX, 2)

# Caculates the total with ot with out the discount
total = round(subtotal + sales_tax - sales_discount, 2)


# Displays the time, date and total
print(f"Sales tax is {sales_tax}.")
print(f"your Total at {time_and_date:%Y-%m-%d} was {total}.")




"""
Your program asks the user for the subtotal but does not ask the user for the day of the week. 
Your program gets the day of the week from your computer's operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.
"""