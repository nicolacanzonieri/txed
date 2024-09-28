'''
JSON UTIL

Index:
- data_to_vec()
- get_data_value(
'''


from utils.char_util import its_a_letter, its_a_number
from utils.vec_util import print_vec
from utils.str_util import str_to_vec
from utils.file_util import file_to_vec, vec_to_file


def data_to_vec(path_to_data) -> list:
    '''
    Returns a vector with the elements of a JSON file.
    
    @param path_to_data: the path to a specific JSON file.

    NOTE:
    At the moment data_to_vec does not support lists in data files
    '''
    data_vec = []
    
    with open(path_to_data, "r") as data_file:
        line = data_file.read()
        vec_index = 0
        line_vec = str_to_vec(line)
        while vec_index < len(line_vec):
            line_len = len(line_vec[vec_index])
            line_index = line_len - 1
            while line_index >= 3 and vec_index < len(line_vec)-2:
                line = line_vec[vec_index]   
                if line[line_index : line_index + 1] == '"' and line[line_index-2 : line_index - 1] == ':' and line[line_index-3 : line_index - 2] == '"':
                    data_vec.append(line_vec[vec_index][line_index + 1 : line_len-2])
                    break
                line_index -= 1
            while line_index >= 3 and vec_index == len(line_vec)-2:
                line = line_vec[vec_index]   
                if line[line_index : line_index + 1] == '"' and line[line_index - 2 : line_index - 1] == ':' and line[line_index-3 : line_index - 2] == '"':
                    data_vec.append(line_vec[vec_index][line_index + 1 : line_len-1])
                    break
                line_index -= 1
            vec_index += 1
        
    return data_vec


def get_data_value(path_to_data, value_id) -> str:
    '''
    Return a string containing the value of a data value in a given row:
    
    @param "path_to_data" : a string containing the path to a .data file
    @param "value_id" : the number of the data (eg. the first value have id = 0, the second one have id = 1, ect...)
    '''
    data_vec = data_to_vec(path_to_data)
    return data_vec[value_id]