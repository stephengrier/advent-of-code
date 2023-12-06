#!/usr/bin/env python3
"""
Solution to advent of code 2023 day 5 challenge
"""
import re


def parse_input_data(file):
    input_data = {}
    with open(file, 'r') as f:
        while line:= f.readline():
            if re.search('^seeds:', line):
                _, seeds = line.split(':')
                input_data['seeds'] = seeds.split()
            elif x := re.search('^([a-z-]+)', line):
                input_data[x.group()] = []
                line = f.readline()
                while re.search('^\d', line):
                    input_data[x.group()].append(line.split())
                    line = f.readline()
    return input_data


def scan_range(source, dest_start, source_start, length):
    source_end = source_start + length - 1

    if source_start <= source <= source_end:
        offset = source - source_start
        return dest_start + offset
    return None


def scan_ranges(source, ranges):
    for range in ranges:
        if res := scan_range(source, int(range[0]), int(range[1]), int(range[2])):
            return res
    # If source is not mapped through any of the ranges it is the same as the destination
    return source


def main():
    input_file = 'input.txt'

    input_data = parse_input_data(input_file)
    print(len(input_data), 'lines loaded from input file')

    locations = []
    for seed in input_data['seeds']:
        print(f"Mapping seed {seed}")
        val = int(seed)
        for map in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
                    'water-to-light', 'light-to-temperature',
                    'temperature-to-humidity', 'humidity-to-location']:
            val = scan_ranges(val, input_data[map])
            print(f"- mapped via {map} to {val}")
        locations.append(val)

    print(f"Part 1: lowest location number: {min(locations)}")

    # Part 2
    locations2 = 9999999999999999
    for i in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]:
        start = int(input_data['seeds'][i])
        length = int(input_data['seeds'][i+1])
        for j in range(length):
            seed = start + j
            print(f"Mapping seed {seed}")
            val = int(seed)
            for map in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
                        'water-to-light', 'light-to-temperature',
                        'temperature-to-humidity', 'humidity-to-location']:
                val = scan_ranges(val, input_data[map])
                print(f"- mapped via {map} to {val}")
            if val < locations2: locations2 = val

    print(f"Part 2: lowest location number: {locations2}")



if __name__ == '__main__':
    main()
