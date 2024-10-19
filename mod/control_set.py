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


import sys
import os


from utils.ui_util import print_top_border, print_bottom_border


debug = False


def clear_terminal():
    '''
    Clear terminal
    '''
    os.system("cls" if os.name == "nt" else "clear")


'''
Detect special keys pressed by the user
'''
if sys.platform == "win32":
    import msvcrt

    def get_key():
        while True:
            key = msvcrt.getch()
            if debug:
                print("\n\nPRESSED KEY" + str(key) + "\n\n")
            if key == b'\x17':  # Close
                return "CTRL+w"
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
            if ord(key) == 23:  # Close
                return "CTRL+w"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key


def set_control(max_string_length, control, label):
    new_key = ""
    while True:
        clear_terminal()
        title = "CHANGING CONTROL " + control
        print_top_border(max_string_length, title)
        
        # PRINT
        print("\n\n")
        print("To remap this navigation key, press Ctrl and then any key...")
        print("")
        print("CURRENT KEY: " + label)
        if new_key == "":
            print("\n\n")
        else:
            print("NEWER KEY:   " + new_key)
            print("\n")

        print_bottom_border(max_string_length, "[CTRL+W : End remapping]");

        user_input = get_key()
        if user_input == "CTRL+w":
            break


def set_controls(max_string_length):
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

        print("")
        for i in range(max_string_length):
            print("=", end="")
        print("\n", end="")
        print("[CTRL+W : Close Control-Setter]")

        user_input = get_key()

        if user_input == "1":
            set_control(max_string_length, "UP", up_label)
        elif user_input == "2":
            set_control(max_string_length, "DOWN", down_label)
        elif user_input == "3":
            set_control(max_string_length, "LEFT", left_label)
        elif user_input == "3":
            set_control(max_string_length, "RIGHT", right_label)
        elif user_input == "CTRL+w":
            clear_terminal()
            break