#!/usr/bin/env python3

# run with "python3 -m doctest day6-puzzle1.py"

def find_marker(line):
    """
    >>> find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    7
    >>> find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz")
    5
    >>> find_marker("nppdvjthqldpwncqszvftbrmjlhg")
    6
    >>> find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    10
    >>> find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    11
    >>> find_marker("abcdd")
    4
    >>> find_marker("ujjaabcd")
    8
    """
    for i in range(4, len(line)+1):
        if len(set(line[i-4:i])) == 4:
            return i
    return None


input_file = "day6-input.txt"
line = open(input_file).readline()
result = find_marker(line)
print(f"Result is {result}, confirmed 1640")
