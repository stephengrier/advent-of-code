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


def replace_number_words_with_digits(str):
    str = str.replace('one', 'o1e')
    str = str.replace('two', 't2o')
    str = str.replace('three', 't3e')
    str = str.replace('four', 'f4r')
    str = str.replace('five', 'f5e')
    str = str.replace('six', 's6x')
    str = str.replace('seven', 's7n')
    str = str.replace('eight', 'e8t')
    str = str.replace('nine', 'n9e')
    return str


def main():
    input_file = 'input'
    sum_of_all = 0
    sum_of_all_2 = 0
    lines = read_input_file(input_file)
    print(len(lines), 'lines in input file')

    for line in lines:
        sum_of_all += get_calibration_value_from_line(line)
        sum_of_all_2 += get_calibration_value_from_line(replace_number_words_with_digits(line))

    print(f"Sum of all calibration values is: {sum_of_all}")
    print(f"Sum of all calibration values (for part 2) is: {sum_of_all_2}")


if __name__ == '__main__':
    main()
