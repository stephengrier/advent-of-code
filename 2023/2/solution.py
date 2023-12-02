#!/usr/bin/env python3
"""
Solution to advent of code 2023 day 2 task
"""


GAME_MIN_NUMBERS = {
        'red': 12,
        'green': 13,
        'blue': 14
    }


# Game 1: 1 red, 10 blue, 5 green; 11 blue, 6 green; 6 green; 1 green, 1 red, 12 blue; 3 blue; 3 blue, 4 green, 1 red
def load_game_data(file):
    all_games_data = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            all_games_data.append(parse_game_data(line))
            line = f.readline()

    return all_games_data


def parse_game_data(line):
    game_data = {}

    # First, split game ID from cube data on colon
    game_id, game_data_raw = line.split(':', 1)

    # Lose the 'Game ' from the game id string
    _, game_data['id'] = game_id.split()

    # Next, split game data into instances on semicolon
    instances = game_data_raw.split(';')

    # For each instance, get the number of each colour revealed
    # If greater than the number already seen during this game, record it
    for instance in instances:
        # split colours on comma
        cube_data = instance.split(',')
        for colour in cube_data:
            number, colour = colour.split()
            if colour not in game_data or int(number) > game_data[colour]:
                game_data[colour] = int(number)

    return game_data


def main():
    input_file = 'input'
    sum_of_ids = 0
    sum_of_powers = 0

    all_games_data = load_game_data(input_file)
    print(len(all_games_data), 'lines loaded from input file')

    # Loop over each game and work out which ones met the minimum numbers
    for game in all_games_data:
        if (game.get('red', 0) <= GAME_MIN_NUMBERS['red'] and
            game.get('green', 0) <= GAME_MIN_NUMBERS['green'] and
            game.get('blue', 0) <= GAME_MIN_NUMBERS['blue']):
            sum_of_ids += int(game['id'])
        # For part 2, multiply the min numbers of each colour to get the "power"
        sum_of_powers += game.get('red', 0) * game.get('green', 0) * game.get('blue', 0)

    print(f"Sum of all possible game IDs is: {sum_of_ids}")
    print(f"Sum of all powers is: {sum_of_powers}")


if __name__ == '__main__':
    main()
