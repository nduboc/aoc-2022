#!/usr/bin/env python3

path="day2-input.txt"
total=0


LOST = 0
DRAW = 3
WIN = 6

ROCK = 'ROCK'; PAPER = 'PAPER'; SCISSOR = 'SCISSOR'
his_to_object = {'A' : ROCK, 'B': PAPER, 'C': SCISSOR}
mine_to_object = {'X' : ROCK, 'Y': PAPER, 'Z': SCISSOR}

round_score = {ROCK: 1, PAPER: 2, SCISSOR: 3}

# key: his/mine, result: outcome score for me
round_outcome = {
    (ROCK, ROCK): DRAW,
    (ROCK, PAPER): WIN,
    (ROCK, SCISSOR): LOST,
    (PAPER, ROCK): LOST,
    (PAPER, PAPER): DRAW,
    (PAPER, SCISSOR): WIN,
    (SCISSOR, ROCK): WIN,
    (SCISSOR, PAPER): LOST,
    (SCISSOR, SCISSOR): DRAW,   
    }

with open(path) as fIn:
    for line in fIn:
        his_code, mine_code = line.strip().split(" ")
        his = his_to_object[his_code]
        mine = mine_to_object[mine_code]
        
        score = round_score[mine] + round_outcome[(his, mine)]
        total += score

print(total, "confirmed: 12645")
# correct: 12645