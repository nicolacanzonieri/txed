'''
CONTROL SETTER

Index:
- set_control()
- set_controls()
'''


up_label = ""
down_label = ""
left_label = ""
right_label = ""
fast_right_label = ""
fast_left_label = ""


import sys
import os


from utils.data_util import edit_data
from utils.dir_util import get_path_to
from utils.os_util import clear_terminal
from utils.ui_util import print_top_border, print_bottom_border


debug = True


'''
Detect special keys pressed by the user
'''
if sys.platform == "win32":
    import msvcrt

    def get_key():
        while True:
            key = msvcrt.getch()
            if debug:
                print("\n\nPRESSED KEY: " + str(key) + "\n\n")
            if key == b'\x05':    # Control-Setter
                return "CTRL+e"
            elif key == b'\x17':  # Close
                return "CTRL+w"
            elif key == b"\x08":  # Backspace/Delete key
                return "DELETE"
            elif key == b"\xe0":
                return "CANCEL"   # Cancel key (NOT SUPPORTED TODO!)
            elif key == b'\x13':
                return "CTRL+s"   # Save
            elif key == b'\r':
                return "ENTER"    # Enter, Newline
            return key.decode("utf-8")

else:
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
            if debug:
                print("\n\nPRESSED KEY" + str(key) + "\n\n")
            if ord(key) == 5:     # Control-Setter
                return "CTRL+e"
            if ord(key) == 23:    # Close
                return "CTRL+w"
            elif ord(key) == 19:  # Save
                return "CTRL+s"
            elif ord(key) == 127: # Backspace/Delete key
                return "DELETE"
            elif ord(key) == 126: # Cancel key (NOT SUPPORTED TODO!)
                return "CANCEL"
            elif ord(key) == 13:  # Enter, Newline
                return "ENTER"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key


def set_control(max_string_length, control, label):
    '''
    Change the key for a specific control

    @param "max_string_length" : Integer with the maximum string length allowed
    @param "control" : string with the name of the control that will be changed
    @param "label" : label for the current control (for example CTRL+T)
    '''
    new_key = ""
    warning_msg = ""
    while True:
        clear_terminal()
        title = "CHANGING CONTROL " + control
        print_top_border(max_string_length, title)
        
        # PRINT
        print("\n\n")
        print("To remap this navigation key, press Ctrl and then any key...")
        print("")
        print("CURRENT KEY: " + label)
        if new_key == "" and warning_msg == "":
            print("\n\n")
        elif new_key != "" and warning_msg == "":
            print("NEWER KEY:   " + new_key)
            print("\n")
        elif new_key == "" and warning_msg != "":
            print(warning_msg)
            print("\n")

        print_bottom_border(max_string_length, "[CTRL+W : End remapping , CTRL+S : Save current key]")

        user_input = get_key()

        if control == "UP":
            data_row = 4 if os.name == "nt" else 5
        elif control == "DOWN":
            data_row = 6 if os.name == "nt" else 7
        elif control == "LEFT":
            data_row = 8 if os.name == "nt" else 9
        elif control == "RIGHT":
            data_row = 10 if os.name == "nt" else 11
        elif control == "FAST LEFT":
            data_row = 12 if os.name == "nt" else 13
        elif control == "FAST RIGHT":
            data_row = 14 if os.name == "nt" else 15

        if user_input == "CTRL+w":
            break
        elif user_input == "CTRL+s":
            edit_data(get_path_to("data sys_var.data"), data_row, "'" + user_input + "'")
        elif user_input == "CTRL+e":
            warning_msg = "CTRL+E is already used by the control setter!"
            new_key = ""
        elif user_input == "DELETE":
            warning_msg = "DELETE is a priority key!"
            new_key = ""
        elif user_input == "CANCEL":
            warning_msg = "CANCEL is a priority key!"
            new_key = ""
        elif user_input == "ENTER":
            warning_msg = "ENTER is a priority key!"
            new_key = ""
        else:
            warning_msg = ""
            new_key = str(ord(user_input)) if os.name == "nt" else str(user_input)



def set_controls(max_string_length):
    '''
    Start Control-Setter

    @param "max_string_length" : Integer with the maximum string length allowed
    '''
    title = "CONTROL-SETTER"
    while True:
        clear_terminal()
        print(title, end="")
        for i in range(max_string_length - len(title) - len("MAX: " + str(max_string_length))):
            print(" ", end="")
        print("MAX: " + str(max_string_length))
        for i in range(max_string_length):
            print("=", end="")
        print("\n", end="")

        # PRINT
        print("[1] : UP = " + up_label)
        print("[2] : DOWN = " + down_label)
        print("[3] : LEFT = " + left_label)
        print("[4] : RIGHT = " + right_label)
        print("[5] : FAST LEFT = " + fast_left_label)
        print("[6] : FAST RIGHT = " + fast_right_label)

        print("")
        for i in range(max_string_length):
            print("=", end="")
        print("\n", end="")
        print("[CTRL+W : Close Control-Setter]")

        user_input = get_key()

        if user_input == "1" or user_input == b'1':
            set_control(max_string_length, "UP", up_label)
        elif user_input == "2" or user_input == b'2':
            set_control(max_string_length, "DOWN", down_label)
        elif user_input == "3" or user_input == b'3':
            set_control(max_string_length, "LEFT", left_label)
        elif user_input == "4" or user_input == b'4':
            set_control(max_string_length, "RIGHT", right_label)
        elif user_input == "5" or user_input == b'5':
            set_control(max_string_length, "FAST LEFT", fast_left_label)
        elif user_input == "6" or user_input == b'6':
            set_control(max_string_length, "FAST RIGHT", fast_right_label)
        elif user_input == "CTRL+w":
            clear_terminal()
            break
