# Calvin Bullock Final

import pytest
from othello import parse_cordnate_to_index 

def test_parse_cordnate_to_index():
    assert parse_cordnate_to_index("A", 1) == 10
    assert parse_cordnate_to_index("A", 5) == 46
    assert parse_cordnate_to_index("E", 5) == 50
    assert parse_cordnate_to_index("E", 5) == 50


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
