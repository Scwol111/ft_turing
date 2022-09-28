from src.transitions import *
from src.error import error_exit
import json


class Machine:
    name = str()
    alphabet = list()
    blank = str()
    states = list()
    initial = str()
    finals = list()
    transitions = dict()

def check_field(state:str, data:dict, types) -> bool:
    try:
        data[state]
        if not type(data[state]) is types:
            error_exit(f"{state} not is {types}")
    except:
        error_exit(f"not founded {state} in machine file")
    return True

def check_in_list(state: str, data: dict, listed:list):
    if not data[state] in listed:
        error_exit(f"{state} not in list")
    return True

def check_list_in_list(states: list, listed: list) -> bool:
    for i in states:
        if not i in listed:
            error_exit(f"{i} not in states list")


def fill_machine(filename:str) -> Machine:
    machine = Machine()
    try:
        with open(filename, "r", encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:#TODO do something
        error_exit(f"Error while reading file {filename}. More info below:\n{e.args}")
    if (check_field("name", data, str)):
        machine.name = data["name"]
    if (check_field("alphabet", data, list)):
        machine.alphabet = data["alphabet"]
    if (check_field("blank", data, str) and check_in_list("blank", data, machine.alphabet)):
        machine.blank = data["blank"]
    if (check_field("states", data, list)):
        machine.states = data["states"]
    if (check_field("initial", data, str) and check_in_list("initial", data, machine.states)):
        machine.initial = data["initial"]
    if (check_field("finals", data, list) and check_list_in_list(data["finals"], data["states"])):
        machine.finals = data["finals"]
    if (check_field("transitions", data, dict)):
        pass #TODO adding transitions
    return machine
