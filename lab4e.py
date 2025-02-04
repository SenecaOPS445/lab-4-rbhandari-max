#!/usr/bin/env python3
# Author ID: rbhandari17@myseneca.ca

def is_digits(sobj):
    """
    This function takes a string as input and checks if all characters in the string are digits.
    It returns True if all characters are digits, otherwise False.
    """
    for char in sobj:
        if char not in '0123456789':  # Check if each character is a digit
            return False
    return True

if __name__ == '__main__':
    # Testing list of strings
    test_list = ['x3058', '3058', '8503x', '8503']
    
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
