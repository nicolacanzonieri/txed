'''
TXED PYTHON TEXT EDITOR
By Nicola Canzonieri - 2024


Index:
- update_ctrls()
- get_key()
- print_cursor()
- print_ui()
- input_handler()
- main_logic()
- start_editor()
'''

import sys
import os

from utils.data_util import get_data_value
from utils.dir_util import get_path_to
from utils.file_util import file_to_vec, vec_to_file, extend_file_vec
from utils.os_util import clear_terminal
from utils.str_util import str_to_int
from utils.ui_util import print_top_border, print_bottom_border


from mod.control_set import set_controls 


'''
GLOBAL VARIABLES
'''
var_data_path = get_path_to("data var.data")
max_string_length = str_to_int(get_data_value(var_data_path, 1))
max_file_lines = str_to_int(get_data_value(var_data_path, 2))
debug = False


'''
CONTROL VARIABLES
'''
up_ctrl = get_data_value(var_data_path, 3 if os.name == "nt" else 4)
down_ctrl = get_data_value(var_data_path, 5 if os.name == "nt" else 6)
left_ctrl = get_data_value(var_data_path, 7 if os.name == "nt" else 8)
right_ctrl = get_data_value(var_data_path, 9 if os.name == "nt" else 10)
fast_left_ctrl = get_data_value(var_data_path, 11 if os.name == "nt" else 12)
fast_right_ctrl = get_data_value(var_data_path, 13 if os.name == "nt" else 14)


def update_ctrls():
	'''
	Update current cursors by retrieving data from data file
	'''
	up_ctrl = get_data_value(var_data_path, 3 if os.name == "nt" else 4)
	down_ctrl = get_data_value(var_data_path, 5 if os.name == "nt" else 6)
	left_ctrl = get_data_value(var_data_path, 7 if os.name == "nt" else 8)
	right_ctrl = get_data_value(var_data_path, 9 if os.name == "nt" else 10)
	fast_left_ctrl = get_data_value(var_data_path, 11 if os.name == "nt" else 12)
	fast_right_ctrl = get_data_value(var_data_path, 13 if os.name == "nt" else 14)
	if os.name != "nt":
		up_ctrl = str_to_int(up_ctrl)
		down_ctrl = str_to_int(down_ctrl)
		left_ctrl = str_to_int(left_ctrl)
		right_ctrl = str_to_int(right_ctrl)
		fast_left_ctrl = str_to_int(fast_left_ctrl)
		fast_right_ctrl = str_to_int(fast_right_ctrl)


'''
Detect special keys pressed by the user
'''
if sys.platform == "win32":
	import msvcrt

	def get_key():
		while True:
			data_path = get_path_to("data var.data")
			key = msvcrt.getch()
			if debug:
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
			data_path = get_path_to("data var.data")
			key = sys.stdin.read(1)
			if debug:
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
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return key


def print_cursor(line, cursor_x):
	'''
	Print the cursor line with the cursor
	@param "line" : the string that we are modifying
	@param "cursor_x" : the cursor x position
	'''
	line_index = 0
	
	while line_index <= len(line):
		if line_index == cursor_x:
			print("^", end="")
		else:
			print(" ", end="")
		line_index += 1
	print("")


def print_ui(path_to_file, file_vec, cursor_x, cursor_y):
	'''
	Print UI
	@param "file_vec" : the list obtained from the file (file_to_vec)
	@param "cursor_x" : cursor x position
	@param "cursor_y" : cursor y position
	'''
	file_vec_index = 0

	while cursor_y >= file_vec_index + max_file_lines:
		file_vec_index += 1
	
	try:
		print_top_border(max_string_length, path_to_file)
	except:
		print("ERROR: can't print top border UI")
		
		# PRINTER
	i = 0
	while i < max_file_lines:
		if cursor_y == file_vec_index:
			is_cursor_line = True
		else:
			is_cursor_line = False

		if file_vec_index < len(file_vec):
			try:
				file_line = file_vec[file_vec_index]
				print(file_line)
			except:
				print("")

			if is_cursor_line:
				print_cursor(file_line, cursor_x)
			
		file_vec_index += 1
		i += 1
		
	print("")
	for i in range(max_string_length):
		print("=", end="")
	print("\n", end="")
	print("[CTRL+W : Close TxEd , CTRL+S : Save file , CTRL+E : Change controls , CTRL+I/J/K/L/U/O : Move]")


def input_handler(user_input, cursor_x, cursor_y, file_vec) -> tuple:
	'''
	Return a tuple containing the new cursor position after having analyzed user input
	@param user_input: string containing pressed key/combination
	@param "cursor_x" : cursor x position
	@param "cursor_y" : cursor y position
	'''
	if user_input == "CTRL+e":
		set_controls(max_string_length)
		update_ctrls()
	elif user_input == "UP":
		cursor_y -= 1
	elif user_input == "RIGHT":
		if cursor_x == len(file_vec[cursor_y]) and cursor_y < len(file_vec):
			cursor_y += 1
			cursor_x = 0
		else:
			cursor_x += 1
	elif user_input == "DOWN":
		cursor_y += 1
	elif user_input == "LEFT":
		if cursor_x == 0 and cursor_y > 0:
			cursor_y -= 1
			cursor_x = len(file_vec[cursor_y])
		else:
			cursor_x -= 1
	elif user_input == "FAST RIGHT":
		cursor_x += 5
	elif user_input == "FAST LEFT":
		cursor_x -= 5
	elif user_input == "DELETE" and cursor_x > 0:
		file_vec[cursor_y] = file_vec[cursor_y][:cursor_x-1] + file_vec[cursor_y][cursor_x:]
		cursor_x -= 1
	elif user_input == "DELETE" and cursor_x == 0 and cursor_y > 0:
		updated_file_vec = []
		index_1 = 0
		index_2 = 0
		while (index_2 < len(file_vec)):
			if index_2 != cursor_y:
				updated_file_vec.append(file_vec[index_2])
			else:
				index_1 -= 1
				merged_line = updated_file_vec[index_1] + file_vec[index_2]
				updated_file_vec[index_1] = merged_line
			index_1 += 1
			index_2 += 1
		cursor_y -= 1
		cursor_x = len(file_vec[cursor_y])
		file_vec = extend_file_vec(updated_file_vec, max_string_length)
	elif user_input == "DELETE" and cursor_x == 0 and cursor_y == 0:
		None
	elif user_input == "ENTER":
		file_vec.insert(cursor_y + 1, file_vec[cursor_y][cursor_x:])
		file_vec[cursor_y] = file_vec[cursor_y][:cursor_x]
		cursor_y += 1
	else: # User pressed a generic keyboard button (like a letter)
		file_vec[cursor_y] = file_vec[cursor_y][:cursor_x] + user_input + file_vec[cursor_y][cursor_x:]
		cursor_x += 1
	return fix_cursor_position(file_vec, cursor_x, cursor_y)


def fix_cursor_position(file_vec, cursor_x, cursor_y) -> tuple:
	'''
	Return fixed cursor position if it is not inside the text boundaries 
	@param "file_vec" : the list obtained from the file (file_to_vec)
	@param "cursor_x" : cursor x position
	@param "cursor_y" : cursor y position
	'''
	try:
		file_line = file_vec[cursor_y]
	except:
		file_line = file_vec[cursor_y - 1]
	
	if cursor_x < 0:
		cursor_x = 0
	if  cursor_x > len(file_line):
		cursor_x = len(file_line)
	if cursor_y < 0:
		cursor_y = 0
	elif cursor_y >= len(file_vec):
		cursor_y = len(file_vec) - 1
	return (file_vec, cursor_x, cursor_y)


def main_logic(path_to_file, file_vec, cursor_x, cursor_y):
	'''
	Handle the whole text editor
	@param "file_vec" : the list obtained from the file (file_to_vec)
	@param "cursor_x" : cursor x position
	@param "cursor_y" : cursor y position
	'''
	# PREPARE TO LAUNCH TXED
	clear_terminal()
	
	# MAIN LOOP
	while True:
		# PRINT USER INTERFACE
		print_ui(path_to_file, file_vec, cursor_x, cursor_y)

		# USER KEY GETTER
		try:
			user_input = get_key()
		except:
			user_input = ""
		
		if not debug:
			clear_terminal()

		# USER INPUT HANDLER
		if user_input == "CTRL+w":
			break
		elif user_input == "CTRL+s":
			vec_to_file(path_to_file, file_vec)
		else:
			input_tuple = input_handler(user_input, cursor_x, cursor_y, file_vec)
			file_vec = input_tuple[0]
			cursor_x = input_tuple[1]
			cursor_y = input_tuple[2]


def start_editor(path_to_file):
	'''
	Start the text editor by giving it the path to a specific file
	'''
	# CURSOR POSITION
	cursor_x = 0
	cursor_y = 0
	# TRANSFORM FILE TO A LIST
	file_vec = extend_file_vec(file_to_vec(path_to_file), max_string_length)
	# START MAIN LOGIC
	main_logic(path_to_file, file_vec, cursor_x, cursor_y)


def main():
	if len(sys.argv) < 2:
		print("ERROR: insufficient arguments!")
	else:
		start_editor(sys.argv[1])


main()
