#!/usr/bin/env python3

import re

# INPUT = "day15-sample.txt"
# MAX_COORD = 20

INPUT = "day15-input.txt"
MAX_COORD = 4000000

input_re = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

def test_re():
    """
    >>> input_re.match("Sensor at x=2, y=18: closest beacon is at x=-2, y=15").group(1, 2, 3, 4)
    ('2', '18', '-2', '15')
    >>> input_re.match("Sensor at x=2, y=18: closest beacon is at x=a, y=15")
    """
    pass

class Sensor:
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.beacon_x = bx
        self.beacon_y = by
        self.radius = abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)


    def __str__(self):
        return f"Sensor at {self.x}, {self.y}, closest beacon at {self.beacon_x}, {self.beacon_y}, radius {self.radius}"

    def covered_at_line(self, y):
        diff_y = abs(self.y - y)
        if diff_y > self.radius:
            return None
        on_line_width = self.radius - diff_y
        return (self.x - on_line_width, self.x + on_line_width)


def cut_span(spans, s):
    """
    >>> cut_span([(5, 10), (20, 24)], (0, 2))
    [(5, 10), (20, 24)]
    >>> cut_span([(5, 10), (20, 24)], (12, 14))
    [(5, 10), (20, 24)]
    >>> cut_span([(5, 10), (20, 24)], (25, 30))
    [(5, 10), (20, 24)]
    >>> cut_span([(0, 10), (20, 24)], (5, 15))
    [(0, 4), (20, 24)]
    >>> cut_span([(0, 10), (12, 24)], (5, 15))
    [(0, 4), (16, 24)]
    >>> cut_span([(0, 10), (20, 24)], (16, 22))
    [(0, 10), (23, 24)]
    >>> cut_span([(0, 10), (20, 24), (50, 100)], (15, 90))
    [(0, 10), (91, 100)]
    >>> cut_span([(0, 10), (12, 24)], (10, 10))
    [(0, 9), (12, 24)]
    >>> cut_span([(0, 10), (12, 24)], (-1, 25))
    []
    """
    start = 0
    while start < len(spans) and spans[start][1] < s[0] :
        start+=1
    if start == len(spans):
        return spans
    if s[1] < spans[start][0]:
        return spans
    if spans[start][0] < s[0]:
        new_span = (spans[start][0], s[0]-1)
        spans.insert(start, new_span)
        start += 1
    if s[1] < spans[start][1] :
        spans[start] = (s[1]+1, spans[start][1])
        return spans
    elif s[1] == spans[start][1]:
        del spans[start]
        return spans
    else:
        new_s_start = spans[start][1] + 1
        del spans[start]
        return cut_span(spans, (new_s_start, s[1]))


if __name__ == "__main__":
    with open(INPUT, "r") as f:
        sensors = []
        for line in f:
            values = input_re.match(line.strip()).group(1, 2, 3, 4)
            values = map(int, values)
            sensors.append(Sensor(*values))

    
    found = None
    
    for y in range(MAX_COORD+1):
        if found:
            break
        
        if y % 100000 == 0:
            print(y)
        spans = []
        for s in sensors:
            span = s.covered_at_line(y)
            if span is not None:
                spans.append(span)
        #print(f"{y}, {len(spans)}")

        line = [(0, MAX_COORD)]
        for s in spans:
            line = cut_span(line, s)

        if len(line) > 1:
            raise Exception(f"More than 1 remaining spot on line {y}")
        if len(line) == 1:
            if line[0][1] != line[0][0]:
                raise Exception(f"Span size larger than 1 on line {y}")
            found = (line[0][0], y)

    if not found:
        print("No result ?!")
    else:
        print(f"Found at {found}, result is {found[0]*4000000 + found[1]}, confirmed 11645454855041")

    
    
