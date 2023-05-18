from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """
    test that call and return of _make_full_name looks like this
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".
    """
    assert make_full_name("", "") == "; "
    assert make_full_name("", "Time") == "Time; "
    assert make_full_name("bob", "") == "; bob"
    assert make_full_name("Angelica", "Awesome") == "Awesome; Angelica"
    assert make_full_name("T.J", "Bop") == "Bop; T.J"


def test_extract_family_name():
    """
    func that tests the call and return of extract_family_name looks like this
    extract_family_name("Brown; Sally"), it would return "Brown".
    extract_family_name("A; B"), it would return "A".
    """
    assert extract_family_name("; ") == ""
    assert extract_family_name("Time; ") == "Time"
    assert extract_family_name("; Bob") == ""
    assert extract_family_name("Awesome; Angelica") == "Awesome"
    assert extract_family_name("Bop; T.J") == "Bop"


def test_extract_given_name():
    """
    func that tests the call and return of extract_family_name looks like this
    extract_given_name("Brown; Sally"), it would return "Sally".
    extract_family_name("A; B"), it would return "B".
    """
    assert extract_given_name("; ") == ""
    assert extract_given_name("Time; ") == ""
    assert extract_given_name("; Bob") == "Bob"
    assert extract_given_name("Awesome; Angelica") == "Angelica"
    assert extract_given_name("Bop; T.J") == "T.J"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
