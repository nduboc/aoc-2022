#!/usr/bin/env python3

def find_marker(line, ms):
    """
    >>> find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
    7
    >>> find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
    5
    >>> find_marker("nppdvjthqldpwncqszvftbrmjlhg", 4)
    6
    >>> find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)
    10
    >>> find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)
    11
    >>> find_marker("abcdd", 4)
    4
    >>> find_marker("ujjaabcd", 4)
    8
    >>> find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
    19
    >>> find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)
    29
    """
    for i in range(ms, len(line)+1):
        if len(set(line[i-ms:i])) == ms:
            return i
    return None



input_file = "day6-input.txt"
line = open(input_file).readline()
result = find_marker(line, 14)
print(f"Result is {result}, confirmed 3613")
