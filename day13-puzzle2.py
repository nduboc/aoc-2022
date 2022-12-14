#!/usr/bin/env python3

import functools

INPUT = "day13-input.txt"


def right_order(val1, val2):
    if isinstance(val1, int) and isinstance(val2, int):
        if val1 == val2:
            return 0
        else:
            return val1 - val2
    if isinstance(val1, int):
        return right_order([val1],val2)
    if isinstance(val2, int):
        return right_order(val1, [val2])
    if len(val1) == 0 and len(val2) == 0:
        return 0
    if len(val1) == 0:
        return -1
    if len(val2) == 0:
        return 1
    order_of_first = right_order(val1[0], val2[0])
    if order_of_first == 0:
        return right_order(val1[1:], val2[1:])
    else:
        return order_of_first

if __name__ == "__main__":
    with open(INPUT, "r") as fIn:
        cur_index = 0
        result = 0
        vals = []
        vals.append([[2]])
        vals.append([[6]])
        for line in fIn:
            if line == "\n":
                continue
            vals.append(eval(line))

        vals.sort(key=functools.cmp_to_key(right_order))

        divider1_i = vals.index([[2]])+1
        divider2_i = vals.index([[6]])+1

        print(f"Result {divider1_i * divider2_i }, confirmed 22464")
        