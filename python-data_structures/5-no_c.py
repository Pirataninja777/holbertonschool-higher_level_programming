#!/usr/bin/python3
def no_c(my_string):
    stack = []
    for char in my_string:
        if char != 'c' and char != 'C':
            stack.append(char)
    return ''.join(stack)
