"""
Create deep turing machine desciption
"""

import json
import string


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
        data["transitions"]["init"].append(
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
        alpha = l1
        alphabet_reading("init", f"al_read_{l1}", l1)
        for l2 in ALPHABET:
            if not l2 in alpha:
                alpha = l1 + l2
                alphabet_reading(f"al_read_{l1}", f"al_read_{alpha}", l2)
                for l3 in ALPHABET:
                    if not l3 in alpha:
                        alpha = l1 + l2 + l3
                        alphabet_reading(f"al_read_{l1}{l2}", f"st_read_{alpha}", l3)
                        fill_states(alpha)

def fill_states(alpha):
    skip_one(f"st_read_{alpha}", ":")
    

ALPHABET = string.ascii_lowercase + string.digits + "+="
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
