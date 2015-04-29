# -*- coding: utf-8 -*-
# Homework 2
# Aditya
# Alpha-Beta

from helper import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]

_my_alpha = -float('inf')
_my_beta = float('inf')

def cutoff(state, cut_off_depth, current_depth):
    if current_depth == cut_off_depth:
        return True
    else:
        return False

def get_actions(state, player):
    actions = set()
    # TODO: Write cleaner API
    # get_pos() is not necessary
    pos = get_pos(state, player)
    actions = get_moves_for_pos(state, player, pos)
    # TODO: maybe return actions after sort() - to ensure traverse order = positional order
    actions = list(actions)
    actions.sort()
    return actions

def utility(state, player):
    opp = get_opp(player)

    modifier = {}
    modifier[player] = +1
    modifier[opp] = -1

    util = 0
    
    for i in xrange(8):
        for j in xrange(8):
            if state[i][j] != '*':
                util += modifier[state[i][j]] * weights[i][j]
                
    return util

def make_copy(some_state):
    copy = [['null' for i in xrange(8)] for j in xrange(8)]
    for row in xrange(8):
        for col in xrange(8):
            copy[row][col] = some_state[row][col]
    return copy


def print_formatted(_alpha, _beta, node, depth, value):
    if value == float('inf'):
        value = 'Infinity'
    elif value == -float('inf'):
        value = '-Infinity'
    to_print = str(node) + ',' + str(depth) + ',' + str(value)
    to_print = to_print + ',' + str(_alpha) + ',' + str(_beta)
    print to_print

def result(state, player, action):
    state_copy = make_copy(state)
    directs = [flip_down, flip_downleft, flip_downright, flip_left,
               flip_right, flip_up, flip_upleft, flip_upright]
    for flip_each_way in directs:
        #print flip_each_way, 'for action', action
        r = flip_each_way(state_copy, player, action)
##        if r:
##            pass
##            #print 'success for ', flip_each_way
    return state_copy

##alpha = -float('inf')
##beta = float('inf')
##
##def terminal(state, max_player, min_player):
##    min_a = get_actions(state, min_player)
##    max_a = get_actions(state, max_player)
##
##    if len(min_a) == 0 and len(max_a) == 0:
##        return True
##    else:
##        return False
##
##def get_alpha():
##    global alpha
##    return alpha
##def get_beta():
##    global beta
##    return beta
##def set_beta(new_val):
##    global beta
##    print ' changing beta from ', beta, ' to ', new_val
##    beta = new_val
##def set_alpha(new_val):
##    global alpha
##    print ' changing alpha from ', alpha, ' to ', new_val
##    alpha = new_val
##
##def min_val(state, current_depth, cut_off, calling_action):
##
##    local_alpha = get_alpha()
##    local_beta = get_beta()
##    
##    player = MIN_PLAYER
##    print_formatted(local_alpha, local_beta, pa(calling_action), current_depth, -float('inf'))
##    
##    if cutoff(state, cut_off, current_depth):
##        return utility(state, MIN_PLAYER)
##
##    v = float('inf')
##    actions = get_actions(state, player)
##    for a in actions:
##        rs = result(state, player, a)
##        v = min(v, max_val(rs, current_depth+1, cut_off, a))
##        #print pa(calling_action), '--leaf to parent -- backward---'
##        if v < local_alpha:
##            return v
##        local_beta = min(local_beta, v)
##        ## HERE TODO: Update global alpha,beta
##        ## update glboal alpha, beta
##        ## get new_alpha,beta
##        set_beta(local_beta)
##        local_beta = get_beta()
##        
##        new_alpha = get_alpha()
##        new_beta = get_beta()
##        
##        print_formatted(new_alpha, new_beta, pa(calling_action), current_depth, -float('inf'))
##
##    return v
##    
##
##def max_val(state, current_depth, cut_off, calling_action):
##
##    local_alpha = get_alpha()
##    local_beta = get_beta()
##
##    player = MAX_PLAYER
##    print_formatted(local_alpha, local_beta, pa(calling_action), current_depth, float('inf'))
##    
##    if cutoff(state, cut_off, current_depth):
##        return utility(state, MAX_PLAYER)
##    v = -float('inf')
##    actions = get_actions(state, player)
##    for a in actions:
##        rs = result(state, player, a)
##        v = max(v, min_val(rs, current_depth+1, cut_off, a))
##
##        #print pa(calling_action), '--leaf to parent -- backward---'
##
##        if v > local_beta:
##            return v
##        local_alpha = max(local_alpha, v)
##        ## HERE TODO: Update global alpha,beta
##        ## update glboal alpha, beta
##        ## get new_alpha,beta
##
##        set_alpha(local_alpha)
##        local_alpha = get_alpha()
##        
##        new_alpha = get_alpha()
##        new_beta = get_beta()
##        
##        print_formatted(new_alpha, new_beta, pa(calling_action), current_depth, -float('inf'))
##    return v
##
##def alpha_beta_search(state, player, cut_off):
##
##    global MAX_PLAYER, MIN_PLAYER
##    
##    MAX_PLAYER = player
##    MIN_PLAYER = get_opp(player)
##    
##    current_depth = 0
##    v = max_val(state, current_depth, cut_off, 'root')
##    actions = get_actions(state, player)
##    tmp = {}
##    for a in actions:
##        tmp[pa(a)] = utility(result(state, player, a), player)
##    return tmp
##
#### OLD CODE #####

def update_node_vals(node, val, which):
    val1 = val
    val2 = value_of_node[node]
    if abs(val1) == float('inf') or abs(val2) == float('inf'):
        which = 'force_update'
    if which == 'force_update':
        value_of_node[node] = val
    elif which == 'keep_min':
        value_of_node[node] = min(val1,val2)
    elif which == 'keep_max':
        value_of_node[node] = max(val1,val2)

def min_val(state, current_depth, cut_off, calling_action, alpha, beta):
    global MIN_PLAYER
    global value_of_node
    if calling_action not in value_of_node:
        value_of_node[calling_action] = float('inf')

    if current_depth < cut_off:

        #print '-',

        print_formatted(alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])
    

    if cutoff(state, cut_off, current_depth):
        util_min = utility(result(state, MIN_PLAYER, calling_action), MIN_PLAYER)
        update_node_vals(calling_action, util_min, 'keep_max')


        #print '--',


        print_formatted(alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])
        return utility(state, MIN_PLAYER)

    v = float('inf')
    actions = get_actions(state, MIN_PLAYER)
    for a in actions:
        new_v = max_val(result(state, MIN_PLAYER, a), current_depth+1,
                        cut_off, a, alpha, beta)
        v = min(v, new_v)

        if v <= alpha:
            value_of_node[calling_action] = min(value_of_node[calling_action],value_of_node[a])

            #FIXME: beta val not updated
            # Fix:
            beta = min(beta, v)
            
            if pa(calling_action) == 'c4':
               pass #import pdb; pdb.set_trace()
            #print '---',


            print_formatted( alpha, beta,pa(calling_action),current_depth,value_of_node[calling_action])
            return v

        beta = min(beta, value_of_node[a])
        value_of_node[calling_action] = min(value_of_node[calling_action],value_of_node[a])

        #print '----',

        if (pa(calling_action) == 'c4'):
            pass#import pdb; pdb.set_trace()

        print_formatted( alpha, beta,
                         pa(calling_action),current_depth,
                         value_of_node[calling_action])
        #print '^^^^^^^ from min_val'

    return v

def max_val(state, current_depth, cut_off, calling_action, alpha, beta):
    global MAX_PLAYER
    global value_of_node
    if calling_action != 'root' and calling_action not in value_of_node:
        value_of_node[calling_action] = -float('inf')
    if (current_depth < cut_off):


        #print '#',


        print_formatted(alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])

    
    if (cutoff(state, cut_off, current_depth)):
        util_max = utility(result(state, MAX_PLAYER, calling_action), MAX_PLAYER) 
        update_node_vals(calling_action, util_max, 'keep_min')

        #print '##',
        
        print_formatted( alpha, beta,pa(calling_action),current_depth,value_of_node[calling_action])

        return utility(state, MAX_PLAYER)

    v = -float('inf')
    actions = get_actions(state, MAX_PLAYER)
    for a in actions:
        new_v = min_val(result(state, MAX_PLAYER, a), current_depth+1,
                        cut_off, a, alpha, beta)
        v = max(v, new_v)

        if v >= beta:
            value_of_node[calling_action] = max(value_of_node[calling_action],
                                                value_of_node[a])

            alpha = max(alpha, v)
            
            print '###',

            print_formatted( alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])


            return v
        #print 'alpha =max(alpha,v) = ', alpha, '=','max(',alpha,',',value_of_node[a],')'
        alpha = max(alpha, value_of_node[a])
        value_of_node[calling_action] = max(value_of_node[calling_action],value_of_node[a])


        #print '####',

        print_formatted( alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])

        #print '^^^^^^ from max_val'
    return v
        
    
def alpha_beta_search_(state, player, cut_off):
    print 'Node,Depth,Value'
    print 'Root,0,-Infinity'
    global MAX_PLAYER, MIN_PLAYER
    global value_of_node
    value_of_node = {'root':-float('inf')}

    MAX_PLAYER = player
    MIN_PLAYER = get_opp(player)
    
    actions = get_actions(state, MAX_PLAYER)
    tmp = {}
    start_depth = 0

    ninf = -float('inf')
    pinf = float('inf')

    for a in actions:
        tmp[a] = min_val(
            result(state, MAX_PLAYER, a), start_depth, cut_off, a, ninf, pinf)
        value_of_node['root'] = max(value_of_node['root'],value_of_node[a])
        print 'root,0,' + str(value_of_node['root'])
    choices = [(value_of_node[child], pa(child)) for child in actions]
    return choices


def alpha_beta_search(state, player, cut_off):
    pinf = float('inf')
    ninf = -float('inf')
    current_depth = 0
    calling_action = 'root'

    print 'Node,Depth,Value,Alpha,Beta'

    global MAX_PLAYER, MIN_PLAYER
    global value_of_node
    value_of_node = {'root':-float('inf')}

    MAX_PLAYER = player
    MIN_PLAYER = get_opp(player)

    v = max_val(state, current_depth, cut_off, calling_action, ninf, pinf)
    actions = get_actions(state, MAX_PLAYER)
    tmp = [a for a in actions if v == utility(
        result(state, MAX_PLAYER, a), MAX_PLAYER)]
    return tmp

