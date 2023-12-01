from solution import get_first_digit

def test_get_first_digit_returns_first_digit():
    assert get_first_digit('one4twothree9fourfive') == '4'
    assert get_first_digit('six8seven3eightnine') == '8'

def test_get_first_digit_returns_none_if_no_digits():
    assert get_first_digit('onethreenine') is None
