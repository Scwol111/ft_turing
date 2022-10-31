"""
Create deep turing machine desciption
"""

import json
import string

ALPHABET = string.ascii_lowercase + string.digits
LETTER_LEN = 3
STATES_LEN = 5
TRANSITIONS_LEN = 20

data = {
    "name": "deeper_addition",
    "alphabet": [".", ":", "L", "R", "H"],
    "blank": ".",
    "states": ["HALT"],
    "initial": "init",
    "finals": ["HALT"],
    "comment": "alphabet:states:initial:transitions:input",
    "alphabet_comment": "<char as add><char as plus><char as end>:",
    "states_comment": "<state char>..<state char> (max size = 5): initial:",
    "transitions_comment": "<state char><char to read><to state char/H=HALT><char to write><L/R>",
    "example": "1+=:asd:s:s.s.Rs1s1Rs+a1Ra1a1Ra=d.Ld1H.R:11+11=",
    "transitions": {
    }
}

for l1 in ALPHABET:
    alpha = l1
    if "init" not in data["states"]:
        data["states"].append("init")
    if "init" not in data["transitions"]:
        data["transitions"]["init"] = [
            {"read": l1, "to_state": f"al_read_{l1}",
                "write": ".", "action": "RIGHT"}
        ]
    else:
        data["transitions"]["init"].append(
            {"read": l1, "to_state": f"al_read_{l1}", "write": ".", "action": "RIGHT"})
    for l2 in ALPHABET:
        if not l2 in alpha:
            alpha = l1 + l2
            if f"al_read_{l1}" not in data["states"]:
                data["states"].append(f"al_read_{l1}")
            if f"al_read_{l1}" not in data["transitions"]:
                data["transitions"][f"al_read_{l1}"] = [
                    {"read": l2, "to_state": f"al_read_{alpha}",
                        "write": ".", "action": "RIGHT"}
                ]
            else:
                data["transitions"][f"al_read_{l1}"].append({"read": l2, "to_state": f"al_read_{alpha}",
                                                            "write": ".", "action": "RIGHT"})
            for l3 in ALPHABET:
                if not l3 in alpha:
                    alpha = l1 + l2 + l3
                    if f"al_read_{l1}{l2}" not in data["states"]:
                        data["states"].append(f"al_read_{l1}{l2}")
                    if f"al_read_{l1}{l2}" not in data["transitions"]:
                        data["transitions"][f"al_read_{l1}{l2}"] = [
                            {"read": l3, "to_state": f"st_read_{alpha}",
                                "write": ".", "action": "RIGHT"}
                        ]
                    else:
                        data["transitions"][f"al_read_{l1}{l2}"].append({"read": l3, "to_state": f"st_read_{alpha}",
                                                                        "write": ".", "action": "RIGHT"})


data["alphabet"].extend(list(ALPHABET))
with open("descriptions/deeper_addition.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=4)
