"""
Create deep turing machine desciption
"""

import json
import string
from datetime import datetime
from itertools import permutations

def alphabet_reading(previous, next_s, read):
    global data
    if previous not in data["states"]:
        data["states"].append(previous)
    if previous not in data["transitions"]:
        data["transitions"][previous] = [
            {"read": read, "to_state": next_s,
             "write": ".", "action": "RIGHT"}
        ]
    else:
        data["transitions"][previous].append(
            {"read": read, "to_state": next_s, "write": ".", "action": "RIGHT"})

def skip_one(state, char):
    global data
    if state not in data["states"]:
        data["states"].append(state)
    if state not in data["transitions"]:
        data["transitions"][state] = [
            {"read": char, "to_state": state,
             "write": ".", "action": "RIGHT"}
        ]
    else:
        data["transitions"]["init"].append(
            {"read": char, "to_state": state, "write": ".", "action": "RIGHT"})

def fill_alphabet():
    for l1 in ALPHABET:
        # alpha = l1
        alphabet_reading("init", f"al_read_{l1}", l1)
        fill_states(l1)
        # for l2 in ALPHABET:
        #     if not l2 in alpha:
        #         alpha = l1 + l2
        #         alphabet_reading(f"al_read_{l1}", f"al_read_{alpha}", l2)
        #         for l3 in ALPHABET:
        #             if not l3 in alpha:
        #                 alpha = l1 + l2 + l3
        #                 alphabet_reading(f"al_read_{l1}{l2}", f"st_read_{alpha}", l3)
        #                 fill_states(alpha)

def fill_states(alpha):
    global data
    skip_one(f"st_read_{alpha}", ":")
    small_alphabets = ALPHABET
    for i in alpha:
        small_alphabets = small_alphabets.replace(i, '')
    # for i in range(1, 6):
    for states in permutations(small_alphabets, STATES_LEN):
        srt = "".join(sorted(states))
        for i in range(5):
            # print("HHH", f"st_read_{alpha}_{srt[:i]}")
            # print("TTT",('_' + srt[:i-1]) if i > 0 else '')
            alphabet_reading(f"st_read_{alpha}{('_' + srt[:i]) if i > 0 else ''}", f"st_read_{alpha}_{srt[:i + 1]}", i)
            skip = {"read": ";", "to_state": f"init_read_{alpha}_{srt[:i + 1]}", "write": ".", "action": "RIGHT"}
            # print(data["states"])
            if i > 0 and skip not in data["transitions"][f"st_read_{alpha}_{srt[:i]}"]:
                data["transitions"][f"st_read_{alpha}_{srt[:i]}"].append(skip)
                fill_initial(alpha, srt[:i])

def fill_initial(alpha, states):
    for i in states:
        alphabet_reading(f"init_read_{alpha}_{states}", f"tr_read_{alpha}_{states}_{i}", i)
        fill_transitions(alpha, states, i)
        print(alpha, states, i)

def fill_transitions(alpha, states, init):
    pass

start = datetime.now()

# ALPHABET = string.ascii_lowercase + string.digits + "+="
ALPHABET = string.ascii_letters[:5] + string.digits[:5]
LETTER_LEN = 3
STATES_LEN = 5
TRANSITIONS_LEN = 20
ADD_ALPHA = ""

data = {
    "name": "deeper_addition",
    "alphabet": [".", ":", ";", "|", "/", "L", "R", "H", "+", "="],
    "blank": ".",
    "states": ["HALT"],
    "initial": "init",
    "finals": ["HALT"],
    "comment": "alphabet:states:initial:transitions:input",
    "alphabet_comment": "<char as add><char as plus><char as end>:",
    "states_comment": "<state char>..<state char> (max size = 5): initial:",
    "transitions_comment": "<state char><char to read><to state char/H=HALT><char to write><L/R>",
    "example": "1+=:asd;s|s.s.Rs1s1Rs+a1Ra1a1Ra=d.Ld1H.R/11+11=",
    "transitions": {
    }
}

fill_alphabet()
data["alphabet"].extend(list(ALPHABET))
with open("descriptions/deeper_addition.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(datetime.now() - start)
