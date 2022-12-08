#!/usr/bin/env python3

input="day8-input.txt"

map = ""
size = 0

def i(l, c):
    global map
    global size
    return map[l*size+c]

def visibility(v, line):
    if len(line) == 0:
        return 0
    for i in range(len(line)):
        if line[i] >= v:
            return i+1
    return len(line)

def score_at(l, c):
    v = i(l, c)
    score_up = visibility(v, [i(x, c) for x in range(l-1, -1, -1)])
    score_down = visibility(v, [i(x, c) for x in range(l+1, size)])
    score_left = visibility(v, [i(l, x) for x in range(c-1, -1, -1)])
    score_right = visibility(v, [i(l, x) for x in range(c+1, size)])
    return score_up * score_down * score_left * score_right
    
    

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

    result = 0
    for x in range(0, size):
        for y in range(0, size):
            result = max(result, score_at(x, y))
    print(f"Result {result}, confirmed 259308")


if __name__ == "__main__":
    main()

