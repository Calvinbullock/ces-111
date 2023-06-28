import os
import sys


def main():
    """ """
    board_list = board_reset()

    # Runs until user quites program
    while True:
        print("Enter a cordinate pair [A, 1]: ")
        print("Type E to quit:")
        print("Type R to reset:")
        print("")
        user_input = input("> ")

        # Clears the Console
        os.system("cls||clear")

        if user_input == "R":
            board_list = board_reset()

        elif user_input == "E":
            print("Good Bye")
            sys.exit()

        else:
            print(input)
            print_board(board_list)


def parse_move():
    """
    
    """
    pass


def board_reset():
    """
    Creats board_list whitch stores the postions of the board
            and pieces.

    return
        string list: board postions
    """
    board_list = [
        " ",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "1",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "2",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "3",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "4",
        "_",
        "_",
        "_",
        "W",
        "B",
        "_",
        "_",
        "_",
        "5",
        "_",
        "_",
        "_",
        "B",
        "W",
        "_",
        "_",
        "_",
        "6",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "7",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "8",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
    ]

    return board_list

    # " ", "A", "B", "C", "D", "E", "F", "G", "H",
    # "1", "_", "_", "_", "_", "_", "_", "_", "_",
    # "2", "_", "_", "_", "_", "_", "_", "_", "_",
    # "3", "_", "_", "_", "_", "_", "_", "_", "_",
    # "4", "_", "_", "_", "W", "B", "_", "_", "_",
    # "5", "_", "_", "_", "B", "W", "_", "_", "_",
    # "6", "_", "_", "_", "_", "_", "_", "_", "_",
    # "7", "_", "_", "_", "_", "_", "_", "_", "_",
    # "8", "_", "_", "_", "_", "_", "_", "_", "_"


def print_board(list):
    """
    Takes the board list and prints out the formated
        Board.

    Paramites
        String List: of the piaces places on teh board.
    """
    for index, item in enumerate(list):
        if index % 9 == 0:
            print()
            print("-------------------------------------")
            print("|", end="")

        print(f" {item} |", end="")

    print()
    print()


main()
