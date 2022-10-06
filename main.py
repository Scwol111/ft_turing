"""_summary_
"""

import sys

from src.execution import execute_machine
from src.machine import Machine, fill_machine


def main() -> None:
    machine = fill_machine(sys.argv[1])
    execute_machine(machine, sys.argv[2])
    print(machine.transitions)

if __name__ == "__main__":
    main()
