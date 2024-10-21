'''
FILE UTIL

Index:
- file_to_str()
- file_to_vec()
- vec_to_file()
- extend_file_vec()
'''


from utils.dir_util import create_file
    

def file_to_str(path_to_file) -> str:
    '''
    Return a string containing a text file located on a specified path
    
    @param "path_to_file" : a string containing the path to a file
    '''
    with open(path_to_file, "r") as file:
        file_lines = file.read()
        return file_lines


def file_to_vec(path_to_file) -> list:
    '''
    Return a list where each element is a sentence that in the file ends with the "new line feed" character.
    
    @param "path_to_file" : a string containing the path to a file
    '''
    file_line = file_to_str(path_to_file)
    file_vec = []
    sub_file_line = ""
    char_index = 0

    if file_line[len(file_line) - 1 : len(file_line)] != "\n":
        file_line += "\n"

    while char_index < len(file_line):
        if file_line[char_index : char_index + 1] != "\n":
            sub_file_line += file_line[char_index : char_index + 1]
        else:
            file_vec.append(sub_file_line)
            sub_file_line = ""
        char_index += 1
    return file_vec


def vec_to_file(path_to_file, file_vec):
    '''
    Create or overwrite a current file by rebuilding it from a file_vec
    
    @param "path_to_file" : a string containing the path to a file
    @param "file_vec" : a list containing the file' lines
    '''
    new_file_text = ""
    for line in file_vec:
        new_file_text += line + "\n"
    create_file(path_to_file, new_file_text)


def extend_file_vec(file_vec, limit) -> list:
	'''
	Returns a list of sentences extracted from the provided file, where each sentence is either shorter than 
	or equal to the specified maximum length. Sentences exceeding the limit are split into multiple elements.
	@param "file_vec" : The original list of strings representing file contents (potentially containing 
						long sentences).
	'''
	vec_index = 0
	while vec_index < len(file_vec):
		line = file_vec[vec_index]
		if len(line) > limit:
			file_vec[vec_index] = file_vec[vec_index][ : limit]
			file_vec.insert(vec_index + 1, line[limit : ])
		vec_index += 1
	return file_vec