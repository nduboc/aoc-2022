#!/usr/bin/env python3

input = "day9-input.txt"

def rel_pos(head, tail):
    return (tail[0] - head[0], tail[1] - head[1])

# . . . . .
# . . . . .
# . . X . .
# . . . . .
# . . . . .

tail_moves = {
    (2, 0): (-1, 0),
    (2, 1): (-1, -1),
    (2, 2): (-1, -1),
    (1, 2): (-1, -1),
    (0, 2): (0, -1),
    (-1, 2): (1, -1),
    (-2, 2): (1, -1),
    (-2, 1): (1, -1),
    (-2, 0): (1, 0),
    (-2, -1): (1, 1),
    (-2, -2): (1, 1),
    (-1, -2): (1, 1),
    (0, -2): (0, 1),
    (1, -2): (-1, 1),
    (2, -2): (-1, 1),
    (2, -1): (-1, 1),
}

def move_tail(head_pos, tail_pos):
    rel = rel_pos(head_pos, tail_pos)
    if abs(rel[0]) <= 1 and abs(rel[1]) <= 1:
        return tail_pos
    tail_move = tail_moves[rel]
    return (tail_pos[0] + tail_move[0], tail_pos[1] + tail_move[1])

moves_by_direction = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}
def move_head(head_pos, direction):
    m = moves_by_direction[direction]
    return head_pos[0] + m[0], head_pos[1] + m[1]

if __name__ == "__main__":
    rope = [(0, 0)] * 10
    visited = set()
    visited.add(rope[-1])
    with open(input, "r") as f:
        for l in f:
            l = l.strip()
            direction = l[0]
            distance = int(l[2:])
            for i in range(distance):
                rope[0] = move_head(rope[0], direction)
                for t in range(1, len(rope)):
                    rope[t] = move_tail(rope[t-1], rope[t])
                visited.add(rope[-1])
    print(f"Visited {len(visited)} positions, confirmed: 2593")
