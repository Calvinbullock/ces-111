# Calvin Bullock


# Found this here
# https://stackoverflow.com/questions/10079216/skip-first-entry-in-for-loop-in-python
from itertools import islice


def main():
    filename = "request.csv"
    # filename = "products.csv"
    products_dict = read_dictionary(filename, 0)
    print(products_dict)


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Opens a file and returns an array from it
    try:
        pass
    except:
        print("Could not find the file, please check the file and try again ")

    if True:
        # Reads the lines of the file into an array
        products_dict = {}
        with open(filename) as file:
            for line in islice(file, 1, None):  # broken....
                line = line.strip()
                array = line.split(",")
                # print(array)

                products_dict[array[key_column_index]] = array

        # Closes file.
        file.close()
        
        return products_dict



main()
