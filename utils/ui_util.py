'''
DATA UTIL

Index:
- print_top_border()
- print_bottom_border()
'''


def print_top_border(max_string_length, title):
	print(title, end="")
	for i in range(max_string_length - len(title) - len("MAX: " + str(max_string_length))):
		print(" ", end="")
	print("MAX: " + str(max_string_length))
	for i in range(max_string_length):
		print("=", end="")
	print("\n", end="")


def print_bottom_border(max_string_length, title):
	for i in range(max_string_length):
            print("=", end="")
        print("\n", end="")
	print(title)