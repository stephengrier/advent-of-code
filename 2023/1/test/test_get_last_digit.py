from solution import get_last_digit

def test_get_last_digit_returns_last_digit():
    assert get_last_digit('one4twothree9fourfive') == '9'
    assert get_last_digit('six8seven3eightnine') == '3'

def test_get_last_digit_returns_none_if_no_digits():
    assert get_last_digit('onethreenine') is None
