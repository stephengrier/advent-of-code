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

    # Part 1
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

    # Part 2
    locations2 = []
    seed_pairs = zip(input_data['seeds'][::2], input_data['seeds'][1::2])
    seed_ranges = [[int(x), int(x)+int(y)-1] for x, y in seed_pairs]
    for r in seed_ranges:
        ranges = [r]
        for map in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
                    'water-to-light', 'light-to-temperature',
                    'temperature-to-humidity', 'humidity-to-location']:
            mapped = []
            unmapped = ranges
            print(f"Processing next map class {map} with unmapped {unmapped}")
            while unmapped:
                print(f"unmapped contains {unmapped}")
                range = unmapped.pop()
                print(f"Processing unmapped range {range}")
                for map_range in input_data[map]:
                    dest_start = int(map_range[0])
                    source_start = int(map_range[1])
                    length = int(map_range[2])
                    source_end = int(source_start) + int(length) -1
                    dest_end = dest_start + length -1
                    range_length = range[1] - range[0]

                    # If seed range start is after end of map range or seed range end is
                    # before map start there is no match, so pass range through
                    # to next map range
                    if range[1] < source_start or range[0] > source_end:
                        print(f"Range {range} does not match map range [{source_start}, {source_end}] for {map}")
                        continue
                    # If seed range is entirely within map range map start and end values
                    elif range[0] >= source_start and range[1] <= source_end:
                        print(f"Range {range} within range {source_start} {source_end} for {map}")
                        offset = range[0] - source_start
                        range = [dest_start + offset, dest_start + range_length + offset]
                        print(f"- mapped range via {map} to {range}")
                        break
                    # If range start is less than map range start and range end is
                    # after map range end there is an overlap at both ends. Split
                    # our seed range on the intersections and push non-matching
                    # ranges onto unmapped to be processed later.
                    elif range[0] < source_start and range[1] > source_end:
                        print(f"Range {range} overlaps {source_start} {source_end} at both ends {map}")
                        unmapped.append([range[0], source_start - 1])
                        unmapped.append([source_end + 1, range[1]])
                        range = [dest_start, dest_end]
                        break
                    elif range[0] < source_start:
                        print(f"Range {range} overlaps {source_start} {source_end} at start {map}")
                        offset = source_start - range[0]
                        unmapped.append([range[0], source_start - 1])
                        range = [dest_start, dest_start + range_length - offset]
                        break
                    elif range[1] > source_end:
                        print(f"Range {range} overlaps {source_start} {source_end} at end {map}")
                        offset = range[0] - source_start
                        unmapped.append([source_end + 1, range[1]])
                        range = [dest_start + offset, dest_end]
                        break
                mapped.append(range)
            ranges = mapped
        locations2.append(min(r[0] for r in ranges))

    print(f"Part 1: lowest location number: {min(locations)}")
    print(f"Part 2: lowest location number: {min(locations2)}")


if __name__ == '__main__':
    main()
