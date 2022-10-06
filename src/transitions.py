from src.action import Action, create_action
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
    if (check_field("read", description, str)):
        out.read = description["read"]
    if (check_field("to_state", description, str)):
        out.read = description["to_state"]
    if (check_field("write", description, str)):
        out.write = description["write"]
    if (check_field("action", description, str)):
        out.action = create_action(description["action"])
    return out