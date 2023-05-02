
def main():
    # Get an odometer value in U.S. miles from the user.
    odom_start = input("A starting odometer value in miles: ")

    # Get another odometer value in U.S. miles from the user.
    odom_end = input("An ending odometer value in miles: ")

    # Get a fuel amount in U.S. gallons from the user.
    fuel_amt_gal = input("inputAn amount of fuel in gallons: ")

    # Quick test values
    odom_start = 30462
    odom_end = 30810
    fuel_amt_gal = 11.2

    # Cast input strings to ints 
    odom_end = int(odom_end)
    odom_start = int(odom_start)
    fuel_amt_gal = float(fuel_amt_gal)

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(odom_start, odom_end, fuel_amt_gal)
    print(mpg)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    print(lp100k)

    # Display the results for the user to see.
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.

    Return: 
    Fuel efficiency in miles per gallon.
    """
    print(end_miles, start_miles, amount_gallons)
    mpg = round((end_miles - start_miles) / amount_gallons, 2)

    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter:
    mpg: A value in miles per gallon
    
    Return:
    The converted value in liters per 100km.
    """
    lp100k = round(235.215 / mpg, 2)

    return lp100k


# Call the main function so that
# this program will start executing.
main()