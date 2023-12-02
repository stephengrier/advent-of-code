import pytest
from solution import parse_game_data


def test_parse_game_data():
    line1 = {
        'input': 'Game 1: 1 red, 10 blue, 5 green; 11 blue, 6 green; 6 green; 1 green, 1 red, 12 blue; 3 blue; 3 blue, 4 green, 1 red',
        'assert': {
            'id': '1',
            'red': 1,
            'green': 6,
            'blue': 12
        }
    }

    assert parse_game_data(line1['input']) == line1['assert']
