#!/usr/bin/env python3

input="day8-input.txt"

map = ""
size = 0

def i(l, c):
    global map
    global size
    return map[l*size+c]

def visible_up(l, c):
    m = max([i(x, c) for x in range(0, l)])
    return m < i(l, c)

def visible_down(l, c):
    m = max([i(x, c) for x in range(l+1, size)])
    return m < i(l, c)

def visible_left(l, c):
    m = max([i(l, x) for x in range(0, c)])
    return m < i(l, c)

def visible_right(l, c):
    m = max([i(l, x) for x in range(c+1, size)])
    return m < i(l, c)

def visible(l, c):
    return (l == 0 or l == size-1 or c == 0 or c == size-1 or
       visible_up(l, c) or visible_down(l, c) or visible_left(l, c) or visible_right(l, c))

def main():
    global map
    global size
    ln = 0

    with open(input, "r") as f:
        map = f.readline().strip()
        ln +=1
        size = len(map)
        for l in f:
            map +=  l.strip()
            ln +=1

    if ln != size:
        print(f"width and length do not match: {size}x{ln}")
        return

    visibles = sum(1 if visible(x, y) else 0 for x in range(0, size) for y in range(0, size))
    print(f"Result {visibles}, confirmed 1798")


if __name__ == "__main__":
    main()

