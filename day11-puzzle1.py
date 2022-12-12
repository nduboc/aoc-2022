#!/usr/bin/env python3

def add(i):
    return lambda x : x+i

def mult(i):
    return lambda x : x*i

def double():
    return lambda x : x*x

def divisible(i):
    return lambda x : x % i == 0

# def debug(*args):
#     print(*args)
def debug(*args):
    pass

def monkey(op, test, if_true, if_false):
    def turn(i, monkey_lists):
        debug("    Inspect item ", i)
        worry = int(op(i) / 3)
        debug("      corrected worry ", worry)
        if test(worry):
            debug(f"      worry {worry} send to {if_true}")
            monkey_lists[if_true].append(worry)
        else:
            debug(f"      worry {worry} send to {if_false}")
            monkey_lists[if_false].append(worry)
    return turn

SAMPLE=False

if SAMPLE:
    monkeys = [ monkey(mult(19), divisible(23), 2, 3),
                monkey(add(6), divisible(19), 2, 0),
                monkey(double(), divisible(13), 1, 3),
                monkey(add(3), divisible(17), 0, 1) ]

    monkey_lists = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]

else :
    monkeys = [monkey(mult(19), divisible(3), 2, 3),
                monkey(add(8), divisible(11), 5, 6),
                monkey(mult(13), divisible(19), 3, 1),
                monkey(add(6), divisible(5), 1, 6),
                monkey(add(5), divisible(2), 2, 0),
                monkey(double(), divisible(7), 4, 7),
                monkey(add(2), divisible(17), 5, 7),
                monkey(add(3), divisible(13), 4, 0)]



    monkey_lists = [[76, 88, 96, 97, 58, 61, 67],
                    [93, 71, 79, 83, 69, 70, 94, 98],
                    [50, 74, 67, 92, 61, 76],
                    [76, 92],
                    [74, 94, 55, 87, 62],
                    [59, 62, 53, 62],
                    [62],
                    [85, 54, 53]]

monkey_counts = [0]*len(monkeys)

for t in range(20):
    print("Turn", t)
    for m in range(len(monkeys)):
        debug("  Monkey ", m)
        for i in range(len(monkey_lists[m])):
            monkey_counts[m]+=1
            item = monkey_lists[m].pop(0)
            monkeys[m](item, monkey_lists)

print(monkey_counts)
monkey_counts.sort()
print(f"{monkey_counts[-2] * monkey_counts[-1]}, confirmed 182293")
