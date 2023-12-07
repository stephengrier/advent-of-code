#!/usr/bin/env python3
"""
Solution to advent of code 2023 day 6 challenge
"""
import math


def parse_input_data(file):
    input_data = {}
    with open(file, 'r') as f:
        while line:= f.readline():
            item, _data = line.split(':')
            input_data[item] = [int(x) for x in _data.split()]
    return input_data


def calculate_distance_sailed_by_time(hold_ms, max_ms):
    # Boat's speed increases by 1mm/ms for every hold_ms milliseconds.
    remaining_ms = max_ms - hold_ms
    speed_msps = hold_ms
    return speed_msps * remaining_ms


def calculate_race_distances(max_ms, record):
    wins = []
    for h in range(max_ms):
        millimeters_travelled = calculate_distance_sailed_by_time(h, max_ms)
        if millimeters_travelled > record:
            wins.append(h)
    return wins


def main():
    input_file = 'input.txt'

    input_data = parse_input_data(input_file)
    print(len(input_data), 'lines loaded from input file')

    # Part 1
    ways_to_win_per_race = []
    for i, t in enumerate(input_data['Time']):
        ways_to_win_per_race.append(len(calculate_race_distances(t, input_data['Distance'][i])))

    # Part 2
    time = int(''.join([str(x) for x in input_data['Time']]))
    distance = int(''.join([str(x) for x in input_data['Distance']]))
    w = calculate_race_distances(time, distance)

    print(f"Part 1: product of ways to win is {math.prod(ways_to_win_per_race)}")
    print(f"Part 2: {len(w)} ways to win")


if __name__ == '__main__':
    main()
