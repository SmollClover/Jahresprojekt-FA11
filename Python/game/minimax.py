from math import inf

class MiniMax:
    __PLAYER = {
        "min": 1,
        "max": -1,
        "undefined": 0
    }

    def __init__(self, game, state, depth, player, alpha = -inf, beta = inf):
        self.__game = game
        self.__state = state
        self.__depth = depth
        self.__player = player
        self.__alpha = alpha
        self.__beta = beta

    def calc(self):
        if self.__player == self.__PLAYER["max"]:
            best = [0, 0, self.__alpha, []]
        elif self.__player == self.__PLAYER["min"]:
            best = [0, 0, self.__beta, []]

        if self.__depth == 0 or self.__game.isGameOver(self.__state):
            score = self.__game.judgeMove(self.__state)
            return [0, 0, score, []]

        if len(self.__game.getCurrPiece()) < 2:
            for move in self.__game.validMoves(self.__state):
                col = move[0]
                row = move[1]
                self.__state[col][row] = self.__player
                score = MiniMax(self.__game, self.__state, self.__depth - 1, - self.__player, self.__alpha, self.__beta).calc()
                self.__state[col][row] = self.__PLAYER["undefined"]
                score[0] = col
                score[1] = row

                if self.__player == self.__PLAYER["max"]:
                    if score[2] > best[2]:
                        best = score
                        self.__alpha = best[2]

                        if best[2] >= self.__beta:
                            break
                elif self.__player == self.__PLAYER["min"]:
                    if score[2] < best[2]:
                        best = score
                        self.__beta = best[2]

                        if best[2] <= self.__alpha:
                            break
        else:
            for piece in self.__game.getAllPieces(self.__state, self.__player):
                for move in self.__game.validMoves(self.__state, piece):
                    col = move[0]
                    row = move[1]
                    tempCopy = self.__state[col][row]
                    self.__state[col][row] = self.__player
                    self.__state[piece[1]][piece[2]] = self.__PLAYER["undefined"]
                    score = MiniMax(self.__game, self.__state, self.__depth - 1, - self.__player, self.__alpha, self.__beta).calc()
                    self.__state[col][row] = tempCopy
                    self.__state[piece[1]][piece[2]] = self.__player
                    score[0] = col
                    score[1] = row

                    if self.__player == self.__PLAYER["max"]:
                        if score[2] > best[2]:
                            best = score
                            best[3] = piece
                            self.__alpha = best[2]

                            if best[2] >= self.__beta:
                                break
                    elif self.__player == self.__PLAYER["min"]:
                        if score[2] < best[2]:
                            best = score
                            best[3] = piece
                            self.__beta = best[2]

                            if best[2] <= self.__alpha:
                                break

        return best