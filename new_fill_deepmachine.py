import json
import string
from datetime import datetime
from itertools import permutations, combinations

class Act:
    L="LEFT"
    R="RIGHT"

def add_state(state):
    global data
    if state not in data["states"]:
        data["states"].append(state)

def add_transitions(state, read, to_state, write, action):
    global data
    add_state(state)
    add_state(to_state)
    if state not in data["transitions"]:
        data["transitions"][state] = [
            {"read": read, "to_state": to_state,
             "write": write, "action": action}
        ]
    else:
        data["transitions"][state].append(
            {"read": read, "to_state": to_state, "write": write, "action": action})


def goto_input(alpha, state, init):
    al = f"{alpha}{ADD_ALPHA}{state}{ACTION_ALPHA}"
    for i in al:
        add_transitions(f"goto_input_{alpha}_{state}_{i}", i, f"goto_input_{alpha}_{state}_{i}", i, Act.R)
    add_transitions(f"goto_input_{alpha}_{state}_{i}", END_TRANS, f"goto_input_{alpha}_{state}_{i}", END_TRANS, Act.R)

def read_init(alpha, state):
    for i in state:
        add_transitions(f"read_init_{alpha}_{state}", i, f"goto_input_{alpha}_{state}_{i}", BLANK, Act.R)
        # add_transitions(f"goto_input_{alpha}_{state}_{i}", END_INIT, f"goto_input_{alpha}_{state}_{i}", BLANK, Act.R)
        add_transitions(f"goto_input_{alpha}_{state}_{i}", END_INIT, f"goto_input_{alpha}_{state}_{i}", BLANK, Act.R)
        goto_input(alpha, state, i)

def fill_states(alpha):
    for rn in range(1, STATES_LEN + 1):
        for state in permutations(ALPHABET.replace(alpha, ''), rn):
            state = "".join(state)
            srt = "".join(sorted(state))
            if rn == 1:
                past = f"st_read_{alpha}"
            else:
                past = f"st_read_{alpha}_{srt[:-1]}"
            add_transitions(past, state[-1], f"st_read_{alpha}_{srt}", BLANK, Act.R)
            add_transitions(f"st_read_{alpha}_{srt}", END_STATE, f"read_init_{alpha}_{srt}", BLANK, Act.R)
            read_init(alpha, srt)
    # for i in combinations(ALPHABET.replace(alpha, ""), STATES_LEN):
    #     for rn in range(STATES_LEN):
    #         past = f"st_read_{alpha}"
    #         for state in permutations(i, rn):
    #             add_transitions(past, state[-1], f"st_read_{alpha}_{''}", BLANK)

def fill_alphabet():
    for i in ALPHABET:
        add_transitions("init", i, f"st_read_{i}", BLANK, Act.R)
        add_transitions(f"st_read_{i}", END_ALPHA, f"st_read_{i}", BLANK, Act.R)
        # add_transitions(f"st_read_{i}", END_ALPHA, "HALT", BLANK, Act.R)
        fill_states(i)


start = datetime.now()

END_INIT = "|"
END_STATE = ";"
END_ALPHA = ":"
END_TRANS = "/"
BLANK = "."
ALPHABET = string.ascii_lowercase[:5] + str(string.digits[:5])
LETTER_LEN = 3
STATES_LEN = 4
TRANSITIONS_LEN = 20
ADD_ALPHA = "+=."
ACTION_ALPHA = "LRH"

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
with open("descriptions/deeper_addition_V2.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(datetime.now() - start)