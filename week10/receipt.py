# Calvin Bullock, June 13th
# Milestone 9


import csv
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

TAX_RATE = .06

def main():
    # Test file names
    # Filename = "request.csv"
    filename = "products.csv"

    # Read the file and return the dictinary
    products_dict = read_dictionary(filename, 0)
    print(products_dict)


    # Inkom Emporium

    = input("wheat bread: ") #2 @ 2.55
    = input("1 cup yogurt: ") #4 @ 0.75
    = input("32 oz granola: ") #1 @ 3.21
    = input("twix candy bar: ") #2 @ 0.85
    = input("1 cup yogurt: ") #3 @ 0.75


def read_list(filename):
    """Read the contents of a CSV file into a two dimentinal array.

    Parameters
        filename: the name of the CSV file to read.
    Return: a two dementinal array that contains
        the contents of the CSV file.

    """
    # Reads the lines of the file into an array
    products_list = []

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
    total_items = 0
    subtotal = 0
    sales_tax = 0
    total_cost = 0

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
    
    print()
    print(f"Number of Items: {total_items}")  # 12
    print(f"Subtotal: {subtotal :.2f}")  # 15.26
    print(f"Sales Tax: {sales_tax :.2f}")  # 0.92
    print(f"Total: {total_cost :.2f}")  # 16.18
    print()


if __name__ == "__main__":
    main()
