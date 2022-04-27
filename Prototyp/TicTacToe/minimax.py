from math import inf

def minimax(game, state, depth, player):
    PLAYER = {
        "min": 1,
        "max": -1,
        "undefined": 0
    }

    if player == PLAYER["max"]:
        best = [0, 0, -inf]
    elif player == PLAYER["min"]:
        best = [0, 0, +inf]

    if depth == 0 or game.isGameOver(state):
        score = game.judgeMove(state)
        return [0, 0, score]

    for move in game.validMoves(state):
        col = move[0]
        row = move[1]
        state[col][row] = player
        score = minimax(game, state, depth-1, -player)
        state[col][row] = PLAYER["undefined"]
        score[0] = col
        score[1] = row

        if player == PLAYER["max"]:
            if score[2] > best[2]:
                best = score
        elif player == PLAYER["min"]:
            if score[2] < best[2]:
                best = score
    return best