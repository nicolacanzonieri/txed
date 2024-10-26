'''
KEY GETTER UTIL

Index:
- get_key()
'''

import sys
import os

from utils.data_util import get_data_value
from utils.dir_util import get_path_to
from utils.str_util import str_to_int


'''
GLOBAL VARIABLES
'''
VAR_DATA_PATH = get_path_to("data var.data")
DEBUG = False


'''
CONTROL VARIABLES
'''
up_ctrl = get_data_value(VAR_DATA_PATH, 3 if os.name == "nt" else 4)
down_ctrl = get_data_value(VAR_DATA_PATH, 5 if os.name == "nt" else 6)
left_ctrl = get_data_value(VAR_DATA_PATH, 7 if os.name == "nt" else 8)
right_ctrl = get_data_value(VAR_DATA_PATH, 9 if os.name == "nt" else 10)
fast_left_ctrl = get_data_value(VAR_DATA_PATH, 11 if os.name == "nt" else 12)
fast_right_ctrl = get_data_value(VAR_DATA_PATH, 13 if os.name == "nt" else 14)


'''
Detect special keys pressed by the user
'''
def get_key():
    if sys.platform == "win32":
        import msvcrt

        while True:
            data_path = get_path_to("data var.data")
            key = msvcrt.getch()
            if DEBUG:
                print("\n\nPRESSED KEY: " + str(key) + "\n\n")
            if key == b'\x05':    # Control-Setter
                return "CTRL+e"
            elif str(key) == up_ctrl:          # Up
                return "UP"
            elif str(key) == right_ctrl:       # Right
                return "RIGHT"
            elif str(key) == down_ctrl:        # Down
                return "DOWN"
            elif str(key) == left_ctrl:        # Left
                return "LEFT"
            elif str(key) == fast_right_ctrl:  # Fast right
                return "FAST RIGHT"
            elif str(key) == fast_left_ctrl:   # Fast left
                return "FAST LEFT"
            elif key == b'\x17':  # Close
                return "CTRL+w"
            elif key == b"\x08":  # Backspace/Delete key
                return "DELETE"
            elif key == b"\xe0":  # Cancel key (NOT SUPPORTED TODO!)
                return "CANCEL"
            elif key == b'\x13':  # Save
                return "CTRL+s"
            elif key == b'\r':    # Enter, Newline
                return "ENTER"
            elif key == b'\t':    # Tab
                return "TAB"
            return key.decode("utf-8")
    else:
        import tty
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            data_path = get_path_to("data var.data")
            key = sys.stdin.read(1)
            if DEBUG:
                print("\n\nPRESSED KEY: " + str(ord(key)) + "\n\n")
            if ord(key) == 5:     # Control-Setter
                return "CTRL+e"
            elif str(ord(key)) == up_ctrl:          # Up
                return "UP"
            elif str(ord(key)) == right_ctrl:       # Right
                return "RIGHT"
            elif str(ord(key)) == down_ctrl:        # Down
                return "DOWN"
            elif str(ord(key)) == left_ctrl:        # Left
                return "LEFT"
            elif str(ord(key)) == fast_right_ctrl:  # Fast right
                return "FAST RIGHT"
            elif str(ord(key)) == fast_left_ctrl:   # Fast left
                return "FAST LEFT"
            elif ord(key) == 23:  # Close
                return "CTRL+w"
            elif ord(key) == 19:  # Save
                return "CTRL+s"
            elif ord(key) == 127: # Backspace/Delete key
                return "DELETE"
            elif ord(key) == 126: # Cancel key (NOT SUPPORTED TODO!)
                return "CANCEL"
            elif ord(key) == 13:  # Enter, Newline
                return "ENTER"
            elif ord(key) == 9:   # Tab
                return "TAB"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key