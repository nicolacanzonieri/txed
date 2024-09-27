'''
DIR UTIL

Index:
- get_path_separator()
- get_path_to()
- get_prnt_folder()
- check()
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


def get_prnt_folder(current_path, prnt_lvl) -> str:
    '''
    Return a string containing the parent path for a given path.
    
    @param current_path: The path from which the parent folder will be extracted.
    @param prnt_lvl: The level of parent directory to retrieve.
    '''
    path_len = len(current_path)
    prnt_lvl_indx = 1
    index = path_len

    while index > 0 and prnt_lvl_indx > 0:
        if current_path[index-1 : index] == get_path_separator():
            if prnt_lvl_indx == prnt_lvl:
                return current_path[0 : index]
            else:
                prnt_lvl_indx += 1
        index -= 1
    return current_path


def check(path) -> bool:
    '''
    Return true if a certain file or directory exist in the given path
    
    @param "path" : a string containing the path to a directory or a file
    '''
    return os.path.exists(path)


def create_file(path, file_text):
    '''
    Crate a new file in the given path
    
    @param "path" : a string containing the path to the new file (this path must contain the filename with extension)
    '''
    with open(path, "w") as new_file:
        new_file.write(file_text)
        new_file.close()