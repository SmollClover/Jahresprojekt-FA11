import pygame

class TicTacToe: 

    SIZE = 6
    WINDOW_WIDTH = 400
    WINDOW_HEIGTH = 400
    BLOCK_SIZE = 50
    BLOCK_PADDING = 5
    CHIP_COLOR = {True: (255, 0, 0), False: (255, 0, 255)} 
    BOARD_COLOR = (255,255,255)
    PLAYER = True
    BOARD=[]
    WIN_COUNT = 4
    STATE = {
        "DRAW": -1,
        "NOBODY": 0,
        "PLAYER": 1,
        "KI": 2,
    }

    def __init__(self):
        self.BOARD = [[0 for x in range(self.SIZE)] for y in range(self.SIZE)]
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGTH))
        self.SCREEN.fill((31, 31, 31))
        self.drawBoard();    
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handleClickEvent(event)
                    winnerState = self.boardCondition()
                    if winnerState == self.STATE["DRAW"]:
                        print('Unentschieden!')
                    elif winnerState == self.STATE["PLAYER"]:
                        print('Der/Die SpielerIn hat gewonnen!')
                    elif winnerState == self.STATE["KI"]:
                        print('Die KI hat gewonnen!')
            pygame.display.flip()

        print("Exit program")
        pygame.quit()

    def __drawBlock(self, color, posX, posY):
        fieldSize = (self.BLOCK_SIZE + self.BLOCK_PADDING) * self.SIZE - self.BLOCK_PADDING
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldSize / 2)
        offsetY = int(self.WINDOW_HEIGTH / 2 - fieldSize / 2)
        return (pygame.draw.rect(self.SCREEN, color, (offsetX + (posX * (self.BLOCK_SIZE + self.BLOCK_PADDING)), offsetY + (posY * (self.BLOCK_SIZE + self.BLOCK_PADDING)), self.BLOCK_SIZE, self.BLOCK_SIZE)), color)

    def drawBoard(self):
        fieldSize = (self.BLOCK_SIZE + self.BLOCK_PADDING) * self.SIZE - self.BLOCK_PADDING
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldSize / 2) - self.BLOCK_PADDING
        offsetY = int(self.WINDOW_HEIGTH / 2 - fieldSize / 2) - self.BLOCK_PADDING
        pygame.draw.rect(self.SCREEN, (80, 80, 80), (offsetX, offsetY, fieldSize + 2 * self.BLOCK_PADDING, fieldSize + 2 * self.BLOCK_PADDING))

        for column in range(len(self.BOARD)):
            for block in range(len(self.BOARD[0])):
                self.BOARD[column][block] = self.__drawBlock(self.BOARD_COLOR, column, block)

    def __drawChip(self, column, block):
        self.BOARD[column][block] = self.__drawBlock(self.CHIP_COLOR[self.PLAYER], column, block)

    def handleClickEvent(self, event):
        for column in range(len(self.BOARD)):
            for block in range(len(self.BOARD[0])):
                if pygame.Rect.collidepoint(self.BOARD[column][block][0], event.pos):
                    if self.BOARD[column][block][1] == self.BOARD_COLOR:
                        self.__drawChip(column, block)
                        self.PLAYER = not self.PLAYER
                    return

    def boardCondition(self):
        def isDraw():
            for column in range(len(self.BOARD)):
                for block in range(len(self.BOARD[0])):
                    if self.BOARD[column][block][1] == self.BOARD_COLOR:
                        return self.STATE["NOBODY"]
            return self.STATE["DRAW"]

        def isHorizontalWin():
            for row in range(len(self.BOARD[0])):
                lastColor = ()
                colorInARow = 0
                for col in range(len(self.BOARD)):
                    blockColor = self.BOARD[col][row][1]
                    if blockColor == self.BOARD_COLOR:
                        lastColor = blockColor
                        colorInARow = 0
                    elif blockColor == lastColor:
                        colorInARow = colorInARow + 1
                    else:
                        colorInARow = 1
                        lastColor = blockColor
                    if colorInARow == self.WIN_COUNT:
                        if blockColor == self.CHIP_COLOR[True]:
                            print("horizontal")
                            return self.STATE["PLAYER"]
                        else:
                            print("horizontal")
                            return self.STATE["KI"]
            return self.STATE["NOBODY"]

        def isVerticalWin():
            for col in range(len(self.BOARD)):
                lastColor = ()
                colorInACol = 0
                for row in range(len(self.BOARD[0])):
                    blockColor = self.BOARD[col][row][1]
                    if blockColor == self.BOARD_COLOR:
                        lastColor = blockColor
                        colorInACol = 0
                    elif blockColor == lastColor:
                        colorInACol = colorInACol + 1
                    else:
                        colorInACol = 1
                        lastColor = blockColor
                    if colorInACol == self.WIN_COUNT:
                        if blockColor == self.CHIP_COLOR[True]:
                            print("vertical")
                            return self.STATE["PLAYER"]
                        else:
                            print("vertical")
                            return self.STATE["KI"]
            return self.STATE["NOBODY"]

        def isDiagonalLeftWin():
            colLen = len(self.BOARD)
            rowLen = len(self.BOARD[0])
            for col in range(colLen):
                for row in range(rowLen):
                    if not (col <= self.WIN_COUNT - 2 or rowLen-1 - row <= self.WIN_COUNT - 2):
                        color = set()
                        for c in range(self.WIN_COUNT):
                            color.add(self.BOARD[col-c][row+c][1])
                        if len(color) == 1 and list(color)[0] == self.CHIP_COLOR[True]:
                            print("diagonallinks")
                            return self.STATE["PLAYER"]
                        elif len(color) == 1 and list(color)[0] == self.CHIP_COLOR[False]:
                            print("diagonallinks")
                            return self.STATE["KI"]
            return self.STATE["NOBODY"]

        def isDiagonalRightWin():
            colLen = len(self.BOARD)
            rowLen = len(self.BOARD[0])
            for col in range(colLen):
                for row in range(rowLen):
                    if not (rowLen-1 - row <= self.WIN_COUNT - 2 or colLen-1 - col <= self.WIN_COUNT - 2):
                        color = set()
                        for c in range(self.WIN_COUNT):
                            color.add(self.BOARD[col+c][row+c][1])
                        if len(color) == 1 and list(color)[0] == self.CHIP_COLOR[True]:
                            print("diagonalrechts")
                            return self.STATE["PLAYER"]
                        elif len(color) == 1 and list(color)[0] == self.CHIP_COLOR[False]:
                            print("diagonalrechts")
                            return self.STATE["KI"]
            return self.STATE["NOBODY"]

        states = [isDraw(), isHorizontalWin(), isVerticalWin(), isDiagonalLeftWin(), isDiagonalRightWin()]
        for state in states:
            if state != self.STATE["NOBODY"]:
                return state
        return self.STATE["NOBODY"]

if __name__=="__main__":
    TicTacToe()