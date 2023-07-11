# Calvin Bullock CSE-111 Final

import os
import sys

# Allows me to display errors to user after clearing the console.
ERROR_MSG = ""

# Tracks whitch players turn it is:
#       0 = W, White.
#       1 = B, Black.
# TODO -- makes testing difficult might need to move to main function then pass to other functions
TURN = 0


def main():
    """
    TODO ....... Exsplane the mian!!!!
    TODO ....... Exsplane the mian!!!!
    TODO ....... Exsplane the mian!!!!
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
        # os.system("cls||clear")
        ERROR_MSG = ""

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

            else:
                index = parse_cordnate_to_index(row, col)
                make_move(index, board_list)
                print_board(board_list)


def make_move(move_index, board_list):
    """
    This function checks whose turn it is then places the piece in the
        user specified index.

    Paramiters
        [move_index: int] The index that the user wants to place a piece.
        [board_list: string list] The list of pieces and there postions.
    """
    # Check if square is ocupied
    if board_list[move_index] == "W" or board_list[move_index] == "B":
        print("Already a piece there, try again.")
        return 1  # error

    def in_line_check(turns_letter, letter_opposite, orig_index, board_list):
        """
        Checks if a piece is places next to a diffrent colour and has the
            same colour nth places from it on the otherside of the opposite
            colour.

        Paramiters
            [turns_letter: string]    - The letter of the curent turns user.
            [letter_opposite: string] - The opposite of the curent users letter.
            [index: int]           - The index that is being changed.
            [board_list: string list] - The list of board postions.

        Returns
            True == invalid move
            False == valid move
        """
        # Directional math compass
        #   -9        N
        # -1  +1    W   E
        #   +9        S

        north_index = index - 1
        east_index = index + 9
        south_index = index + 1
        west_index = index - 9
        north_east_index = index - 8
        south_east_index = index + 10
        south_west_index = index + 8
        north_west_index = index - 10

        # Triggers if there is at least one opposite letter after the given index
        #       exits if out of board bounds.
        while board_list[index] == opposite_letter or index < 0 or index > 80:
            print(f"L137 {index}")
            # assert index < 0 or index > 80  # BUG --------------------- BUG

            # Lambda checks if the value at direction_index is
            #       equal to the letter.
            valid = (
                lambda direction_index, letter: board_list[direction_index] == letter
            )

            if valid(north_index, opposite_letter):
                north_index -= 1

            if valid(east_index, opposite_letter):
                east_index += 9

            if valid(south_index, opposite_letter):
                south_index += 1

            if valid(west_index, opposite_letter):
                west_index -= 9

            if valid(north_east_index, opposite_letter):
                north_east_index -= 8

            if valid(south_east_index, opposite_letter):
                south_east_index += 10

            if valid(south_west_index, opposite_letter):
                south_west_index += 8

            if valid(north_west_index, opposite_letter):
                north_west_index -= 10

            # TODO -- this is what I need to go to.
            # TODO -- this is what I need to go to.
            # if valid(op_letter)
            #       add to direction
            #
            # elif valid(turn_letter):
            #       revers direction and ...
            #       filter() for oposite letter and change to turns_letter

            # Check if the opposite letter is at the end of the path.
            if board_list[index] == turns_letter:
                print("L162")  # DEBUG
                return True

        print("L165")  # DEBUG
        return False

        # BUG Working here ---- BUG
        # BUG Working here ---- BUG
        #       The if else statment above is triggering wrong.
        #       To test this bug enter cords F, 4.

    # Check if square is ocupied
    if board_list[move_index] == "W" or board_list[move_index] == "B":
        print("Already a piece there, try again.")
        return 1  # error

    elif TURN == 0:  # make white move
        if in_line_check("W", "B", move_index, board_list):
            board_list[move_index] = "W"
            TURN = 1
            return 0

    else:  # Make black move
        if in_line_check("B", "W", move_index, board_list):
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

        print(f" {item} |", end="")  # -- DEBUG
        # print(f" {index} |", end="")

    print()
    print("-------------------------------------")

    print()
    print()


if __name__ == "__main__":
    main()


# TODO At least use each of these might be more
# - testing fuc
# - Lists
# - Dictinaries
# - text files
# - exception handeling
# - Objects
# - lamda functions / functions in functions
