"""
execute turnig machine file
"""
from src.current_machine import CurrentMachine
from src.machine import Machine
from src.action import Action, move_pointer
from src.transitions import show_one_transition_info
from src.error import error_exit


def show_tape(tape: str, current: int) -> None:
    """Show inputed tape of turing machine

    Args:
        tape (str): input of turing machine
        current (int): poiner to tape
    """
    print(f"[{tape[:current]}<{tape[current]}>{tape[current + 1:]}]", end=' ')

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
        founded_flag = False
        for i in machine.transitions[curent.state]:
            if i.read == curent.input[curent.current]:
                founded_flag = True
                show_tape(curent.input, curent.current)
                show_one_transition_info(curent.state, i)
                curent.state = i.to_state
                curent.input = curent.input[:curent.current] + i.write + curent.input[curent.current + 1:]
                curent.current += move_pointer(i.action)
                if curent.current < 0:
                    if i.action == Action.LEFT and i.write == machine.blank:
                        founded_flag = False
                    else:
                        curent.input = f"{machine.blank}{curent.input}"
                        curent.current = 0
                elif curent.current >= len(curent.input):
                    if i.action == Action.RIGHT and i.write == machine.blank:
                        founded_flag = False
                    else:
                        curent.input = f"{curent.input}{machine.blank}"
                break
        if not founded_flag:
            error_exit("Machine is blocked. Please check description and input")
    show_tape(curent.input, curent.current)
    print(curent.state, "-> End of work")
