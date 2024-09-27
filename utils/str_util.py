'''
STR UTIL

Index:
- str_to_vec()
- str_to_int()
'''


import math
    

def str_to_vec(string) -> list:
    '''
    Return a list where each element is a sentence that in the original string ends with the 
    "new line feed" character.

    @param "string" : the interested string
    '''
    str_vec = []
    sub_file_line = ""
    char_index = 0

    if string[len(string) - 1 : len(string)] != "\n":
        string += "\n"

    while char_index < len(string):
        if string[char_index : char_index + 1] != "\n":
            sub_file_line += string[char_index : char_index + 1]
        else:
            str_vec.append(sub_file_line)
            sub_file_line = ""
        char_index += 1
    return str_vec


def str_to_int(string) -> int:
    '''
    Returns the result of converting a string to an integer.
    
    @param string: A string containing only numbers.
    '''
    char = string[0]
    if len(string) > 1:
        return (ord(char) - 48) * pow(10, (len(string) - 1)) + str_to_int(string[1:])
    else:
        return (ord(char) - 48)