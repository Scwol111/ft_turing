"""
main file of programm
"""

import sys
from src.execution import execute_machine
from src.machine import fill_machine
from src.machine import show_machine_info
from src.error import error_exit


def main() -> None:
    """
    main function of programm
    """
    if "-h" in sys.argv or "--help" in sys.argv:
        print("""usage: ft_turing [-h] jsonfile input

positional arguments:
    jsonfile json description of the machine
    
    input input of the machine
    
optional arguments:
    -h, --help show this help message and exit
""")
    elif len(sys.argv) == 3:
        machine = fill_machine(sys.argv[1])
        show_machine_info(machine)
        execute_machine(machine, sys.argv[2])
        print("*" * 100)
    else:
        error_exit("Not enough arguments. Use -h to help")

if __name__ == "__main__":
    main()
