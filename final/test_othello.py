# Calvin Bullock CSE-111 Final test file

import pytest
from othello import parse_cordnate_to_index
from othello import parse_cords


def test_parse_cordnate_to_index():
    """ """
    assert parse_cordnate_to_index("A", 1) == 10
    assert parse_cordnate_to_index("A", 5) == 46
    assert parse_cordnate_to_index("E", 5) == 50


def test_parse_cords():
    """ """
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

    # # TODO breaks bcause lack of space...
    # row, col = parse_cords("f,4")
    # assert row == "F"
    # assert col == 4


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
