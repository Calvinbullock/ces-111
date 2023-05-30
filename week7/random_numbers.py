import random


def main():
    """
    """
    numbers = [16.2, 75.1, 52.3]

    print_list(numbers)
    append_random_numbers(numbers,2)
    print_list(numbers)


def print_list(list):
    """
    Prints out a list's indexs

    paramiters
    list: any tye of list
    """
    for index in list:
        print(index)


def append_random_numbers(list, n_times=1):
    """
    """

    # This will repeat n_times
    for index in range(n_times):
        # generate a random number then add it to list
        rand_num = random.uniform(0, 100)
        list.append(rand_num)


if __name__ == "__main__":
    main()
