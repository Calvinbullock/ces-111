# Calvin Bullock, June 13th
# Team 9

import csv


def main():
    # # Collect I number from user
    # byu_i_num = input("Please enter an I-Number (xxxxxxxxx): ")

    # # Testing I-nums
    # byu_i_num = "551234151"
    byu_i_num = "751766201"

    # Open and read file
    filename = "students.csv"
    student_dict = read_dictionary(filename, 0)

    # Check if the students number is in the dictinary
    if byu_i_num in student_dict:
        print(student_dict[byu_i_num][1])
    else:
        print("No such student.")


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
    products_dict = {}

    # Reads the lines of the file into an array
    with open(filename) as file:
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
