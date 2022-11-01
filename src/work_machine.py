"""Module to fill information about turing machine
"""

import json
from src.machine import Machine
from src.transitions import show_transition_info
from src.transitions import fill_transition
from src.error import error_exit
from src.utils import check_str_in_list
from src.utils import check_in_list
from src.utils import check_list_in_list
from src.utils import check_field
from src.utils import show_list

def fill_machine(filename:str) -> Machine:
    """_summary_

    Args:
        filename (str): _description_

    Returns:
        Machine: Turing machine description
    """
    machine = Machine()
    try:
        with open(filename, "r", encoding='utf-8') as file:
            data = json.load(file)
    except Exception as error:
        error_exit(f"Error while reading file {filename}. More info below:\n{error.args}")
    if check_field("name", data, str):
        machine.name = data["name"]
    if check_field("alphabet", data, list):
        machine.alphabet = data["alphabet"]
    if check_field("blank", data, str) and check_in_list("blank", data, machine.alphabet):
        machine.blank = data["blank"]
    if check_field("states", data, list):
        machine.states = data["states"]
    if check_field("initial", data, str) and check_in_list("initial", data, machine.states):
        machine.initial = data["initial"]
    if check_field("finals", data, list) and check_list_in_list(data["finals"], data["states"]):
        machine.finals = data["finals"]
    if check_field("transitions", data, dict):
        for i in data["transitions"]:
            if check_str_in_list(i, machine.states):
                machine.transitions[i] = [fill_transition(i, j, machine) for j in data["transitions"][i]]
    return machine

def show_machine_info(machine: Machine) -> None:
    """Show summary information about parsed turing machine

    Args:
        machine (Machine): parsed and filled machine description
    """
    print("*" * 100)
    size = len(machine.name)
    print("*", " " * (49 - size // 2), machine.name, " " * (49 - size // 2 - size % 2), '*', sep='')
    print("*" * 100)
    print("Alphabet:", end='')
    show_list(machine.alphabet)
    print("States:", end='')
    show_list(machine.states)
    print("Initial:", machine.initial)
    print("Finals:", end='')
    show_list(machine.finals)
    if not machine.hide_transitions:
        for i in machine.transitions:
            show_transition_info(i, machine.transitions[i])
    else:
        print("Transitions hidden by user")
    print("*" * 100)
