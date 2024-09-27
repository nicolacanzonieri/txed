'''
VEC UTIL

Index:
- print_vec()
- print_matrix()
- find_value_in_vec()
'''


def print_vec(vec):
    '''
    Print a python list in terminal
    
    @param "vec" : a python list
    '''
    for item in vec:
        print(item)


def print_matrix(matrix):
    '''
    Print a python matrix in terminal
    
    @param "matrix" : a python matrix
    '''
    for row in matrix:
        for item in row:
            print(item, end=", ")


def find_value_in_vec(val, vec) -> int:
    '''
    Return the index where a given value is located inside a vec
    
    @param "val" : value to find
    @param "vec" : list where to search the value
    @return "index" : the position where val is located. If val is not in vec than index = -1
    '''
    index = 0
    while index < len(vec):
        if vec[index] == val: 
            return index
        else:
            index += 1
    return -1