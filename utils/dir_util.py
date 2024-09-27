'''
DIR UTIL

Index:
- get_path_separator()
- get_path_to()
- create_file()
'''


import os


def get_path_separator() -> str:
    '''
    Return the path separator (str) for the current OS
    '''
    return os.sep


def get_path_to(path_to_file) -> str:
    '''
    Return the os' accepted path (str) to a specified file with the correct path separator
    
    @param "path_to_file" : a string that represent the path to a certain file with the following sintax:
                            path_to_file = "folder1 folder2 folder3 ... file"
    '''
    path_vec = path_to_file.split()
    full_path = ""

    for item in path_vec:
        full_path = full_path + get_path_separator() + item
    full_path = full_path[1:]
    return full_path


def create_file(path, file_text):
    '''
    Crate a new file in the given path
    
    @param "path" : a string containing the path to the new file (this path must contain the filename with extension)
    '''
    with open(path, "w") as new_file:
        new_file.write(file_text)
        new_file.close()