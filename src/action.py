"""
Enum and functions for turing machine action
"""
from enum import Enum
from src.error import error_exit

class Action(Enum):
    """ Enum for turing machine action. Present action LEFT, RIGHT or STAY
    """
    LEFT = 1
    RIGHT = 2
    STAY = 3

def create_action(action: str) -> Action:
    """Creating enum action from it's string

    Args:
        action (str): String with action

    Returns:
        Action: Enum with turing machine action
    """
    if action.upper() == "RIGHT":
        return Action.RIGHT
    elif action.upper() == "LEFT":
        return Action.LEFT
    elif action.upper() == "STAY":
        return Action.STAY
    error_exit("Unknown action")

def move_pointer(action: Action) -> int:
    """Detect what need todo with inputed action

    Args:
        action (Action): one of LEFT, RIGHT or STAY

    Returns:
        int: _description_
    """
    if action == Action.LEFT:
        return -1
    elif action == Action.RIGHT:
        return 1
    elif action == Action.STAY:
        return 0
    error_exit("Unknown action")
