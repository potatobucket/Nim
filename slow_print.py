"""
Printing module to print one character at a time to terminal.
"""

from time import sleep as slp

def slow_print(string = "Testing slow_print function", delay = 0.05):
    """
Prints string characters one at a time to terminal.\n
Delay is time in seconds to wait before printing next character.
    """
    for letter in string:
        print(letter, end = "", flush = True)
        slp(delay)
    print("\n", end = "")
