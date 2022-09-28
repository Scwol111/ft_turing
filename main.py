from platform import machine
import sys
from src.machine import Machine, fill_machine
# import os

def main() -> None:
    machine = fill_machine(sys.argv[1])
    print(machine)

if __name__ == "__main__":
    main()