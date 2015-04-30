

def ps(s):
    for each in s:
        print each

from string import ascii_lowercase
def pa(act):
    # Remeber: Format of action = (i, j)
    # (i, j) = (1,2) , (3, 4) etc
    # i = number
    # j = letter
    # if   a = (i,j)
    # then x = ascii_lowercase[a[1]] + str(a[0])
    # now x = 'd2', 'c3' etc (add +1 to num to get 1-index based repr)
    if act == 'root':
        return act
    return (str(ascii_lowercase[act[1]]) + str(act[0]+1))



# Flip opponent for valid moves functions
def flip_right(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]
    flip_result = False
    if j >= 7:
        return flip_result
    
    j = j + 1
    opp = get_opp(player)
    flip_end_pos = ()
    
    if _state[i][j] == opp:
        while _state[i][j] == opp:
            j = j + 1
            if (not (0 <= j <= 7)):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i,j)
                break
    if flip_end_pos:
        #_state = _state[:]
        for _j in xrange(flip_start_pos[1], flip_end_pos[1]+1):
            _state[i][_j] = player
        flip_result = True
    return flip_result

def flip_downleft(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]
    flip_result = False

    if i >= 7 or j <= 0:
        return flip_result
    
    opp = get_opp(player)

    i += 1
    j -= 1
    flip_end_pos = ()

    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i += 1
            j -= 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i,j)
                break
    if flip_end_pos:
        i = flip_start_pos[0]
        j = flip_start_pos[1]
        while flip_start_pos[0] <= i <= flip_end_pos[0] and flip_end_pos[1] <= j <= flip_start_pos[1]:
            _state[i][j] = player
            i += 1
            j -= 1
        flip_result = True
    return flip_result

    

def flip_downright(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]
    flip_result = False

    if i >= 7 or j >= 7:
        return flip_result
        
    opp = get_opp(player)
    
    j += 1
    i += 1
    flip_end_pos = ()

    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            j += 1
            i += 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i,j)
                break
    if flip_end_pos:
        i = flip_start_pos[0]
        j = flip_start_pos[1]
        while flip_start_pos[0] <= i <= flip_end_pos[0] and flip_start_pos[1] <= j <= flip_end_pos[1]:
            _state[i][j] = player
            i += 1
            j += 1
        flip_result = True
    return flip_result


def flip_left(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]
    flip_result = False

    if j <= 0:
        return flip_result
    
    opp = get_opp(player)
    
    j = j - 1
    flip_end_pos = ()
    
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            j = j - 1
            if (not (0 <= j <= 7)):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i,j)
                break
    if flip_end_pos:
        for _j in xrange(flip_end_pos[1], flip_start_pos[1]+1):
            _state[i][_j] = player
        flip_result = True
    return flip_result


def flip_down(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]
    flip_result = False

    if (i >= 7):
        return flip_result
    
    opp = get_opp(player)
    
    i = i + 1
    flip_end_pos = ()
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i = i + 1
            if (not (0 <= i <= 7)):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i, j)
                break
    if flip_end_pos:
        i = flip_start_pos[0]
        
        while flip_start_pos[0] <= i <= flip_end_pos[0]:
            _state[i][j] = player
            i += 1

        for _i in xrange(flip_start_pos[0], flip_end_pos[0]+1):
            _state[_i][j] = player
        flip_result = True
    return flip_result


def flip_up(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]

    flip_result = False
    
    if i <= 0:
        return flip_result

    opp = get_opp(player)
    
    i = i - 1
    flip_end_pos = ()
    
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i = i - 1
            if (not (0 <= i <= 7)):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i,j)
                break
    if flip_end_pos:
        i = flip_start_pos[0]
        
        while flip_end_pos[0] <= i <= flip_start_pos[0]:
            _state[i][j] = player
            i -= 1
        flip_result = True
    return flip_result

def flip_upleft(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]
    flip_result = False
    
    if i <= 0 or j <= 0:
        return flip_result
    
    opp = get_opp(player)
    
    i = i - 1
    j = j - 1
    flip_end_pos = ()
    
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i -= 1
            j -= 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i,j)
                break
    if flip_end_pos:
        i = flip_start_pos[0]
        j = flip_start_pos[1]
        
        while flip_end_pos[0] <= i <= flip_start_pos[0] and flip_end_pos[1] <= j <= flip_start_pos[1]:
            _state[i][j] = player
            i -= 1
            j -= 1
        flip_result = True
    return flip_result


def flip_upright(_state, player, flip_start_pos):
    i = flip_start_pos[0]
    j = flip_start_pos[1]
    flip_result = False
    
    if i <= 0 or j >= 7:
        return flip_result
    
    opp = get_opp(player)

    i = i - 1
    j = j + 1
    flip_end_pos = ()
    
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i -= 1
            j += 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == player):
                flip_end_pos = (i,j)
                break
    if flip_end_pos:
        i = flip_start_pos[0]
        j = flip_start_pos[1]

        while flip_end_pos[0] <= i <= flip_start_pos[0] and flip_start_pos[1] <= j <= flip_end_pos[1]:
            _state[i][j] = player
            i -= 1
            j += 1
        flip_result = True
    return flip_result
         

## end

def get_pos(_state, player):
    pos = []
    for i in range(8):
        for j in range(8):
            if _state[i][j] == player:
                pos.append([i,j])
    return pos

def get_opp(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def check_up(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i - 1

    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i = i - 1
            if (not (0 <= i <= 7)):
                break
            if (_state[i][j] == '*'):
                return (i,j)

def check_down(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i + 1
    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i = i + 1
            if (not (0 <= i <= 7)):
                break
            if (_state[i][j] == '*'):
                return (i,j)

def check_left(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    j = j - 1
    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            j = j - 1
            if (not (0 <= j <= 7)):
                break
            if (_state[i][j] == '*'):
                return (i,j)

def check_right(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    j = j + 1
    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            j = j + 1
            if (not (0 <= j <= 7)):
                break
            if (_state[i][j] == '*'):
                return (i,j)

def check_upleft(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i - 1
    j = j - 1
    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i -= 1
            j -= 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == '*'):
                return (i,j)

def check_upright(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i - 1
    j = j + 1
    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i -= 1
            j += 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == '*'):
                return (i,j)

def check_downleft(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)

    i += 1
    j -= 1
    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            i += 1
            j -= 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == '*'):
                return (i,j)

def check_downright(_state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    j += 1
    i += 1
    if (not ((0 <= i <= 7) and ( 0<= j <= 7)) ):
        return
    if _state[i][j] == opp:
        while (_state[i][j] == opp ):
            j += 1
            i += 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (_state[i][j] == '*'):
                return (i,j)


def get_moves_for_pos(_state, player, pos):
    moves = set()
    for each_pos in pos:

        # Check up
        up_move = check_up(_state, player, each_pos)
        # print('printing  up_moves..'), 
        # print(up_move)
        if up_move:
            moves.add(up_move)

        # check down
        down_move = check_down(_state, player, each_pos)
        # print('printing  down_move..'), 
        # print(down_move)
        if down_move:
            moves.add(down_move)

        # check left
        left_move = check_left(_state, player, each_pos)
        # print('printing  left_move..'), 
        # print(left_move)
        if left_move:
            moves.add(left_move)

        # check right
        right_move = check_right(_state, player, each_pos)
        # print('printing  right_move..'), 
        # print(right_move)
        if right_move:
            moves.add(right_move)

        # check up-left
        upleft_move = check_upleft(_state, player, each_pos)
        # print('printing  upleft_move..'), 
        # print(upleft_move)
        if upleft_move:
            moves.add(upleft_move)

        # check up-right
        upright_move = check_upright(_state, player, each_pos)
        # print('printing  down_move..'), 
        # print(upright_move)
        if upright_move:
            moves.add(upright_move)

        # check down-left
        downleft_move = check_downleft(_state, player, each_pos)
        # print('printing  downleft_move..'), 
        # print(downleft_move)
        if downleft_move:
            moves.add(downleft_move)

        # check down-right
        downright_move = check_downright(_state, player, each_pos)
        # print('printing  downright_move..'), 
        # print(downright_move)
        if downright_move:
            moves.add(downright_move)

    return moves

def read_input():
    # Read input
    # Assign only until last 2 chars
    # to ignore \r\n - carriage return, new line
    # Use -1 if running on Unix like environment;
    # i.e. ignore only last '\n'
    
    f = open('input.txt', 'rU')
    
    task = f.readline()[:-1]
    player = f.readline()[:-1]
    cut_off_depth = f.readline()[:-1]
    _state = [''] * 8
    
    # Read current _state
    for i in range(8):
        _state[i] = f.readline()[:8]
        
    return [task, player, cut_off_depth, _state]
