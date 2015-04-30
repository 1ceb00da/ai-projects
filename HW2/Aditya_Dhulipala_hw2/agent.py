#! /usr/bin/python2.6

## Homework 2
## Aditya Dhulipala

from collections import namedtuple
from helper import *
from minimax import minimax_decision
from minimax import greedy
from alpha_beta import alpha_beta_search
from test_states import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]
st = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]



#
s = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]
a = [(1, 2), (4, 5), (5, 4), (3, 2), (0, 3)]
#

pl = 'X'
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


def write_output(result_state, log):
    next_state = [''.join(each_line) for each_line in result_state]
    with open('output.txt', 'w') as f:
        f.write('\n'.join(next_state))
        f.write('\n')
        f.write('\n'.join(log))
    f.close()


    
[task, player, cut_off_depth, state] = read_input()
#print 'INPUT'
#print '\n'.join([task, player, cut_off_depth])
#print '\n'.join([''.join(e) for e in state])

if int(task) == 1:
    result_state = greedy(state, player)
    
elif int(task) == 2:
    [result_state, traverse_log] = minimax_decision(state, player,
                                                    int(cut_off_depth))
elif int(task) == 3:
    [result_state, traverse_log] = alpha_beta_search(state, player,
                                                     int(cut_off_depth))


# ADI -- Change code to output
# to file
#print 'OUTPUT'
#print '\n'.join([''.join(e) for e in result_state])
#print '\n'.join(traverse_log)

write_output(result_state, traverse_log)

##print 'started.... try \n', 'minimax_decision(s, "X", 1)', '\n', 'pra(s,"X")'
##print 'try:'
##print 'minimax_decision(tst, "X", 1)'
##print 'ps(tst)'
##print '\n'
##print 'run:\n', 'minimax_decision(st, "X", 2)'
##print 'run:\n', 'alpha_beta_search(st, "X", 2)'
##print 'alpha_beta_search(state, player, int(cut_off_depth))'
