'''
CHAR UTIL

Index:
- its_a_letter()
- its_a_number()
'''


def its_a_letter(char) -> bool:
    '''
    Return true if the given char is a letter
    '''
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'


def its_a_number(char) -> bool:
    '''
    Return true if the given char is a number
    '''
    return '0' <= char <= '9'

