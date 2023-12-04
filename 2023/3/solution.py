#!/usr/bin/env python3
"""
Solution to advent of code 2023 day 3 task
"""


def parse_input_file(file):
    rows = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            rows.append(parse_schematic_row(line))
            line = f.readline()

    return rows


def parse_schematic_row(line):
    schematic_row = []

    # Loop over each character in the line...
    i = 0
    while i < len(line):
        char = line[i]
        if char == '.':
            # Period char is nothing so add None to our array
            schematic_row.append(None)
            i += 1
        elif char.isdigit():
            # Scan forward to get the whole number
            number = char
            j = i+1
            while line[j].isdigit():
                number += line[j]
                j += 1
            # We now know the number, set it for each column containing one of
            # the digits
            for _ in range(len(number)):
                schematic_row.append(int(number))
            # Increment i to the end of the number as we read all chars above
            i += len(number)
        elif char == '\n':
            # Just skip newline
            i += 1
        else:
            # Anything else must be a symbol
            schematic_row.append(char)
            i += 1

    return schematic_row


def main():
    input_file = 'input'
    sum_of_part_numbers = 0
    sum_of_gear_ratios = 0

    rows = parse_input_file(input_file)
    print(len(rows), 'lines loaded from input file')

    for r in range(len(rows)):
        for c in range(len(rows[r])):
            # If entry is a string it's a symbol...
            if type(rows[r][c]) == str:
                print(f"Found symbol {rows[r][c]}")
                adjacent_numbers = []
                # Check if the position before it was a number
                if type(rows[r][c-1]) == int:
                    print(f"Found number before it {rows[r][c-1]}")
                    adjacent_numbers.append(rows[r][c-1])
                # Check if the position after it is a number
                if type(rows[r][c+1]) == int:
                    print(f"Found number after it {rows[r][c+1]}")
                    adjacent_numbers.append(rows[r][c+1])
                # Check if the row above to the left is a number
                if type(rows[r-1][c-1]) == int:
                    print(f"Found number above it to the left {rows[r-1][c-1]}")
                    adjacent_numbers.append(rows[r-1][c-1])
                # Check if row above, position directly above is a numner
                # but not the same number as the position before it as we've
                # already counted that
                if (type(rows[r-1][c]) == int and
                    rows[r-1][c] != rows[r-1][c-1]):
                    print(f"Found number directly above it {rows[r-1][c]}")
                    adjacent_numbers.append(rows[r-1][c])
                # Check if row above, position to the right is a number
                # but not the same number as the position before it as we've
                # already counted that
                if (type(rows[r-1][c+1]) == int and
                    rows[r-1][c+1] != rows[r-1][c]):
                    print(f"Found number above it to the right {rows[r-1][c+1]}")
                    adjacent_numbers.append(rows[r-1][c+1])

                # Check if the row below to the left is a number
                if type(rows[r+1][c-1]) == int:
                    print(f"Found number below it to the left {rows[r+1][c-1]}")
                    adjacent_numbers.append(rows[r+1][c-1])
                # Check if row above, position directly below is a numner
                # but not the same number as the position before it as we've
                # already counted that
                if (type(rows[r+1][c]) == int and
                    rows[r+1][c] != rows[r+1][c-1]):
                    print(f"Found number directly below it {rows[r+1][c]}")
                    adjacent_numbers.append(rows[r+1][c])
                # Check if row below, position to the right is a number
                # but not the same number as the position before it as we've
                # already counted that
                if (type(rows[r+1][c+1]) == int and
                    rows[r+1][c+1] != rows[r+1][c]):
                    print(f"Found number below it to the right {rows[r+1][c+1]}")
                    adjacent_numbers.append(rows[r+1][c+1])

                # All all the adjacent numbers we've found to the total
                for n in adjacent_numbers:
                    sum_of_part_numbers += n

                # If this is a '*' char and has two adjacent numbers it is a
                # gear. Multiply the numbers to get the gear ratio and add it
                # to the total gear ratio.
                if rows[r][c] == '*' and len(adjacent_numbers) == 2:
                    sum_of_gear_ratios += (adjacent_numbers[0]*adjacent_numbers[1])

    print(f"Sum of all part numbers is: {sum_of_part_numbers}")
    print(f"Sum of all gear ratios is: {sum_of_gear_ratios}")


if __name__ == '__main__':
    main()
