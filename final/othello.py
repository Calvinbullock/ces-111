# Calvin Bullock CSE-111 Final
# June 19th 2023

import os
import sys

# ======================================================== #
# TODO Check for move out of bounds.
# TODO High scores save as a dict to a file.
# TODO how to check for game over?.....
#
# ======================================================== #

# Allows me to display errors to user after clearing the console.
ERROR_MSG = ""

# TODO -- makes testing make_move() difficult might need to move to
#       main function then pass to other functions....
# Tracks whitch players turn it is:
#       0 = W, White.
#       1 = B, Black.
TURN = 0


def main():
    """
    This is the main function of an othello game. This function will take
            useer input and direct the path of the stack based on that
            user input.
    """
    global ERROR_MSG
    global TURN

    # Initial board creation and print
    board_list = board_reset()
    print_board(board_list)

    # Runs until user quites program
    while True:
        # Print notification messages
        print(ERROR_MSG)
        if TURN == 0:
            print("*White's Turn.")
        else:
            print("*Black's Turn.")

        # Print menu
        print("Enter a cordinate pair [A, 1]: ")
        print("Type E to quit:")
        print("Type R to reset:")
        print("")
        user_input = input("> ")

        # Clears the Console
        os.system("cls||clear")
        ERROR_MSG = ""

        # Main game stack
        # Parse user choice to action
        if user_input == "R":  # Reset Board
            board_list = board_reset()

        elif user_input == "E":  # Exit program
            print("Good Bye")
            sys.exit()

        else:  # Make move
            # TODO if the try catch in this func breaks this line breaks
            #       sepretly is there a better / cleaner way to catch
            #       this error?
            try:
                row, col = parse_cords(user_input)

            except TypeError:
                print("ERROR: Invalid cordanates please try again.")
                print()

            else:  # Good to go no errors
                index = parse_cordnate_to_index(row, col)
                make_move(index, board_list)
                print_board(board_list)


def make_move(move_index, board_list):
    """
    Checks if a piece is places next to a diffrent colour and has the
        same colour nth places from it on the otherside of the oponites
        colour. This does the math in the positive directions.

    Paramiters
        [index: int]              - The index that is being changed.
        [turns_letter: string]    - The letter of the curent turns user.
        [letter_opposite: string] - The opposite of the curent users letter.
        [direction: int]          - The number of indexs to move the
                                            needed direction.
        [valid: function]         - This is a lambda function that checks
                                            if the value at direction_index
                                            is equal to the letter..
        [board_list: string list] - The list of board postions.

    Returns
        True == invalid move
        False == valid move
    """
    global TURN
    global ERROR_MSG

    def change_letter(turn_letter, index_list, board_list):
        """
        This function swaps the oponites pieces with the turns pieces
                if move is valid.

        Paramiters:
            [turn_letter: ] - The letter that the values will be set to.
            [index_list: ]  - A list of indexs that need to be switched.
            [board_list: ]  - The list of all pieces on the board.

        """
        for index in index_list:
            board_list[index] = turn_letter

    def in_line_check_pos(
        index, turn_letter, opposite_letter, direction, valid, board_list
    ):
        """
        Checks if a piece is places next to a diffrent colour and has the
            same colour nth places from it on the otherside of the oponites
            colour. This does the math in the positive directions.

        Paramiters
            [turns_letter: string]    - The letter of the curent turns user.
            [letter_opposite: string] - The opposite of the curent users letter.
            [index: int]           - The index that is being changed.
            [board_list: string list] - The list of board postions.

        Returns
            True == invalid move
            False == valid move
        """
        index_list = []
        at_least_one_oposite_letter = False
        direction_index = index + direction

        while (
            direction_index > 0
            and direction_index < 80
            and not valid(direction_index, "_")
        ):
            # All the if statments check if the letter at direction_index
            #       is equal to opposite letter if yes move the direction.
            if valid(direction_index, opposite_letter):
                at_least_one_oposite_letter = True
                index_list.append(direction_index)
                direction_index += direction

            elif valid(direction_index, turn_letter) and at_least_one_oposite_letter:
                change_letter(turn_letter, index_list, board_list)
                return True

            elif direction_index < 0:  # No piece in this direction
                return False

            else:
                direction_index += direction

        return False

    def in_line_check_neg(
        index, turn_letter, opposite_letter, direction, valid, board_list
    ):
        """
        Checks if a piece is places next to a diffrent colour and has the
            same colour nth places from it on the otherside of the oponites
            colour. This does the math in the positive directions.

        Paramiters
            [index: int]              - The index that is being changed.
            [turns_letter: string]    - The letter of the curent turns user.
            [letter_opposite: string] - The opposite of the curent users letter.
            [direction: int]          - The number of indexs to move the
                                                needed direction.
            [valid: function]         - This is a lambda function that checks
                                                if the value at direction_index
                                                is equal to the letter..
            [board_list: string list] - The list of board postions.

        Returns
            True == invalid move
            False == valid move
        """
        index_list = []
        at_least_one_oposite_letter = False
        direction_index = index - direction

        while (
            direction_index > 0
            and direction_index < 80
            and not valid(direction_index, "_")
        ):
            # All the if statments check if the letter at direction_index
            #       is equal to opposite letter if yes move the direction.
            if valid(direction_index, opposite_letter):
                at_least_one_oposite_letter = True
                index_list.append(direction_index)
                direction_index -= direction

            elif valid(direction_index, turn_letter) and at_least_one_oposite_letter:
                change_letter(turn_letter, index_list, board_list)
                return True

            elif direction_index < 0:  # No piece in this direction
                return False

            else:
                direction_index -= direction

        return False

    # Directional math compass
    #   -9        N
    # -1  +1    W   E
    #   +9        S

    # south_index = move_index + 1
    # east_index = move_index + 9
    # south_west_index = move_index + 8
    # south_east_index = move_index + 10

    # north_index = move_index - 1
    # west_index = move_index - 9
    # north_east_index = move_index - 8
    # north_west_index = move_index - 10

    # LAMBDA checks if the value at direction_index is
    #       equal to the letter.
    valid = lambda index, letter: board_list[index] == letter

    # Sets turn and opposite letters
    if TURN == 0:
        turn_letter = "W"
        opposite_letter = "B"

    else:
        turn_letter = "B"
        opposite_letter = "W"

    # Check all directions return True if move is valid, also change all
    #       letters to this players
    south_bool = in_line_check_pos(
        move_index, turn_letter, opposite_letter, 9, valid, board_list
    )
    east_bool = in_line_check_pos(
        move_index, turn_letter, opposite_letter, 1, valid, board_list
    )
    SW_bool = in_line_check_pos(
        move_index, turn_letter, opposite_letter, 8, valid, board_list
    )
    SE_bool = in_line_check_pos(
        move_index, turn_letter, opposite_letter, 10, valid, board_list
    )

    north_bool = in_line_check_neg(
        move_index, turn_letter, opposite_letter, 9, valid, board_list
    )
    west_bool = in_line_check_neg(
        move_index, turn_letter, opposite_letter, 1, valid, board_list
    )
    NE_bool = in_line_check_neg(
        move_index, turn_letter, opposite_letter, 8, valid, board_list
    )
    NW_bool = in_line_check_neg(
        move_index, turn_letter, opposite_letter, 10, valid, board_list
    )

    # Check if square is ocupied
    if board_list[move_index] == "W" or board_list[move_index] == "B":
        print("Already a piece there, try again.")
        return 1  # error

    elif TURN == 0:  # Make white move
        if (
            south_bool
            or east_bool
            or SW_bool
            or SE_bool
            or north_bool
            or west_bool
            or NE_bool
            or NW_bool
        ):
            board_list[move_index] = "W"
            TURN = 1
            return 0

    elif TURN == 1:  # Make black move
        if (
            south_bool
            or east_bool
            or SW_bool
            or SE_bool
            or north_bool
            or west_bool
            or NE_bool
            or NW_bool
        ):
            board_list[move_index] = "B"
            TURN = 0
            return 0

    ERROR_MSG = "Invalid move please place piece next to opposing player"
    return 1


def parse_cords(cords):
    """
    Takes a cordinate pair [letter, number] and translates it into
        a list index.

    Paramiters
        cords:String - a string with a letter and number seperated by
                        a comma and space.

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

        print(f" {item} |", end="")

    print()
    print("-------------------------------------")

    print()
    print()


if __name__ == "__main__":
    main()


# TODO At least use each of these might be more
# 05 - testing fuc
# 07 - Lists
# 08* - Dictinaries
# 09* - text files
# 10 - exception handeling
# 11 - lamda functions / functions in functions
# 12 - Objects
