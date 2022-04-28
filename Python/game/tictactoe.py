class TicTacToe: 
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

    def __init__(self, winCount, width, height):
        self.__winCount = winCount
        self.__width = width
        self.__height = height
        self.__gameState = self.__gameStateEnum["PLAYING"]
        self.__boardState = [[0 for x in range(self.__width)] for y in range(self.__height)]

    def getBoardState(self):
        return self.__boardState

    def getGameState(self):
        return self.__gameState

    def getCurrPlayer(self):
        return self.__currPlayer

    def clickBlock(self, column, row):
        if self.__boardState[column][row] == self.__boardStateEnum["EMPTY"]:
            self.__boardState[column][row] = self.__currPlayer
            self.__gameState = self.__boardCondition(self.__boardState)
            self.__currPlayer = -self.__currPlayer
            return True
        return False

    def __boardCondition(self, state):
        def isDraw():
            for column in range(len(state)):
                for row in range(len(state[0])):
                    if state[column][row] == 0:
                        return self.__gameStateEnum["PLAYING"]
            return self.__gameStateEnum["DRAW"]

        def isHorizontalWin():
            for row in range(len(state[0])):
                lastState = ()
                colorInARow = 0
                for col in range(len(state)):
                    blockState = state[col][row]
                    if blockState == 0:
                        lastState = blockState
                        colorInARow = 0
                    elif blockState == lastState:
                        colorInARow = colorInARow + 1
                    else:
                        colorInARow = 1
                        lastState = blockState
                    if colorInARow == self.__winCount:
                        if blockState == 1:
                            return self.__gameStateEnum["PLAYER"]
                        else:
                            return self.__gameStateEnum["KI"]
            return self.__gameStateEnum["PLAYING"]

        def isVerticalWin():
            for col in range(len(state)):
                lastState = ()
                colorInACol = 0
                for row in range(len(state[0])):
                    blockState = state[col][row]
                    if blockState == 0:
                        lastState = blockState
                        colorInACol = 0
                    elif blockState == lastState:
                        colorInACol = colorInACol + 1
                    else:
                        colorInACol = 1
                        lastState = blockState
                    if colorInACol == self.__winCount:
                        if blockState == 1:
                            return self.__gameStateEnum["PLAYER"]
                        else:
                            return self.__gameStateEnum["KI"]
            return self.__gameStateEnum["PLAYING"]

        def isDiagonalLeftWin():
            colLen = len(state)
            rowLen = len(state[0])
            for col in range(colLen):
                for row in range(rowLen):
                    if not (col <= self.__winCount - 2 or rowLen-1 - row <= self.__winCount - 2):
                        states = set()
                        for c in range(self.__winCount):
                            states.add(state[col-c][row+c])
                        if len(states) == 1 and list(states)[0] == 1:
                            return self.__gameStateEnum["PLAYER"]
                        elif len(states) == 1 and list(states)[0] == -1:
                            return self.__gameStateEnum["KI"]
            return self.__gameStateEnum["PLAYING"]

        def isDiagonalRightWin():
            colLen = len(state)
            rowLen = len(state[0])
            for col in range(colLen):
                for row in range(rowLen):
                    if not (rowLen-1 - row <= self.__winCount - 2 or colLen-1 - col <= self.__winCount - 2):
                        states = set()
                        for c in range(self.__winCount):
                            states.add(state[col+c][row+c])
                        if len(states) == 1 and list(states)[0] == 1:
                            return self.__gameStateEnum["PLAYER"]
                        elif len(states) == 1 and list(states)[0] == -1:
                            return self.__gameStateEnum["KI"]
            return self.__gameStateEnum["PLAYING"]

        states = [isHorizontalWin(), isVerticalWin(), isDiagonalLeftWin(), isDiagonalRightWin(), isDraw()]
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
        if judgedState == self.__gameStateEnum["DRAW"]:
            return -50

        colLen = len(state)
        rowLen = len(state[0])
        for col in range(colLen):
            for row in range(rowLen):
                if row - 1 > 0:
                    if state[col][row - 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col][row - 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1
                if row + 1 < rowLen:
                    if state[col][row + 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col][row + 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1
                if col - 1 > 0:
                    if state[col - 1][row] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col - 1][row] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1
                if col + 1 < colLen:
                    if state[col + 1][row] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col + 1][row] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1
                if row - 1 > 0 and col - 1 > 0:
                    if state[col - 1][row - 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col - 1][row - 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1
                if row + 1 > rowLen and col + 1 > colLen:
                    if state[col + 1][row + 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col + 1][row + 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1
                if row - 1 > 0 and col + 1 > colLen:
                    if state[col + 1][row - 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col + 1][row - 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1
                if row + 1 > rowLen and col - 1 > 0:
                    if state[col - 1][row + 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["PLAYER"]:
                        score += 1
                    if state[col - 1][row + 1] == self.__boardStateEnum["KI"] and state[col][row] == self.__boardStateEnum["KI"]:
                        score += 1

        return score

    def validMoves(self, state):
        blocks = []

        for col in range(len(state)):
            for row in range(len(state[0])):
                if state[col][row] == 0: blocks.append([col, row])

        return blocks

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
    ttt = TicTacToe(4, 6, 6)
    state = ttt.getGameState()
    while state == 0:
        print("Next round:")
        ttt.printState()
        column = int(input("Column: "))
        row = int(input("Row: "))
        if ttt.clickBlock(column, row):
            player = ttt.getCurrPlayer()
            state = ttt.getGameState()
            print("state: " + str(state), "player: " + str(player))
        