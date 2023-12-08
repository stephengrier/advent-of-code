#!/usr/bin/env python3
"""
Solution to advent of code 2023 day 7 challenge
"""
from operator import itemgetter, attrgetter


CARDS = {
        'A': 12,
        'K': 11,
        'Q': 10,
        'J': 9,
        'T': 8,
        '9': 7,
        '8': 6,
        '7': 5,
        '6': 4,
        '5': 3,
        '4': 2,
        '3': 1,
        '2': 0
    }


def parse_input_data(file):
    input = []
    with open(file, 'r') as f:
        while line:= f.readline():
            input.append(line.split())
    return input


def get_hand_type(hand):
    chars = dict.fromkeys(CARDS.keys(), 0)
    for char in hand:
        chars[char] += 1
    values = chars.values()
    if 5 in values:
        return 6
    elif 4 in values:
        return 5
    elif 3 in values and 2 in values:
        return 4
    elif 3 in values:
        return 3
    elif sum(v == 2 for v in values) == 2:
        return 2
    elif 2 in values:
        return 1
    return 0


def get_card_score(char):
    return CARDS[char]


def main():
    input_file = 'input.txt'

    input = parse_input_data(input_file)
    print(len(input), 'lines loaded from input file')

    # Part 1
    s = sorted(input, key=lambda hand:
               (get_hand_type(hand[0]),
                get_card_score(hand[0][0]),
                get_card_score(hand[0][1]),
                get_card_score(hand[0][2]),
                get_card_score(hand[0][3]),
                get_card_score(hand[0][4])))
    total = 0
    for i, c in enumerate(s):
        total += int(c[1]) * (i+1)
    print(f"Part 1: total winnings: {total}")


if __name__ == '__main__':
    main()
