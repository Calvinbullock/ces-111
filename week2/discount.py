from datetime import datetime


TAX = .06
DISCOUNT = .10

# takes user imput for subtotal and turns it into a float
subtotal = input("Enter subtotal: ")
subtotal = float(subtotal)

# gets the date and time from the computer
time_and_date = datetime.now()
day_of_week = time_and_date.weekday()

# checks if the user is viable for discount
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):

    # computes the discount
    subtotal = round(subtotal * DISCOUNT) + subtotal


# Calculates the sales tax
sales_tax = round(subtotal * TAX)
total = sales_tax + subtotal


# Displays the time, date and total    
print(f"Sales tax is {sales_tax}.")
print(f"your Total at {time_and_date:%Y-%m-%d} was {total}.")




"""
Your program asks the user for the subtotal but does not ask the user for the day of the week. 
Your program gets the day of the week from your computer's operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.
"""