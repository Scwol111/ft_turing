"""
main file of programm
"""

import sys

from src.execution import execute_machine
from src.machine import fill_machine
from src.machine import show_machine_info


def main() -> None:
    """
    main function of programm
    """
    machine = fill_machine(sys.argv[1])
    show_machine_info(machine)
    execute_machine(machine, sys.argv[2])
    print("*" * 100)

if __name__ == "__main__":
    main()
