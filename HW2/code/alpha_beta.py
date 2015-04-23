# Homework 2
# Aditya
# Alpha-Beta

from helper import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]

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

def print_formatted(alpha, beta, node, depth, value):
    if value == float('inf'):
        value = 'Infinity'
    elif value == -float('inf'):
        value = '-Infinity'
    to_print = str(node) + ',' + str(depth) + ',' + str(value)
    to_print = to_print + ',' + str(alpha) + ',' + str(beta)
    print to_print

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
        print_formatted(alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])
    

    if cutoff(state, cut_off, current_depth):
        util_min = utility(result(state, MIN_PLAYER, calling_action), MIN_PLAYER)
        update_node_vals(calling_action, util_min, 'keep_max')
        print_formatted(alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])
        return utility(state, MAX_PLAYER)

    v = float('inf')
    actions = get_actions(state, MIN_PLAYER)
    for a in actions:
        new_v = max_val(result(state, MIN_PLAYER, a), current_depth+1,
                        cut_off, a, alpha, beta)
        value_of_node[calling_action] = min(value_of_node[calling_action],value_of_node[a])
        print_formatted( alpha, beta,pa(calling_action),current_depth,value_of_node[calling_action])
        v = min(v, new_v)

        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def max_val(state, current_depth, cut_off, calling_action, alpha, beta):
    global MAX_PLAYER
    global value_of_node
    if calling_action != 'root' and calling_action not in value_of_node:
        value_of_node[calling_action] = -float('inf')
    if (current_depth < cut_off):
        print_formatted(alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])

    
    if (cutoff(state, cut_off, current_depth)):
        util_max = utility(result(state, MAX_PLAYER, calling_action), MAX_PLAYER) 
        update_node_vals(calling_action, util_max, 'keep_min')
        print_formatted( alpha, beta,pa(calling_action),current_depth,value_of_node[calling_action])
        return utility(state, MIN_PLAYER)

    v = -float('inf')
    actions = get_actions(state, MAX_PLAYER)
    for a in actions:
        new_v = min_val(result(state, MAX_PLAYER, a), current_depth+1,
                        cut_off, a, alpha, beta)
        value_of_node[calling_action] = max(value_of_node[calling_action],value_of_node[a])
        print_formatted( alpha, beta, pa(calling_action),current_depth,value_of_node[calling_action])
        v = max(v, new_v)

        if v >= beta:
            return v
        alpha = max(alpha, v)
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

    print 'Node,Depth,Value'
    print 'Root,0,-Infinity'

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
