## Homework 2
# Aditya
# MiniMax

from helper import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]

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

def cutoff(state, cut_off_depth, current_depth):
    if current_depth == cut_off_depth:
        return True
    else:
        return False

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
        if r:
            pass
            #print 'success for ', flip_each_way
    return state_copy


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
    
def max_val(state, current_depth, cut_off_depth, calling_action):
    global MAX_PLAYER
    global value_of_node
    if calling_action not in value_of_node:
        value_of_node[calling_action] = -float('inf')

    #print MAX_PLAYER, 'max pla'
    if (current_depth < cut_off_depth):
        print 'qweqweqwrqwe', pa(calling_action),current_depth,value_of_node[calling_action]

    if cutoff(state, cut_off_depth, current_depth):
        # Since we've reached the cutoff,
        # whatever state was passed here
        # was passed from the min_player
        # HENCE - Return untility for MIN_PLAYER
        util_max = utility(result(state, MAX_PLAYER, calling_action), MAX_PLAYER) 
        #value_of_node[calling_action] = utility(result(state, MAX_PLAYER, calling_action), MAX_PLAYER)
        update_node_vals(calling_action, util_max, 'keep_min')
        print '///',pa(calling_action),current_depth,value_of_node[calling_action]
        return utility(state, MIN_PLAYER)
    v = -float('inf')
    actions = get_actions(state, MAX_PLAYER) # TODO: figure out how to pass player  val
    for a in actions:
        new_val = min_val(result(state, MAX_PLAYER, a), current_depth+1, cut_off_depth, a)
        #value_of_node[a] = -1 * new_val
        print '+++',pa(calling_action),current_depth,value_of_node[a]
        v = max(v, new_val)
##    print ' change val_of_[calling_action] to v'
##    value_of_node[calling_action] = v
##    print ' ' , value_of_node, pa(calling_action), v
    update_node_vals(callin_action, new_val, 'force_update')
    return v

def min_val(state, current_depth, cut_off_depth, calling_action):
    global MIN_PLAYER
    global value_of_node
    if calling_action not in value_of_node:
        value_of_node[calling_action] = float('inf')

    #print MIN_PLAYER, 'min pl'
    if current_depth < cut_off_depth:
        print '---',pa(calling_action),current_depth,value_of_node[calling_action]
    
    if cutoff(state, cut_off_depth, current_depth):
        # Since we've reached the cutoff,
        # whatever state was passed here
        # was passed from the max_player
        # HENCE - Return untility for MAX_PLAYER
        util_min = utility(result(state, MIN_PLAYER, calling_action), MIN_PLAYER)
        #value_of_node[calling_action] = utility(result(state, MIN_PLAYER, calling_action), MIN_PLAYER)
        update_node_vals(calling_action, util_min, 'keep_max')
        print '***',pa(calling_action),current_depth,value_of_node[calling_action]
        return utility(state, MAX_PLAYER)
    
    v = float('inf')
    actions = get_actions(state, MIN_PLAYER) # TODO: figure out how to pass player val
    for a in actions:
        new_val = max_val(result(state, MIN_PLAYER, a), current_depth+1, cut_off_depth, a)
        #value_of_node[a] = -1 * new_val # multiply byt -1 because we want the value calucated as for opp_player
        print '%%%%',pa(calling_action),current_depth,value_of_node[a]
        v = min(v, new_val)
##    print ' change val_of_[calling_action] to v'
##    value_of_node[calling_action] = v
##    print ' ', value_of_node, pa(calling_action), v
    print pa(calling_action)
    import pdb; pdb.set_trace()
    update_node_vals(calling_action, new_val, 'keep_min')
    return v

def minimax_decision(state, player, cut_off_depth):
    print 'Node,Depth,Value'
    print 'Root,0,-Infinity'
    global MAX_PLAYER, MIN_PLAYER
    global value_of_node
    value_of_node = {}

    MAX_PLAYER = player
    MIN_PLAYER = get_opp(player)
    
    actions = get_actions(state, MAX_PLAYER)
    tmp = {}
    start_depth = 1

    for a in actions:
        tmp[a] = min_val(result(state, MAX_PLAYER, a), start_depth, cut_off_depth, a)
        value_of_node['root'] = tmp[a]
        #update_node_vals('root', tmp[a], 'keep_max')
        #import pdb; pdb.set_trace()
        print 'Root,0,',value_of_node['root']

    print 'tmp = ', tmp
    
    return tmp[max(tmp)]
 
