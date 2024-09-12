#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for elements in sorted(a_dictionary):
        print("{}: {}".format(elements, a_dictionary[elements]))
