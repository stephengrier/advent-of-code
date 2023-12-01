#!/usr/bin/env python3
"""
Solution to advent of code 2023 day 1 task
"""
import os


def read_input_file(file):
    lines = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()

    return lines


def get_calibration_value_from_line(line):
    return int("".join([get_first_digit(line), get_last_digit(line)]))


def get_first_digit(str):
    for char in str:
        if char.isdigit():
            return char
    return None


def get_last_digit(str):
    for char in str[::-1]:
        if char.isdigit():
            return char
    return None


def main():
    input_file = 'input'
    sum_of_all = 0
    lines = read_input_file(input_file)
    print(len(lines), 'lines in input file')

    for line in lines:
        print(line,": ",get_calibration_value_from_line(line))
        sum_of_all += get_calibration_value_from_line(line)

    print(f"Sum of all calibration values is: {sum_of_all}")


if __name__ == '__main__':
    main()
