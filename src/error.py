""" Module to exit with error
"""
import sys

def error_exit(error:str):
    """Show error message end exit with error code 1

    Args:
        error (str): error message
    """
    print(f"ERROR: {error}")
    sys.exit(1)
