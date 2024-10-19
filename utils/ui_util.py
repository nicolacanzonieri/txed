def print_top_border(max_string_length, title):
	print(path_to_file, end="")
	for i in range(max_string_length - len(path_to_file) - len("MAX: " + str(max_string_length))):
		print(" ", end="")
	print("MAX: " + str(max_string_length))
	for i in range(max_string_length):
		print("=", end="")
	print("\n", end="")