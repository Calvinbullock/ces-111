# Calvin Bullock, June 13th
# Prove 10

import sys
import csv
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

TAX_RATE = 0.06


def main():
    """
    This program will take two csv files one that has an order and the other
    that has products and their info.
    the program will then take the order and print a receipt of the order
    based on the products data.
    """
    # Read the file and return the dictinary
    products_dict = read_dictionary("products.csv", 0)
    request_list = read_list("request.csv")
    
    list_user_order(products_dict, request_list)


def read_list(filename):
    """Read the contents of a CSV file into a two dimentinal array.

    Parameters
        filename: the name of the CSV file to read.
    Return: a two dementinal array that contains
        the contents of the CSV file.

    """
    # Reads the lines of the file into an array
    products_list = []

    try:
        with open(filename, "rt") as file:
            # uses the csv reader to clean up csv data
            reader = csv.reader(file)
            # saves then skips the csv header
            header = next(reader, None)

            index = 0
            # saves each line to a dictinary pair
            for row_list in reader:
                products_list.append(row_list)
                index += 1

        # Closes file.
        file.close()

    except FileNotFoundError:
        print(f"Could not find file: {filename}")
        sys.exit()

    except PermissionError:
        print(f"You do not have permisttion to acces this file: {filename}.")
        sys.exit()

    return products_list


def read_dictionary(filename, key_column_index=0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Reads the lines of the file into an array
    products_dict = {}
    try:
        with open(filename, "rt") as file:
            # uses the csv reader to clean up csv data
            reader = csv.reader(file)
            # saves then skips the csv header
            header = next(reader, None)

            # saves each line to a dictinary pair
            for row_list in reader:
                products_dict[row_list[key_column_index]] = row_list

        # Closes file.
        file.close()

    except FileNotFoundError:
        print(f"Could not find file: {filename}")
        sys.exit()

    except PermissionError:
        print(f"You do not have permisttion to acces this file: {filename}.")
        sys.exit()

    return products_dict


def list_user_order(products_dict, request_list):
    """
    This function uses a dictinary of products in the store
    and a two dimentinal array of a users order to parse the users
    order into the store data base and pull out the product info then
    print the order's receipt.

    Parameters
            products_dict: A dictinary with the stores product info.
            request_list: a two dementinal array that stores the users
                order info.

    """
    # Instilize for multi loop scope
    total_items = 0
    subtotal = 0

    # Start the recipte printing
    print("Inkom Emporium")
    print()

    try:
        # Parses and prints the orderd products info
        for item_info in request_list:
            product_key = item_info[0]
            order_info_list = item_info
            product_info_list = products_dict[product_key]
            product_qty = int(order_info_list[1])
            product_name = product_info_list[1]
            product_price = float(product_info_list[2])

            print(f"{product_name}: {product_qty} @ {product_price}")

            total_items += product_qty
            subtotal += product_qty * product_price

        sales_tax = subtotal * TAX_RATE
        total_cost = sales_tax + subtotal

    except KeyError:
        print()
        print(f"Invalid key in products_dict: {product_key}")
        sys.exit()

    print()
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal :.2f}")
    print(f"Sales Tax: {sales_tax :.2f}")
    print(f"Total: {total_cost :.2f}")

    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%c}")


if __name__ == "__main__":
    main()


# TODO this program needs to do:
# Include a try block and except blocks to handle **FileNotFoundError, **PermissionError, and KeyError.
# Add main function description


# EXSPECTED OUTPUT
# Inkom Emporium

# wheat bread: 2 @ 2.55
# 1 cup yogurt: 4 @ 0.75
# 32 oz granola: 1 @ 3.21
# twix candy bar: 2 @ 0.85
# 1 cup yogurt: 3 @ 0.75

# Number of Items: 12
# Subtotal: 15.26
# Sales Tax: 0.92
# Total: 16.18

# Thank you for shopping at the Inkom Emporium.
# Wed Nov  4 05:10:30 2020
