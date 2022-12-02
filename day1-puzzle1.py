#!/usr/bin/python3

path="day1-input.txt"

max = -1
with open(path) as fIn:
    current = 0
    while True:
        line = fIn.readline()
        if line == "\n" or line == "":
            print(f"{current}", end="")
            if current > max:
                max = current
                print(" new max")
            else:
                print(f" max still {max}")
            current = 0
            if line == "":
                break
        else:
            v = int(line[:-1])
            current += v

print(max, ", confirmed 72718")
