# Calvin Bullock, June 13th
# Team 9

# Found this here
# https://stackoverflow.com/questions/10079216/skip-first-entry-in-for-loop-in-python
from itertools import islice


def main():
    # # Collect I number from user
    # byu_i_num = input("Please enter an I-Number (xxxxxxxxx): ")

    # # Testing I-nums
    byu_i_num = "551234151"
    # byu_i_num = "751766201"

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
    # Checks if file exsists
    try:
        # Reads the lines of the file into an array
        products_dict = {}
        with open(filename) as file:

            # loops trought the file but skips the first line
            for line in islice(file, 1, None):
                # Splits the file lines into an array
                line = line.strip()
                array = line.split(",")

                products_dict[array[key_column_index]] = array
    except:
        print("Could not find the file, please check the file and try again ")

    # Closes file.
    file.close()

    return products_dict


if __name__ == "__main__":
    main()
