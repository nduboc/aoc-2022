#!/usr/bin/env python3

import sys


INPUT = "day14-input.txt"

def parse_line(line):
    path = []
    tokens = line.split()
    for i in range(0, len(tokens), 2):
        x, y = (int(i) for i in tokens[i].split(","))
        path.append((x, y))
    return path, min(p[0] for p in path), max(p[0] for p in path), min(p[1] for p in path), max(p[1] for p in path)


AIR = "."
ROCK = "#"
SAND = "o"

def iterpath(path):
    """
    >>> list(iterpath([(498, 4), (498, 6), (496, 6)]))
    [(498, 4), (498, 5), (498, 6), (497, 6), (496, 6)]
    >>> list(iterpath([(500, 10), (504, 10), (504, 9)]))
    [(500, 10), (501, 10), (502, 10), (503, 10), (504, 10), (504, 9)]
    """
    start = path[0]
    for nextPoint in path[1:]:
        yield start
        dirX = 1 if nextPoint[0] - start[0] >= 0 else -1
        dirY = 1 if nextPoint[1] - start[1] >= 1 else -1
        for varX in range(start[0] + dirX, nextPoint[0], dirX):
            yield (varX, start[1])
        for varY in range(start[1] + dirY, nextPoint[1], dirY):
            yield (start[0], varY)
        start = nextPoint
    yield start

class Wall:

    def __init__(self, paths, boundLeft, boundRight, boundDown):
        width = boundRight - boundLeft +1
        height = boundDown + 1
        self._boundLeft = boundLeft
        self._width = width
        self._boundRight = boundLeft + width - 1
        self._height = height
        self._boundDown = boundDown
        self._wall = [AIR] * (width * height)

        self._drawRock(paths)

    def _drawRock(self, paths):
        for path in paths:
            for r in iterpath(path):
                self.setCase(r, ROCK)

    def setCase(self, point, o):
        x = point[0] - self._boundLeft
        y = point[1]
        cur = self._wall[y * self._width + x]
        if cur != AIR and cur != o:
            raise Exception(f"setting case ({x}, {y}) with {o} but already set to {cur}")
        self._wall[y * self._width + x] = o

    def getCase(self, point):
        x = point[0] - self._boundLeft
        y = point[1]
        return self._wall[y * self._width + x] 

    def draw(self):
        for y in range(self._height):
            print("%4d " % y, end="")
            print("".join(self._wall[self._width*y: self._width*(y+1)]))

    def inside_bounds(self, p):
        """
        >>> Wall([], 494, 503, 9).inside_bounds((494, 0))
        True
        >>> Wall([], 494, 503, 9).inside_bounds((493, 0))
        False
        >>> Wall([], 494, 503, 9).inside_bounds((494, 9))
        True
        >>> Wall([], 494, 503, 9).inside_bounds((494, 10))
        False
        >>> Wall([], 494, 503, 9).inside_bounds((503, 9))
        True
        >>> Wall([], 494, 503, 9).inside_bounds((504, 9))
        False
        >>> Wall([], 494, 503, 9).inside_bounds((503, 10))
        False
        >>> Wall([], 494, 503, 9).inside_bounds((504, 0))
        False
        >>> Wall([], 494, 503, 9).inside_bounds((500, 4))
        True
        """
        return p[0] >= self._boundLeft and p[0] <= self._boundRight and p[1] <= self._boundDown

    def fall_one_step(self, pos):
        """
        Returns None if next step make the sand unit drops out of the wall.
        Returns pos if the unit is blocked.
        Otheriwse return the next position on the wall.
        """
        for t in (pos[0], pos[1]+1), (pos[0]-1, pos[1]+1), (pos[0]+1, pos[1]+1):
            if not self.inside_bounds(t):
                return None # means out of wall
            if self.getCase(t) == AIR:
                return t
        else:
            return pos

    def fall(self, pos):
        while True:
            next_pos = self.fall_one_step(pos)
            if next_pos is None:
                return None
            if next_pos == pos:
                self.setCase(pos, 'o')
                return pos
            pos = next_pos


if __name__ == "__main__":

    paths = []
    boundLeft = 500
    boundRight = 500
    boundDown = 0
    with open(INPUT, "r") as f :
        for line in f:
            path, minX, maxX, minY, maxY = parse_line(line)
            paths.append(path)
            boundLeft = min(boundLeft, minX)
            boundDown = max(boundDown, maxY)
            boundRight = max(boundRight, maxX)
            if minY <= 0:
                raise Exception(f"unsupported minY == {minY}")
            
    print (len(paths), boundLeft, boundDown, boundRight)
    
    wall = Wall(paths, boundLeft, boundRight, boundDown)
    wall.setCase((500,0), '+')
    wall.draw()

    start = (500, 0)
    
    i = 1
    while True:
        dest = wall.fall(start)
        #wall.draw()
        if dest is None:
            print(f"Full after step {i-1}, confirmed 961")
            wall.draw()
            break
        i+=1


