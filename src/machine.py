""" File to describe and fill turing machine
"""

class Machine:
    """Structure to contain turing machine description
    """
    name = str()
    alphabet = list()
    blank = str()
    states = list()
    initial = str()
    finals = list()
    transitions = dict()
    hide_transitions = False
