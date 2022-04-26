from math import inf

def minimax(game, state, depth, player):
    PLAYER = {
        "max": 1,
        "min": -1,
        "undefined": 0
    }

    if player == PLAYER["max"]:
        best = [0, 0, -inf]    #Was sagt uns die 0?
    elif player == PLAYER["min"]:
        best = [0, 0, +inf]

    if depth == 0 or game.isGameOver(state):
        score = game.judgeMove(state)
        return [0, 0, score]

    for block in game.emptyBlocks(state):
        x = block[0]
        y = block[1]
        state[x][y] = player
        score = minimax(game, state, depth-1, -player)
        state[x][y] = PLAYER["undefined"]
        score[0] = x
        score[1] = y

        if player == PLAYER["max"]:
            if score[2] > best[2]:
                best = score
        elif player == PLAYER["min"]:
            if score[2] < best[2]:
                best = score
    return best