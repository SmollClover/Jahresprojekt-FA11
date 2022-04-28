class Bauernschach: 
    __currPlayer = 1 # 1 for Human | -1 for KI
    __gameStateEnum = {
        "PLAYING": 0,
        "PLAYER": 1,
        "KI": 2,
        "DRAW": 3,
    }
    __boardStateEnum = {
        "EMPTY": 0,
        "PLAYER": 1,
        "KI": -1
    }

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__gameState = self.__gameStateEnum["PLAYING"]
        self.__boardState = [[0 for x in range(self.__width)] for y in range(self.__height)]
        self.__selectedPiece = [False, 0, 0]

        self.__initBoard()

    def __initBoard(self):
        for col in range(len(self.__boardState)):
            for row in range(len(self.__boardState[0])):
                if col == 0:
                    self.__boardState[col][row] = self.__boardStateEnum["KI"]
                elif col == len(self.__boardState[0]) - 1:
                    self.__boardState[col][row] = self.__boardStateEnum["PLAYER"]

    def getBoardState(self):
        return self.__boardState

    def getGameState(self):
        return self.__gameState

    def getCurrPlayer(self):
        return self.__currPlayer

    def getCurrPiece(self):
        return self.__selectedPiece

    def clickBlock(self, column, row):
        if self.__selectedPiece[0] and not self.__boardState[column][row] == self.__currPlayer:
            validMoves = self.validMoves(self.__boardState, self.__selectedPiece)
            for move in validMoves:
                if column == move[0] and row == move[1]:
                    self.__boardState[column][row] = self.__currPlayer
                    self.__boardState[self.__selectedPiece[1]][self.__selectedPiece[2]] = self.__boardStateEnum["EMPTY"]
                    self.__selectedPiece[0] = False
                    self.__gameState = self.__boardCondition(self.__boardState)
                    self.__currPlayer = -self.__currPlayer
                    return True
        else:
            if self.__boardState[column][row] == self.__currPlayer:
                self.__selectedPiece = [True, column, row]
                return True
        return False

    def __boardCondition(self, state):
        def isNoPieceWin():
            playerPieces = 0
            kiPieces = 0
            for col in range(len(state)):
                for row in range(len(state[0])):
                    if state[col][row] == self.__boardStateEnum["PLAYER"]:
                        playerPieces += 1
                    elif state[col][row] == self.__boardStateEnum["KI"]:
                        kiPieces += 1

            if playerPieces == 0:
                return self.__gameStateEnum["KI"]
            elif kiPieces == 0:
                return self.__gameStateEnum["PLAYER"]

            return self.__gameStateEnum["PLAYING"]

        def isOnOponentWin():
            for col in range(len(state)):
                for row in range(len(state[0])):
                    if col == 0 and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        return self.__gameStateEnum["PLAYER"]
                    elif col == len(self.__boardState[0]) - 1 and state[col][row] == self.__boardStateEnum["KI"]:
                        return self.__gameStateEnum["KI"]
            return self.__gameStateEnum["PLAYING"]

        states = [isNoPieceWin(), isOnOponentWin()]
        for state in states:
            if state != self.__gameStateEnum["PLAYING"]:
                return state
        return self.__gameStateEnum["PLAYING"]

    def isGameOver(self, state):
        return not (self.__boardCondition(state) == self.__gameStateEnum["PLAYING"])
        
    def judgeMove(self, state):
        score = 0

        judgedState = self.__boardCondition(state)
        if judgedState == self.__gameStateEnum["PLAYER"]:
            return -100
        if judgedState == self.__gameStateEnum["KI"]:
            return 100

        playerPieces = 0
        kiPieces = 0
        
        for col in range(len(state)):
            for row in range(len(state[0])):
                if state[col][row] == self.__boardStateEnum["PLAYER"]:
                    playerPieces += 1
                    score += -(col + 1)
                elif state[col][row] == self.__boardStateEnum["KI"]:
                    kiPieces += 1
                    score += col + 1

        score += kiPieces
        score += playerPieces

        return score

    def validMoves(self, state, selectedPiece):
        moves = []

        col = selectedPiece[1]
        row = selectedPiece[2]

        if state[col][row] == self.__boardStateEnum["PLAYER"]:
            if col - 1 >= 0:
                if state[col - 1][row] == self.__boardStateEnum["EMPTY"]:
                    moves.append([col - 1, row])
            
            if col - 1 >= 0 and row - 1 >= 0:
                if state[col - 1][row - 1] == self.__boardStateEnum["KI"]:
                    moves.append([col - 1, row - 1])
            
            if col - 1 >= 0 and row + 1 < len(state):
                if state[col - 1][row + 1] == self.__boardStateEnum["KI"]:
                    moves.append([col - 1, row + 1])
        elif state[col][row] == self.__boardStateEnum["KI"]:
            if col + 1 < len(state):
                if state[col + 1][row] == self.__boardStateEnum["EMPTY"]:
                    moves.append([col + 1, row])

            if col + 1 < len(state) and row - 1 > 0:
                if state[col - 1][row - 1] == self.__boardStateEnum["PLAYER"]:
                    moves.append([col + 1, row - 1])
            
            if col + 1 < len(state) and row + 1 < len(state):
                if state[col - 1][row + 1] == self.__boardStateEnum["PLAYER"]:
                    moves.append([col + 1, row + 1])

        return moves

    def printState(self):
        for col in range(len(self.__boardState)):
            s = ""
            for row in range(len(self.__boardState[0])):
                if self.__boardState[col][row] == self.__boardStateEnum["PLAYER"]:
                    icon = "P"
                elif self.__boardState[col][row] == self.__boardStateEnum["KI"]:
                    icon = "K"
                else:
                    icon = "-"
                s = s + icon + " "
            print(s)
        print("-----------")
                

if __name__=="__main__":
    bs = Bauernschach(6, 6)
    state = bs.getGameState()
    while state == 0:
        bs.printState()

        if bs.getCurrPiece()[0]:
            print("Select Position")
        else:
            print("Select Piece")

        column = int(input("Column: "))
        row = int(input("Row: "))
        if bs.clickBlock(column, row):
            player = bs.getCurrPlayer()
            state = bs.getGameState()
            piece = bs.getCurrPiece()
            print("state: " + str(state), "player: " + str(player), "piece: " + str(piece))
        