import pytest
from solution import get_calibration_value_from_line


def test_get_calibration_value_from_line():
    assert get_calibration_value_from_line('one4twothree9fourfive') == 49
    assert get_calibration_value_from_line('8seven3eightnine') == 83


def test_get_calibration_value_from_line_with_only_one_digit():
    assert get_calibration_value_from_line('onethree6nine') == 66


@pytest.mark.xfail(reason="The code doesn't currently handle this case")
def test_get_calibration_value_from_line_with_no_digits():
    assert get_calibration_value_from_line('oneergtdbthreenine') == 0
