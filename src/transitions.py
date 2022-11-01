"""
File to work with Transitions
"""
from src.machine import Machine
from src.action import create_action, show_action
from src.utils import check_field
from src.utils import check_in_list


class Transition:
    """Struct to contain transtition of turing machine
    """
    current = str()
    read = str()
    to_state = str()
    write = str()
    action = None

def fill_transition(current:str, description: dict, machine: Machine) -> Transition:
    """_summary_

    Args:
        current (str): _description_
        description (dict): _description_

    Returns:
        Transition: _description_
    """
    out = Transition()
    out.current = current
    if check_field("read", description, str) and check_in_list("read", description, machine.alphabet):
        out.read = description["read"]
    if check_field("to_state", description, str) and check_in_list("to_state", description, machine.states):
        out.to_state = description["to_state"]
    if check_field("write", description, str) and check_in_list("write", description, machine.alphabet):
        out.write = description["write"]
    if check_field("action", description, str):
        out.action = create_action(description["action"])
    return out

def show_one_transition_info(state: str, rule: Transition) -> None:
    """Show information about one Transition

    Args:
        state (str): state of Transitions
        rule (Transition): Transition structure
    """
    print(f"({state}, {rule.read}) -> ({rule.to_state}, {rule.write}, {show_action(rule.action)})")

def show_transition_info(state: str, rules: list[Transition]) -> None:
    """Show information about Transitions

    Args:
        state (str): state of Transitions
        rules (list[Transition]): list of rules with Transitions
    """
    for i in rules:
        show_one_transition_info(state, i)
