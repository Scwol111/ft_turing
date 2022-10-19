"""
main file of programm
"""

import sys

from src.execution import execute_machine
from src.machine import fill_machine


def main() -> None:
    """
    main function of programm
    """
    machine = fill_machine(sys.argv[1])
    print("Machine filled")
    
    # print(machine.alphabet, machine.blank, machine.finals, machine.initial, machine.name, machine.states, sep='\n')
    # exit(1)
    
    # for i in machine.transitions:
    #     for j in machine.transitions[i]:
    #         print(i, j.read, j.to_state, j.write, j.action)
    # exit(1)
    execute_machine(machine, sys.argv[2])

if __name__ == "__main__":
    main()
