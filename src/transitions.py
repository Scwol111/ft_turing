"""
File to work with Transitions
"""
from src.action import Action, create_action, show_action
from src.error import error_exit


class Transition:
    current = str()
    read = str()
    to_state = str()
    write = str()
    action = Action(3)

def check_field(state:str, data:dict, types) -> bool:
    try:
        data[state]
        if not type(data[state]) is types:
            error_exit(f"{state} not is {types}")
    except:
        error_exit(f"not founded {state} in machine file")
    return True

def fill_transition(current:str, description: dict) -> Transition:
    out = Transition()
    out.current = current
    if check_field("read", description, str):
        out.read = description["read"]
    if check_field("to_state", description, str):
        out.to_state = description["to_state"]
    if check_field("write", description, str):
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
