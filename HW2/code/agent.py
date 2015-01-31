## Homework 2
## Aditya Dhulipala

from collections import namedtuple
from helper import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]
st = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]



#
s = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]

#

pl = 'X'

def ps(s):
    for each in s:
        print each

def get_actions(state, player):
    actions = set()
    # TODO: Write cleaner API
    # get_pos() is not necessary
    pos = get_pos(state, player)
    actions = get_moves_for_pos(state, player, pos)
    return actions

def cutoff(state, depth):
    global cut_off_depth
    if depth == cut_off_depth:
        return True
    else:
        return False

def result(state, action):
    state = state[:]
    print 'result', state, action
    
def min_val(state):
    if cutoff(state, depth):
        return eval_(state)
    pass

def minimax_decision(state, player):
    actions = get_actions(state, player)
    tmp = {}
    for a in actions:
        tmp[min_val(result(state, a))] = a
    return tmp[max(tmp)]
        
    
def alpha_beta(state, player):
    pass

[task, player, cut_off_depth, state] = read_input()
