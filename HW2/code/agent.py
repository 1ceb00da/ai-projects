#! /usr/bin/python

## Homework 2
## Aditya Dhulipala

from collections import namedtuple
from helper import read_input
from minimax import *
from test_states import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]
st = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]



#
s = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]
a = [(1, 2), (4, 5), (5, 4), (3, 2), (0, 3)]
#

pl = 'X'


def alpha_beta(state, player):
    pass

[task, player, cut_off_depth, state] = read_input()



### test
##print "--END--", '\n','\n'
##print 'line num 83 test fn'
##acts = get_actions (s4, 'X')

##d = {}
##for a in acts:
##    newstate = result(s4, 'X', a)
##    u = utility(newstate, 'X')
##    d[a] = u
##    #print utility(result(s4, 'X', a), 'X')
##    #print '\n -- action -- end -- '

def pa(act):
    # Remeber: Format of action = (i, j)
    # (i, j) = (1,2) , (3, 4) etc
    # i = number
    # j = letter
    # if   a = (i,j)
    # then x = ascii_lowercase[a[1]] + str(a[0])
    # now x = 'd2', 'c3' etc (add +1 to num to get 1-index based repr)
    return (str(ascii_lowercase[act[1]]) + str(act[0]+1))

def pra(s,p):
    acts = get_actions(s,p)
    print len(acts), ' -- num actions'
    print acts
    print '\n',
    for a in acts:
        ns = result(s,p,a)
        ps(s)
        print p, ' moves to ', a
        ps(ns)
        raw_input()

print 'started.... try \n', 'minimax_decision(s, "X", 1)', '\n', 'pra(s,"X")'
print 'try:'
print 'minimax_decision(tst, "X", 1)'
print 'ps(tst)'
print '\n'
print 'run:\n', 'minimax_decision(st, "X", 2)'

minimax_decision(st, 'X', 2)
