from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """
    test that call and return of _make_full_name looks like this
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".
    """
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("51 S Center St, timmy, ID 83460") == "timmy"
    assert extract_city("5 S Center St, idaho falls, ID 83460") == "idaho falls"
    assert extract_city("5.5 S Center St, littlecreek, ID 83460") == "littlecreek"

def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("51 S Center St, timmy, Iw 83460") == "Iw"
    assert extract_state("5 S Center St, idaho falls, w 83460") == "w"
    assert extract_state("5.5 S Center St, littlecreek, I.D 83460") == "I.D"


def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "ID 83460"
    assert extract_zipcode("51 S Center St, timmy, ID 830") == "ID 830"
    assert extract_zipcode("5 S Center St, idaho falls, IW 83460") == "IW 83460"
    assert extract_zipcode("5.5 S Center St, littlecreek, IW83460") == "IW83460"
    assert extract_zipcode("5.5 S Center St, littlecreek, IW834") == "IW834"
    assert extract_zipcode("5.5 S Center St, littlecreek, IW.834") == "IW.834"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])


# number street, city, state zipcode
# 525 S Center St, Rexburg, ID 83460