"""
Calvin Bullock - April 29th 2023

This program asks the user for a the number of items they want to 
box and how many boxs they want to use. The program will then return 
the number of items that a box will have.
"""

import math

def items_in_box(items, per_box):
    """
    This function will take the input of items and the how many 
    items you want per box. Then it will return the number of boxes
    you will need.
    """

    items = int(items)
    per_box = int(per_box)

    box_num = items / per_box
    box_num = math.ceil(box_num)

    return box_num

items = input("Enter the number of items: ") 
per_box = input("Enter the number of items per box: ")

print(f"For {items} items, packing {per_box} items in each box, you will need {items_in_box(items, per_box)} boxes.")




""" test - out put
> python boxes.py
Enter the number of items: 8
Enter the number of items per box: 5

For 8 items, packing 5 items in each box, you will need 2 boxes.

> python boxes.py
Enter the number of items: 25
Enter the number of items per box: 4

For 25 items, packing 4 items in each box, you will need 7 boxes.
"""