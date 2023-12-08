import pytest
from solution import get_hand_type


def test_get_hand_type():
    assert get_hand_type('QQQQQ') == 6
    assert get_hand_type('22K22') == 5
    assert get_hand_type('72772') == 4
    assert get_hand_type('42555') == 3
    assert get_hand_type('8Q278') == 1
    assert get_hand_type('78654') == 0
