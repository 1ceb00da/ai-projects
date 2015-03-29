def get_pos(state, player):
    pos = []
    for i in range(8):
        for j in range(8):
            if state[i][j] == player:
                pos.append([i,j])
    return pos

def get_opp(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def check_up(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i - 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            i = i - 1
            if (not (0 <= i <= 7)):
                break
            if (state[i][j] == '*'):
                return (i,j)

def check_down(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i + 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            i = i + 1
            if (not (0 <= i <= 7)):
                break
            if (state[i][j] == '*'):
                return (i,j)

def check_left(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    j = j - 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            j = j - 1
            if (not (0 <= j <= 7)):
                break
            if (state[i][j] == '*'):
                return (i,j)

def check_right(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    j = j + 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            j = j + 1
            if (not (0 <= j <= 7)):
                break
            if (state[i][j] == '*'):
                return (i,j)

def check_upleft(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i - 1
    j = j - 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            i -= 1
            j -= 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (state[i][j] == '*'):
                return (i,j)

def check_upright(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    i = i - 1
    j = j + 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            i -= 1
            j += 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (state[i][j] == '*'):
                return (i,j)

def check_downleft(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)

    i += 1
    j -= 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            i += 1
            j -= 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (state[i][j] == '*'):
                return (i,j)

def check_downright(state, player, pos):
    i = pos[0]
    j = pos[1]
    opp = get_opp(player)
    
    j += 1
    i += 1
    if state[i][j] == opp:
        while (state[i][j] == opp ):
            j += 1
            i += 1
            if (not ((0 <= i <= 7) and (0 <= j <= 7))):
                break
            if (state[i][j] == '*'):
                return (i,j)


def get_moves_for_pos(state, player, pos):
    moves = set()
    for each_pos in pos:

        # Check up
        up_move = check_up(state, player, each_pos)
        # print('printing  up_moves..'), 
        # print(up_move)
        if up_move:
            moves.add(up_move)

        # check down
        down_move = check_down(state, player, each_pos)
        # print('printing  down_move..'), 
        # print(down_move)
        if down_move:
            moves.add(down_move)

        # check left
        left_move = check_left(state, player, each_pos)
        # print('printing  left_move..'), 
        # print(left_move)
        if left_move:
            moves.add(left_move)

        # check right
        right_move = check_right(state, player, each_pos)
        # print('printing  right_move..'), 
        # print(right_move)
        if right_move:
            moves.add(right_move)

        # check up-left
        upleft_move = check_upleft(state, player, each_pos)
        # print('printing  upleft_move..'), 
        # print(upleft_move)
        if upleft_move:
            moves.add(upleft_move)

        # check up-right
        upright_move = check_upright(state, player, each_pos)
        # print('printing  down_move..'), 
        # print(upright_move)
        if upright_move:
            moves.add(upright_move)

        # check down-left
        downleft_move = check_downleft(state, player, each_pos)
        # print('printing  downleft_move..'), 
        # print(downleft_move)
        if downleft_move:
            moves.add(downleft_move)

        # check down-right
        downright_move = check_downright(state, player, each_pos)
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
    state = [''] * 8
    
    # Read current state
    for i in range(8):
        state[i] = f.readline()[:8]
        
    return [task, player, cut_off_depth, state]
