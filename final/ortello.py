def main():
    exit = True
    board_list = board_reset()

    while exit:
        # print("Enter a cordinate pair [A, 1]: ")
        # print("Type Exit to quit:")
        # print("Type R to reset:")
        # print("")

        user_input = input("> ")

        print_board(board_list)


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
    for index, item in enumerate(list):
        if index % 9 == 0:
            print()
        
        # elif :
        #     pass

        # print(f"{item}", end="")
        print(f",{index}", end="")

    print()


main()
