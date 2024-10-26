'''
VEC UTIL

Index:
- print_vec()
- replace_tabs_with_spaces_in_list()
'''


def print_vec(vec):
    '''
    Print a python list in terminal
    
    @param "vec" : a python list
    '''
    for item in vec:
        print(item)


def replace_tabs_with_spaces_in_list(str_list, tab_size=4):
    for i in range(len(str_list)):
        str_list[i] = str_list[i].replace("\t", " " * tab_size)
    return str_list