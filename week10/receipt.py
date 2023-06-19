# Calvin Bullock, June 13th
# Milestone 9


import csv


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


if __name__ == "__main__":
    main()
