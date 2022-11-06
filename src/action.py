"""
Enum and functions for turing machine action
"""
from src.error import error_exit

class Action:
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
    if action.upper() == "RIGHT": #TODO remake
        return Action.RIGHT
    if action.upper() == "LEFT":
        return Action.LEFT
    if action.upper() == "STAY":
        return Action.STAY
    return error_exit("Unknown action")

def move_pointer(action: Action) -> int:
    """Detect what need todo with inputed action

    Args:
        action (Action): one of LEFT, RIGHT or STAY

    Returns:
        int: _description_ #TODO set
    """
    if action == Action.LEFT:
        return -1
    if action == Action.RIGHT:
        return 1
    if action == Action.STAY:
        return 0
    return error_exit("Unknown action")

def show_action(action: Action) -> str:
    """Show information about action

    Args:
        action (Action): action what to do

    Returns:
        str: String of action
    """
    if action == Action.LEFT:
        return "LEFT"
    if action == Action.RIGHT:
        return "RIGHT"
    if action == Action.STAY:
        return "STAY"
    return error_exit("Unknown action")
