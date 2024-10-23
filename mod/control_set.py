'''
CONTROL SETTER

Index:
- set_label_and_quit()
- set_control()
- set_controls()
'''


import sys
import os


from utils.data_util import edit_data, get_data_value
from utils.dir_util import get_path_to
from utils.os_util import clear_terminal
from utils.ui_util import print_top_border, print_bottom_border


up_label = ""
down_label = ""
left_label = ""
right_label = ""
fast_right_label = ""
fast_left_label = ""


debug = False


'''
Detect special keys pressed by the user
'''
if sys.platform == "win32":
    import msvcrt

    def get_key():
        while True:
            key = msvcrt.getch()
            og_key = key
            if debug:
                print("\n\nPRESSED KEY: [" + str(key) + ", " + str(og_key) + "]" + "\n\n")
            if key == b'\x05':    # Control-Setter
                return ["CTRL+e", og_key]
            elif key == b'\x17':  # Close
                return ["CTRL+w", og_key]
            elif key == b"\x08":  # Backspace/Delete key
                return ["DELETE", og_key]
            elif key == b"\xe0":  # Cancel key (NOT SUPPORTED TODO!)
                return ["CANCEL", og_key]
            elif key == b'\x13':  # Save
                return ["CTRL+s", og_key]
            elif key == b'\r':    # Enter, Newline
                return ["ENTER", og_key]
            return [key.decode("utf-8"), og_key]

else:
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
            og_key = ord(key)
            if debug:
                print("\n\nPRESSED KEY: [" + str(ord(key)) + ", " + str(og_key) + "]" + "\n\n")
            if ord(key) == 5:     # Control-Setter
                return ["CTRL+e", og_key]
            if ord(key) == 23:    # Close
                return ["CTRL+w", og_key]
            elif ord(key) == 19:  # Save
                return ["CTRL+s", og_key]
            elif ord(key) == 127: # Backspace/Delete key
                return ["DELETE", og_key]
            elif ord(key) == 126: # Cancel key (NOT SUPPORTED TODO!)
                return ["CANCEL", og_key]
            elif ord(key) == 13:  # Enter, Newline
                return ["ENTER", og_key]
            return [key, og_key]
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def set_label_and_quit(max_string_length, data_value, data_row, data_label_row):
    '''
    Set the label for a specific control

    @param "max_string_length" : Integer with the maximum string length allowed
    @param "data_value" : TODO!
    @param "data_row" : TODO!
    @param "data_label_row" : TODO!
    '''

    new_label = ""
    while True:
        clear_terminal()
        print_top_border(max_string_length, "SET LABEL")
        print('Insert the label for the new command (for example "CTRL+U"): ' + str(new_label))
        print("\n")
        print_bottom_border(max_string_length, "[CTRL+W : Quit (without saving) , ENTER : Save and Quit]")

        user_input = get_key()

        if user_input[0] == "ENTER":
            new_label = '"' + str(new_label) + '"'
            edit_data(get_path_to("data var.data"), data_row, data_value)
            edit_data(get_path_to("data var.data"), data_label_row, new_label)
            break
        elif user_input[0] == "CTRL+w":
            break
        elif user_input[0] == "DELETE":
            new_label = new_label[:len(new_label)-1]
        elif user_input[0] == "CANCEL":
            None
        elif user_input[0] == "CTRL+s":
            None
        elif user_input[0] == "CTRL+e":
            None
        else:
            new_label += user_input[0]


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
        print("CURRENT LABEL:  " + label)
        if new_key == "" and warning_msg == "":
            print("\n\n")
        elif new_key != "" and warning_msg == "":
            print("NEWER KEY CODE: " + str(new_key))
            print("\n")
        elif new_key == "" and warning_msg != "":
            print(warning_msg)
            print("\n")

        print_bottom_border(max_string_length, "[CTRL+W : End remapping , CTRL+S : Save current key]")

        user_input = get_key()

        # DETECT DATA ROW
        if control == "UP":
            data_row = 4 if os.name == "nt" else 5
            data_label_row = 16
        elif control == "DOWN":
            data_row = 6 if os.name == "nt" else 7
            data_label_row = 17
        elif control == "LEFT":
            data_row = 8 if os.name == "nt" else 9
            data_label_row = 18
        elif control == "RIGHT":
            data_row = 10 if os.name == "nt" else 11
            data_label_row = 19
        elif control == "FAST LEFT":
            data_row = 12 if os.name == "nt" else 13
            data_label_row = 20
        elif control == "FAST RIGHT":
            data_row = 14 if os.name == "nt" else 15
            data_label_row = 21

        # SET UI MESSAGES
        if user_input[0] == "CTRL+w":
            break
        elif user_input[0] == "CTRL+s":
            data_value = '"' + str(new_key) + '"'
            set_label_and_quit(max_string_length, data_value, data_row, data_label_row)
            break
        elif user_input[0]== "CTRL+e":
            warning_msg = "CTRL+E is already used by the control setter!"
            new_key = ""
        elif user_input[0] == "DELETE":
            warning_msg = "DELETE is a priority key!"
            new_key = ""
        elif user_input[0] == "CANCEL":
            warning_msg = "CANCEL is a priority key!"
            new_key = ""
        elif user_input[0] == "ENTER":
            warning_msg = "ENTER is a priority key!"
            new_key = ""
        else:
            warning_msg = ""
            new_key = user_input[1] if os.name == "nt" else user_input[1]


def set_controls(max_string_length):
    '''
    Start Control-Setter

    @param "max_string_length" : Integer with the maximum string length allowed
    '''

    title = "CONTROL-SETTER"
    while True:
        up_label = get_data_value(get_path_to("data var.data"), 15)
        down_label = get_data_value(get_path_to("data var.data"), 16)
        left_label = get_data_value(get_path_to("data var.data"), 17)
        right_label = get_data_value(get_path_to("data var.data"), 18)
        fast_left_label = get_data_value(get_path_to("data var.data"), 19)
        fast_right_label = get_data_value(get_path_to("data var.data"), 20)

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

        if user_input[0] == "1" or user_input[0] == b'1':
            set_control(max_string_length, "UP", up_label)
        elif user_input[0] == "2" or user_input[0] == b'2':
            set_control(max_string_length, "DOWN", down_label)
        elif user_input[0] == "3" or user_input[0] == b'3':
            set_control(max_string_length, "LEFT", left_label)
        elif user_input[0] == "4" or user_input[0] == b'4':
            set_control(max_string_length, "RIGHT", right_label)
        elif user_input[0] == "5" or user_input[0] == b'5':
            set_control(max_string_length, "FAST LEFT", fast_left_label)
        elif user_input[0] == "6" or user_input[0] == b'6':
            set_control(max_string_length, "FAST RIGHT", fast_right_label)
        elif user_input[0] == "CTRL+w":
            clear_terminal()
            break
