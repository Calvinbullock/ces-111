"""
Calvin Bullock - April 25, 2023

This file computes the volume of a tire.
To do this the program asks for user imput for width, aspect ratio, 
diamiter.The program will retun the aproxamite volume in liters.

The program will print the width, aspect_ratio, diamater, and volume
to the console.

It will then pass the time, date, width, aspect_ratio, diamater, 
and volume to a text file names volume.txt.
"""

from math import pi
from datetime import datetime

def TireVolume(width, aspect_ratio, diamater):
    """
    Takes 3 ints and use them to calculate the volume of a tire.

    Parameters:
    width           (int): width in the volume formula.
    aspect_ratio    (int): aspect ratio in the volume formula
    diamater        (int): diamater in the volume formula

    returns:
    The volume as a float.
    """
    # computes the volume of a tire with the passed in width, aspect-ratio,
    # and diamiter
    volume = ((pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diamater)) / 10000000000)
    return volume

def Write_To_File(purches_confirmation, width, aspect_ratio, diamater, volume):
    """
    Takes 5 ints/floats and a string and writes them to a txt file.

    Parameters:
    purches_confirmation    (float/int) used if phone_num is printed and filed.  
    width                   (float/int) prints it to the console and a file.
    aspect_ratio            (float/int) prints it to the console and a file.
    diamater                (float/int) prints it to the console and a file.
    volume                  (float/int) prints it to the console and a file.

    returns:
    Nothing
    """
    phone_num = ""

    # opns a file named volume.txt
    with open("volumes.txt", "at") as volume_file:
        
        if (purches_confirmation == "y"):
            phone_num = input("Enter your phone number: ")
            
        # Print a city's name and information to the file.
        print(
            f"{time_and_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diamater}, {volume:.2f}, {phone_num}",
            file = volume_file)

# Quick test case ----
# width = 185
# aspect_ratio = 50
# diamater = 14

# Takes user input # comment out for quick testing
width = input("Enter the width of the tire in mm (ex 205): ")
aspect_ratio = input("Enter the aspect ratio of the tire (ex 60): ")
diamater = input("Enter the diameter of the wheel in inches (ex 15): ")

# Changes the input from string to ints
width = int(width)
aspect_ratio = int(aspect_ratio)
diamater = int(diamater)

# Calls TireVolume to compute the volume and
# uses datetime to retreve the curent time and date.
volume = TireVolume(width, aspect_ratio, diamater)
time_and_date = datetime.now(tz=None)

# Final print out.
print(f"\nThe approximate volume is {volume:.2f} liters")

# Compares the width of the tire to find the minimum cost of the tire in $.
if width >= 205:
    cost = "200.99"
elif width >= 185:
    cost = "176.99"
elif width >= 175:
    cost = "165.99"
elif width >= 165:
    cost = "60.99"

# Asks to confirm if they want to purches the tire.
purches_confirmation = input(f"The cost is ${cost}. Do you want to purches this tire size (y/n): ")

# Functin writs to a file 
Write_To_File(purches_confirmation, width, aspect_ratio, diamater, volume)


# Tire prices and size ranges
"""
wi = 185
ar = 60
ra = 13
pr = $176

wi = 165
ar = 80
ra = 13
pr = $60

wi = 175
ar = 80
ra = 13
pr = $273
"""