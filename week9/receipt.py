# Calvin Bullock, June 13th


# Found this here
# https://stackoverflow.com/questions/10079216/skip-first-entry-in-for-loop-in-python
from itertools import islice


def main():
    # Test file names
    # Filename = "request.csv"
    filename = "products.csv"

    # Read the file and return the dictinary
    products_dict = read_dictionary(filename, 0)
    print(products_dict)


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
    with open(filename) as file:
        # loops trought the file but skips the first line
        for line in islice(file, 1, None):
            # Splits the file lines into an array
            line = line.strip()
            array = line.split(",")

            products_dict[array[key_column_index]] = array

    # Closes file.
    file.close()

    return products_dict


if __name__ == "__main__":
    main()
