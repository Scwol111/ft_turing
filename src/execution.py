"""
execute turnig machine file
"""
from src.current_machine import CurrentMachine
from src.machine import Machine
from src.action import move_pointer


def execute_machine(machine: Machine, tape: str) -> None:
    """ Execute prepared machine

    Args:
        machine (Machine): Turing machine description
        tape (str): Input tape for turing machine
    """
    curent = CurrentMachine()
    curent.state = machine.initial
    curent.input = f"{machine.blank}{tape}{machine.blank}"
    curent.current = 1
    while curent.state not in machine.finals:
        # print(curent.state, curent.input)#TODO delete
        for i in machine.transitions[curent.state]:
            # print(curent.input[curent.current], i.read) #TODO delete
            if i.read == curent.input[curent.current]:
                # print(i.read, i.to_state, i.write, i.action)#TODO delete
                curent.state = i.to_state
                curent.input = curent.input[:curent.current] + i.write + curent.input[curent.current + 1:]
                curent.current += move_pointer(i.action)
                break
        # print(curent.state, machine.finals, curent.state not in machine.finals)#TODO delete
    print("END SIMULATION: ", curent.input)
