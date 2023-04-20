"""
Calvin Bullock - April 29th 2023

This program asks the user for a box and 
"""

import math

items = input("Enter the number of items: ") 
per_box = input("Enter the number of items per box: ")

items = int(items)
per_box = int(per_box)

answer = items / per_box
answer = math.ceil(answer)

print(f"For {items} items, packing {per_box} items in each box, you will need {answer} boxes.")




""" test out put
> python boxes.py
Enter the number of items: 8
Enter the number of items per box: 5

For 8 items, packing 5 items in each box, you will need 2 boxes.

> python boxes.py
Enter the number of items: 25
Enter the number of items per box: 4

For 25 items, packing 4 items in each box, you will need 7 boxes.
"""