"""
main file of programm
"""

import sys
from src.execution import execute_machine
from src.work_machine import fill_machine
from src.work_machine import show_machine_info
from src.error import error_exit
from src.utils import ft_index

def show_help() -> None:
    """Show help prompt
    """
    print("""usage: ft_turing [-h] jsonfile input

positional arguments:
    jsonfile json description of the machine
    
    input input of the machine
    
optional arguments:
    -h, --help - show this help message and exit
    --hide - hide transitions info
""")
    sys.exit(0)

# def start_working()

def main() -> None:
    """
    main function of programm
    """
    hide = False
    if "-h" in sys.argv or "--help" in sys.argv:
        show_help()
    elif "--hide" in sys.argv:
        hide = True
        h_idx = ft_index(sys.argv, "--hide")
        sys.argv = sys.argv[:h_idx] + sys.argv[h_idx + 1:]
    if len(sys.argv) == 3:
        machine = fill_machine(sys.argv[1])
        machine.hide_transitions = hide
        show_machine_info(machine)
        execute_machine(machine, sys.argv[2])
        print("*" * 100)
    elif len(sys.argv) > 3:
        error_exit("Too many arguments. Use -h to help")
    else:
        error_exit("Not enough arguments. Use -h to help")

if __name__ == "__main__":
    main()
