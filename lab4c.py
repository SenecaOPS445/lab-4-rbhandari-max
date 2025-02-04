#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    """
    This function takes two lists: one for keys and another for values,
    combines them to create a dictionary and returns it.
    """
    dictionary = {}
    i = 0
    while i < len(keys):
        dictionary[keys[i]] = values[i]
        i += 1
    return dictionary

def shared_values(dict1, dict2):
    """
    This function accepts two dictionaries and finds all values that are shared between the two dictionaries.
    It returns a set containing ONLY values that are common in both dictionaries.
    """
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    return set1 & set2  # This returns the intersection of both sets

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)

    common = shared_values(dict_york, dict_newnham)
    print('Shared Values: ', common)
