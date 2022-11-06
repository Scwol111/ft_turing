""" Module with some usefull utils
"""

from typing import Iterable, Type
from src.error import error_exit

def check_in_list(state: str, data: dict, listed:list) -> bool:
    """Function to check contains state in list

    Args:
        state (str): state to check
        data (dict): description
        listed (list): list with or without data state

    Returns:
        bool: True if state in list else exit with error
    """
    if data[state] not in listed:
        error_exit(f"{state} [{data[state]}] not in list")
    return True

def check_str_in_list(state: str, listed:list) -> bool:
    """Function to check containig string in list

    Args:
        state (str): string to check
        listed (list): list with or without state

    Returns:
        bool: True if string in list else exit with error
    """
    if state not in listed:
        error_exit(f"{state} not in list")
    return True

def check_list_in_list(states: list, listed: list) -> bool:
    """Function to check all elementss of list inside another list

    Args:
        states (list): list to check
        listed (list): list to find elements inside

    Returns:
        bool: True if all elements inside of list, else exit with error
    """
    for i in states:
        if not i in listed:
            error_exit(f"{i} not in states list")
    return True

def check_field(state:str, data:dict, types: type) -> bool:
    """Function to check contains state in data and check data[state] type

    Args:
        state (str): state to check
        data (dict): description of turing machine
        types (type): type of state to conform

    Returns:
        bool: True if state in data dictionary and conform right type else exit with error
    """
    try:
        if not isinstance(data[state], types):
            error_exit(f"{state} [{data[state]}] not is {types}")
    except KeyError:
        error_exit(f"not founded {state} in machine file")
    return True

def show_list(lst: list) -> None:
    """Show list to output

    Args:
        lst (list): list to show
    """
    print("[", end=' ')
    size = len(lst)
    for i in range(size):
        print(lst[i], end='')
        if i + 1 != size:
            print(',', end='')
        print(' ', end='')
    print(']')

def ft_index(lst: Iterable[Type], find: Type) -> int:
    """Find index of find in interable of types

    Args:
        lst (Iterable[Type]): object to find in
        find (Type): object to find

    Returns:
        int: index of first find
    """
    count = 0
    for i in lst:
        if i == find:
            return count
        count += 1
    return -1
