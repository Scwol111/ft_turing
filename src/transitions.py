from src.action import Action
from src.machine import Machine

class Transition:
    current = str()
    read = str()
    to_state = str()
    write = str()
    action = Action(3)

def fill_transition(current:str, description: dict) -> Transition:
    pass