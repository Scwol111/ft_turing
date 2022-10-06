from enum import Enum

class Action(Enum):
    LEFT = 1
    RIGHT = 2
    STAY = 3

def create_action(action: str) -> Action:
    if (action.upper() == "RIGHT"):
        return Action.RIGHT
    if (action.upper() == "LEFT"):
        return Action.LEFT
    return Action.STAY