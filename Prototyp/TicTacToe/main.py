import pygame
from minimax import minimax

class TicTacToe: 

    SIZE = 6
    BLOCK_SIZE = 50
    BLOCK_PADDING = 5
    CHIP_COLOR = {1: (255, 0, 0), -1: (255, 0, 255)} 
    BOARD_COLOR = (255,255,255)
    PLAYER = 1
    WIN_COUNT = 4
    STATES_GAME = {
        "DRAW": -1,
        "NOBODY": 0,
        "PLAYER": 1,
        "KI": 2,
    }

    def __init__(self, screen):
        self.STATE_GAME = self.STATES_GAME["NOBODY"]
        self.OPTICAL_BOARD = [[0 for x in range(self.SIZE)] for y in range(self.SIZE)]
        self.STATE_BOARD = [[0 for x in range(self.SIZE)] for y in range(self.SIZE)]

        pygame.init()
        self.SCREEN = screen
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = screen.get_size()
        
        self.SCREEN.fill((31, 31, 31))
        self.drawBoard();
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # or self.isGameOver():
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.handleClickEvent(event):
                        winnerState = self.boardCondition(self.STATE_BOARD)
                        if winnerState == self.STATES_GAME["DRAW"]:
                            self.STATE_GAME = winnerState
                            print('Unentschieden!')
                        elif winnerState == self.STATES_GAME["PLAYER"]:
                            self.STATE_GAME = winnerState
                            print('Der/Die SpielerIn hat gewonnen!')
                        elif winnerState == self.STATES_GAME["KI"]:
                            self.STATE_GAME = winnerState
                            print('Die KI hat gewonnen!')
                        self.PLAYER = -self.PLAYER
                        print(minimax(self, self.STATE_BOARD, 2, self.PLAYER))
            pygame.display.flip()

        print("Exit program")
        pygame.quit()

    def __drawBlock(self, color, posX, posY):
        fieldSize = (self.BLOCK_SIZE + self.BLOCK_PADDING) * self.SIZE - self.BLOCK_PADDING
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldSize / 2)
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldSize / 2)
        return pygame.draw.rect(self.SCREEN, color, (offsetX + (posX * (self.BLOCK_SIZE + self.BLOCK_PADDING)), offsetY + (posY * (self.BLOCK_SIZE + self.BLOCK_PADDING)), self.BLOCK_SIZE, self.BLOCK_SIZE))

    def drawBoard(self):
        fieldSize = (self.BLOCK_SIZE + self.BLOCK_PADDING) * self.SIZE - self.BLOCK_PADDING
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldSize / 2) - self.BLOCK_PADDING
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldSize / 2) - self.BLOCK_PADDING
        pygame.draw.rect(self.SCREEN, (80, 80, 80), (offsetX, offsetY, fieldSize + 2 * self.BLOCK_PADDING, fieldSize + 2 * self.BLOCK_PADDING))

        for column in range(len(self.OPTICAL_BOARD)):
            for block in range(len(self.OPTICAL_BOARD[0])):
                self.OPTICAL_BOARD[column][block] = self.__drawBlock(self.BOARD_COLOR, column, block)

    def __drawChip(self, column, block):
        self.OPTICAL_BOARD[column][block] = self.__drawBlock(self.CHIP_COLOR[self.PLAYER], column, block)
        self.STATE_BOARD[column][block] = self.PLAYER

    def handleClickEvent(self, event):
        for column in range(len(self.OPTICAL_BOARD)):
            for block in range(len(self.OPTICAL_BOARD)):
                if pygame.Rect.collidepoint(self.OPTICAL_BOARD[column][block], event.pos):
                    if self.STATE_BOARD[column][block] == 0:
                        self.__drawChip(column, block)
                        return True
                    return False

    def boardCondition(self, state):
        def isDraw():
            for column in range(len(state)):
                for block in range(len(state[0])):
                    if state[column][block] == 0:
                        return self.STATES_GAME["NOBODY"]
            return self.STATES_GAME["DRAW"]

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
                    if colorInARow == self.WIN_COUNT:
                        if blockState == 1:
                            return self.STATES_GAME["PLAYER"]
                        else:
                            return self.STATES_GAME["KI"]
            return self.STATES_GAME["NOBODY"]

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
                    if colorInACol == self.WIN_COUNT:
                        if blockState == 1:
                            return self.STATES_GAME["PLAYER"]
                        else:
                            return self.STATES_GAME["KI"]
            return self.STATES_GAME["NOBODY"]

        def isDiagonalLeftWin():
            colLen = len(state)
            rowLen = len(state[0])
            for col in range(colLen):
                for row in range(rowLen):
                    if not (col <= self.WIN_COUNT - 2 or rowLen-1 - row <= self.WIN_COUNT - 2):
                        states = set()
                        for c in range(self.WIN_COUNT):
                            states.add(state[col-c][row+c])
                        if len(states) == 1 and list(states)[0] == 1:
                            return self.STATES_GAME["PLAYER"]
                        elif len(states) == 1 and list(states)[0] == -1:
                            return self.STATES_GAME["KI"]
            return self.STATES_GAME["NOBODY"]

        def isDiagonalRightWin():
            colLen = len(state)
            rowLen = len(state[0])
            for col in range(colLen):
                for row in range(rowLen):
                    if not (rowLen-1 - row <= self.WIN_COUNT - 2 or colLen-1 - col <= self.WIN_COUNT - 2):
                        states = set()
                        for c in range(self.WIN_COUNT):
                            states.add(state[col+c][row+c])
                        if len(states) == 1 and list(states)[0] == 1:
                            return self.STATES_GAME["PLAYER"]
                        elif len(states) == 1 and list(states)[0] == -1:
                            return self.STATES_GAME["KI"]
            return self.STATES_GAME["NOBODY"]

        states = [isDraw(), isHorizontalWin(), isVerticalWin(), isDiagonalLeftWin(), isDiagonalRightWin()]
        for state in states:
            if state != self.STATES_GAME["NOBODY"]:
                return state
        return self.STATES_GAME["NOBODY"]

    def isGameOver(self, state):
        return not (self.boardCondition(state) == self.STATES_GAME["NOBODY"])
        
    def judgeMove(self, state):
        judgedState = self.boardCondition(state)
        if judgedState == self.STATES_GAME["PLAYER"]:
            return -1
        elif judgedState == self.STATES_GAME["KI"]:
            return 1
        elif judgedState == self.STATES_GAME["DRAW"]:
            return -1
        else:
            return 0

    def emptyBlocks(self, state):
        blocks = []

        for col in range(len(state)):
            for row in range(len(state[0])):
                if state[col][row] == 0: blocks.append([col, row])

        return blocks

if __name__=="__main__":
    TicTacToe(pygame.display.set_mode((400, 400)))