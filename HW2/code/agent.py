## Homework 2
## Aditya Dhulipala

from collections import namedtuple

def read_input():
    # Read input
    # Assign only until last 2 chars
    # to ignore \r\n - carriage return, new line
    # Use -1 if running on Unix like environment;
    # i.e. ignore only last '\n'
    
    file = open('input.txt', 'rU')
    
    task = file.readline()[:-1]
    player = file.readline()[:-1]
    cut_off_depth = file.readline()[:-1]

    # Read current state
    nodes = []
    index = num_nodes
    while index > 0:
        nodes.append(file.readline()[:-1])
        index -= 1

    return [task, player, cut_off_depth, current_state]
