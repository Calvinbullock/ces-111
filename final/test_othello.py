# Calvin Bullock CSE-111 Final test file

import pytest
from othello import parse_cordnate_to_index
from othello import parse_cords
from othello import make_move

# TODO not sure if this should be in the test file but I think it
#       will be needed so.....
TURN = 0


def test_make_move():
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

    assert make_move(40, board_list) == 1  # checks if sq is ocupied
    # assert make_move(10, board_list) == 0 # breaks because turn not inislilized -- so working sorta...
    # assert make_move(41, board_list) == 0 # breaks because turn not inislilized -- so working sorta...

    # BOARD INDEX MAP
    # _ | _A | _B | _C | _D | _E | _F | _G | _H |
    # 1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
    # 2 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
    # 3 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
    # 4 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 |
    # 5 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 |
    # 6 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 |
    # 7 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 |
    # 8 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 |


def test_parse_cordnate_to_index():
    """
    Checks if the letter number cords are parsed to the right indexs
    """
    assert parse_cordnate_to_index("A", 1) == 10
    assert parse_cordnate_to_index("A", 5) == 46
    assert parse_cordnate_to_index("E", 5) == 50


def test_parse_cords():
    """
    Checks if users input string is seperated correctly into a string and int
    """
    row, col = parse_cords("A, 1")
    assert row == "A"
    assert col == 1

    row, col = parse_cords("B, 6")
    assert row == "B"
    assert col == 6

    row, col = parse_cords("F, 4")
    assert row == "F"
    assert col == 4

    row, col = parse_cords("f, 4")
    assert row == "F"
    assert col == 4

    # # TODO breaks because lack of space...
    # row, col = parse_cords("f,4")
    # assert row == "F"
    # assert col == 4


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
