# Calvin Bullock CSE-111 Final

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


def parse_move(cords):
    """
    Takes a cordinate pair [letter, number] and translates it into
        a list index.

    Paramiters
        cords:String - a string with a letter and number seperated by 
                        a comma and space

    Return
        a number and a letter
    """
    cord_array = cords.split(", ")
    row = cord_array[0]
    col = cord_array[1]

    return row, col


def parse_cordnate_to_index(row, col):
    """
    This function takes the column as a number and the row as a leter then
        parses that info into the index for the array that holds the pieace
        postions.

    Paramiters
        row: single char string
        col: int

    Return
        list index at the cordenates the user input.

    """
    # Parse the lette to eqivalent number
    match row:
        case "A":
            row = 0
        case "B":
            row = 1
        case "C":
            row = 2
        case "D":
            row = 3
        case "E":
            row = 4
        case "F":
            row = 5
        case "G":
            row = 6
        case "H":
            row = 7

    return row + col * 10 - col + 1

    # _ | _A | _B | _C | _D | _E | _F | _G | _H |
    # 1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
    # 2 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
    # 3 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
    # 4 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 |
    # 5 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 |
    # 6 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 |
    # 7 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 |
    # 8 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 |


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

        print(f" {item} |", end="")  # -- DEBUG
        # print(f" {index} |", end="")

    print()
    print()


if __name__ == "__main__":
    main()
