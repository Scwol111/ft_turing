"""
Create deep turing machine desciption
"""

import json
import string
from datetime import datetime
from itertools import permutations

class Act:
    R = "RIGHT"
    L = "LEFT"

def alphabet_reading(previous, next_s, read:str):
    global data
    add_state(previous)
    add_state(next_s)
    if previous not in data["transitions"]:
        data["transitions"][previous] = [
            {"read": read, "to_state": next_s,
             "write": ".", "action": "RIGHT"}
        ]
    else:
        data["transitions"][previous].append(
            {"read": read, "to_state": next_s, "write": ".", "action": "RIGHT"})

def skip_one(state, char:str):
    global data
    add_state(state)
    if state not in data["transitions"]:
        data["transitions"][state] = [
            {"read": char, "to_state": state,
             "write": ".", "action": "RIGHT"}
        ]
    else:
        data["transitions"]["init"].append(
            {"read": char, "to_state": state, "write": ".", "action": "RIGHT"})

def read_transactions(prev_s, next_s, read:str, write, action):
    global data
    add_state(prev_s)
    add_state(next_s)
    if prev_s not in data["transitions"]:
        data["transitions"][prev_s] = [
            {"read": read, "to_state": next_s,
             "write": write, "action": action}
        ]
    else:
        data["transitions"][prev_s].append(
            {"read": read, "to_state": next_s, "write": write, "action": action})

def skip_transtactions(alpha, states, char, init):
    for i in f"{states}H":
        read_transactions(f"tr_read_{char}_{states}_{init}", f"tr_read_{char}_{states}_{init}", i, i, Act.R)
    for j in alpha:
        read_transactions(f"tr_read_{char}_{states}_{init}", f"tr_read_{char}_{states}_{init}", j, j, Act.R)
    read_transactions(f"tr_read_{char}_{states}_{init}", f"tr_read_{char}_{states}_{init}", "R", "R", Act.R)
    read_transactions(f"tr_read_{char}_{states}_{init}", f"tr_read_{char}_{states}_{init}", "L", "L", Act.R)
    # read_transactions(f"tr_read_{char}_{states}_{init}", f"{init}_{char}_{states}_input", "/", "/", Act.R)
    read_transactions(f"tr_read_{char}_{states}_{init}", "HALT", "/", "/", Act.R)

def fill_alphabet():
    for l1 in ALPHABET:
        alphabet_reading("init", f"st_read_{l1}", l1)
        fill_states(l1)

def add_state(state):
    global data
    if state not in data["states"]:
        data["states"].append(state)

def fill_states(alpha):
    global data
    skip_one(f"st_read_{alpha}", ":")
    small_alphabets = ALPHABET
    for i in alpha:
        small_alphabets = small_alphabets.replace(i, '')
    # for i in range(1, 6):
    for states in permutations(small_alphabets, STATES_LEN):
        srt = "".join(sorted(states))
        for i in range(STATES_LEN):
            alphabet_reading(f"st_read_{alpha}{('_' + srt[:i]) if i > 0 else ''}", f"st_read_{alpha}_{srt[:i + 1]}", states[i])
            skip = {"read": ";", "to_state": f"tr_read_{alpha}_{srt[:i + 1]}", "write": ".", "action": "RIGHT"}
            if i > 0 and skip not in data["transitions"][f"st_read_{alpha}_{srt[:i]}"]:
                data["transitions"][f"st_read_{alpha}_{srt[:i]}"].append(skip)
                fill_initial(alpha, srt[:i])

def fill_initial(alpha, states):
    add_state(f"st_read_{alpha}_{states}")
    for i in states:
        alphabet_reading(f"st_read_{alpha}_{states}", f"tr_read_{alpha}_{states}_{i}", i)
        fill_transitions(alpha, states, i)

def fill_transitions(alpha, states, init):
    skip_one(f"tr_read_{alpha}_{states}_{init}", "|")
    skip_transtactions(f"{alpha}{ADD_ALPHA}", states, alpha, init)


start = datetime.now()

# ALPHABET = string.ascii_lowercase + string.digits + "+="
ALPHABET = string.ascii_lowercase[:5] + str(string.digits[:5])
LETTER_LEN = 3
STATES_LEN = 4
TRANSITIONS_LEN = 20
ADD_ALPHA = "+=."

data = {
    "name": "deeper_addition",
    "alphabet": [".", ":", ";", "|", "/", "L", "R", "H", "+", "="],
    "blank": ".",
    "states": ["HALT"],
    "initial": "init",
    "finals": ["HALT"],
    "comment": "alphabet:states;initial|transitions/input",
    "alphabet_comment": "<char as add><char as plus><char as end>:",
    "states_comment": "<state char>..<state char> (max size = 5): initial:",
    "transitions_comment": "<state char><char to read><to state char/H=HALT><char to write><L/R>",
    "example": "1:abc;a|a.a.Ra1a1Ra+b1Rb1b1Rb=c.Lc1H.R/11+11=",
    "transitions": {
    }
}

fill_alphabet()
data["alphabet"].extend(list(ALPHABET))
with open("descriptions/deeper_addition.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(datetime.now() - start)
