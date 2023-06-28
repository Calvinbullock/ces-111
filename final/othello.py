# Calvin Bullock CSE-111 Final

import os
import sys

# Allows me to display errors after the clear console call
ERROR_MSG = ""
# Tracks whitch players turn it is 0 = W 1 = B.
TURN = 0


def main():
    """ """
    board_list = board_reset()

    # Runs until user quites program
    while True:
        # Print menu
        print("Enter a cordinate pair [A, 1]: ")
        print("Type E to quit:")
        print("Type R to reset:")
        print("")
        user_input = input("> ")

        # Clears the Console
        os.system("cls||clear")
        ERROR_MSG = ""

        # Parse user choice to action
        if user_input == "R":  # Reset Board
            board_list = board_reset()

        elif user_input == "E":  # Exit program
            print("Good Bye")
            sys.exit()

        else:  # Make move
            try:
                # TODO if the try catch in this func breaks this line breaks
                #       sepretly is there a better / cleaner way to catch
                #       this error?
                row, col = parse_cords(user_input)

            except TypeError:
                print("ERROR: Invalid cordanates please try again.")
                print()

            else:
                parse_cordnate_to_index(row, col)

                print(ERROR_MSG)
                print_board(board_list)


def make_move(move_index, board_list):
    """
    TODO......... DEscription
    """
    if TURN == 0:
        board_list[move_index] = "W"
        TURN = 1

    else:
        board_list[move_index] = "B"
        TURN = 0
    
    # TODO Check if find pieces in the end of each line and set the pieces
    #   main othello rules 


def check_if_square_ocupied(index):
    """
    This function will check if there is apiece already at the index given by
            the user.
        
    Paramiters
        [index: int] The index that needs to be checked
    
    Return
        True or False
    """
    pass


def parse_cords(cords):
    """
    Takes a cordinate pair [letter, number] and translates it into
        a list index.

    Paramiters
        cords:String - a string with a letter and number seperated by
                        a comma and space

    Return
        a number and a letter
    """
    cords = cords.upper()

    try:
        cord_array = cords.split(", ")
        row = cord_array[0]
        col = int(cord_array[1])

        return row, col

    except IndexError:
        pass
        # TODO better way to catch this error?
        # invalided corwardinets will casue an error here and another in the
        #       main function. If I don't catch it here the program crashes,
        #       but the error message is printed in main.


def parse_cordnate_to_index(row, col):
    """
    This function takes the column as a number and the row as a leter then
        parses that info into the index for the array that holds the pieces
        postions.

    Paramiters
        row: single char string
        col: int

    Return
        list index at the cordenates the user input.

    """
    assert row.upper() == row

    # Parse the letter to eqivalent number
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
        String List: of the pieces places on the board.
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
