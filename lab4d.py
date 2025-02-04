#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_string):
    """
    This function accepts a string as input and returns the first five characters of the string.
    """
    return input_string[:5]

def last_seven(input_string):
    """
    This function accepts a string as input and returns the last seven characters of the string.
    """
    return input_string[-7:]

def middle_number(input_number):
    """
    This function accepts a number as input, converts it to a string, 
    and returns the second and third characters of that string.
    """
    str_num = str(input_number)
    # We can slice the string from index 1 to index 3 to get the second and third characters
    return str_num[1:3]

def first_three_last_three(str1, str2):
    """
    This function accepts two strings as input and returns a string that starts 
    with the first three characters of the first string and ends with the last three characters of the second string.
    """
    return str1[:3] + str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))                # Will output 'Hello'
    print(first_five(str2))                # Will output 'Senec'
    print(last_seven(str1))                # Will output 'World!!'
    print(last_seven(str2))                # Will output 'College'
    print(middle_number(num1))             # Will output '50'
    print(middle_number(num2))             # Will output '.5'
    print(first_three_last_three(str1, str2))  # Will output 'Helege'
    print(first_three_last_three(str2, str1))  # Will output 'Send!!'
