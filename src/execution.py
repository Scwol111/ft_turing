from src.current_machine import CurrentMachine
from src.machine import Machine

def execute_machine(machine: Machine, tape: str) -> None:
    """_summary_

    Args:
        machine (Machine): _description_
        tape (str): _description_
    """
    curent = CurrentMachine()
    curent.state = machine.initial
    curent.input = tape
    while True:
        #TODO do somthing
        if curent.state in machine.finals:
            break
