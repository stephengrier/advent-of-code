#!/usr/bin/env python3
"""
Solution to advent of code 2023 day 4 task
"""


def parse_input_data(file):
    all_cards = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            all_cards.append(parse_card_data(line))
            line = f.readline()

    return all_cards

def parse_card_data(line):
    card = {}

    # First, split line in colon char to get the card number
    card_number_str, data = line.rstrip().split(':', 1)
    _, card['card_number'] = card_number_str.split()

    # Next, split line on pipe character to separate winning from have numbers
    winning_numbers_str, have_numbers_str = data.rstrip().split('|', 1)

    card['winning_numbers'] = winning_numbers_str.split()
    card['have_numbers'] = have_numbers_str.split()

    return card


def main():
    input_file = 'input.txt'
    total_points = 0

    all_cards = parse_input_data(input_file)
    print(len(all_cards), 'lines loaded from input file')

    card_counts = []
    for i in range(len(all_cards)):
        card_counts.append(1)

    # Loop over each card and work out how many numbers are winning numbers
    for i, card in enumerate(all_cards):
        number_of_winning_numbers = 0
        for number in card['have_numbers']:
            if number in card['winning_numbers']:
                number_of_winning_numbers += 1

        card_score = 1*2**(number_of_winning_numbers-1) if number_of_winning_numbers > 0 else 0
        total_points += card_score

        # Part 2
        # For each card won by this card, increment its count by the count of
        # the current card (because that card would be won by each instance of
        # the current card)
        for j in range(number_of_winning_numbers):
            card_counts[i+j+1] += card_counts[i]

    print(f"Part 1: the total points from all cards is: {total_points}")
    print(f"Part 2: there are {sum(card_counts)} cards")


if __name__ == '__main__':
    main()
