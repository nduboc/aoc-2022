#!/usr/bin/python3

path="day1-input.txt"

def inject(val, max):
    if len(max) < 3:
        return sorted(max+[val]), True
    elif val > max[0]:
        max = max + [val]
        return sorted(max)[1:4], True
    else:
        return max, False


max = []
with open(path) as fIn:
    current = 0
    ln = 0
    while True:
        line = fIn.readline()
        ln += 1
        if line == "\n" or line == "":
            print(f"{current}", end="")
            max, injected = inject(current, max)
            if injected:
                print(" new max, line", ln)
            else:
                print(f" max still {max}")
            current = 0
            if line == "":
                break
        else:
            v = int(line[:-1])
            current += v

print(sum(max), ", confirmed 213089")
