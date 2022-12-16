#!/usr/bin/env python3

import re

INPUT = "day15-input.txt"
CONSIDERED_LINE = 2000000

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


    

if __name__ == "__main__":
    with open(INPUT, "r") as f:
        sensors = []
        for line in f:
            values = input_re.match(line.strip()).group(1, 2, 3, 4)
            values = map(int, values)
            sensors.append(Sensor(*values))

    spans = []
    for s in sensors:
        span = s.covered_at_line(CONSIDERED_LINE)
        if span is not None:
            spans.append(span)
    positions = set()
    for s in spans:
        for i in range(s[0], s[1]+1):
            positions.add(i)
    # remove known beacons
    for s in sensors:
        if s.beacon_y == CONSIDERED_LINE:
            positions.discard(s.beacon_x)
    #print(sorted(positions))
    print(f"Result {len(positions)}, confirmed 4876693")

    
    
