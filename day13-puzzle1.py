#!/usr/bin/env python3

INPUT = "day13-input.txt"

UNDEF = "UNDEF"

def right_order(val1, val2):
    if isinstance(val1, int) and isinstance(val2, int):
        if val1 == val2:
            return UNDEF
        else:
            return val1 < val2
    if isinstance(val1, int):
        return right_order([val1],val2)
    if isinstance(val2, int):
        return right_order(val1, [val2])
    if len(val1) == 0 and len(val2) == 0:
        return UNDEF
    if len(val1) == 0:
        return True
    if len(val2) == 0:
        return False
    order_of_first = right_order(val1[0], val2[0])
    if order_of_first == UNDEF:
        return right_order(val1[1:], val2[1:])
    else:
        return order_of_first

if __name__ == "__main__":
    with open(INPUT, "r") as fIn:
        cur_index = 0
        result = 0
        while True:
            line1 = fIn.readline()
            if line1 == "":
                break
            if line1 == "\n":
                continue
            line2 = fIn.readline()
            cur_index += 1

            val1 = eval(line1)
            val2 = eval(line2)

            if right_order(val1, val2):
                result += cur_index
        print(f"Result {result}, confirmed 6428")
        