"""
Calvin Bullock - April 20, 2023

This file computes the volume of a tire.
To do this the program asks for user imput for width, aspect ratio, 
diamiter.The program will retun the aproxamite volume in liters.
"""

from math import pi

width = input("Enter the width of the tire in mm (ex 205):")
aspect_ratio = input("Enter the aspect ratio of the tire (ex 60):")
diamater = input("Enter the diameter of the wheel in inches (ex 15): ")

width = int(width)
aspect_ratio = int(aspect_ratio)
diamater = int(diamater)

volume = ((pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diamater)) / 10000000000)

print(f"The approximate volume is {volume:.2f} liters")

# - - Exsamples - - 
# Enter the width of the tire in mm (ex 205): 185
# Enter the aspect ratio of the tire (ex 60): 50
# Enter the diameter of the wheel in inches (ex 15): 14

# The approximate volume is 24.09 liters

# > python tire_volume.py
# Enter the width of the tire in mm (ex 205): 205
# Enter the aspect ratio of the tire (ex 60): 60
# Enter the diameter of the wheel in inches (ex 15): 15

# The approximate volume is 39.92 liters