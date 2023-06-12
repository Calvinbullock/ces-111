def main():
    # file_name = input("Please enter a file name")
    file_name = "provinces.txt"

    array = open_file(file_name)

    print(array)
    print()

    string_replace(array)
    remove_element(array)

    print(array)
    print()

    count_alberta(array)


def open_file(file_name):
    assert type(file_name) == type("")

    # Opens a file and returns an array from it
    try:
        # Reads the lines of the file into an array
        array = []
        with open(file_name) as file:
            for item in file:
                array.append(item.strip())

        # Closes file.
        file.close()

        return array
    except:
        print("Could not find the file, please check file and try again ")

    return array


def string_replace(array):
    for i, provinces in enumerate(array):
        if provinces == "AB":
            array[i] = "Alberta"


def remove_element(array):
    array.pop(0)
    array.pop(len(array) - 1)


def count_alberta(array):
    count = 0
    for provinces in array:
        if provinces == "Alberta":
            count += 1

    print(f"Alberta appears: {count} times")


main()
