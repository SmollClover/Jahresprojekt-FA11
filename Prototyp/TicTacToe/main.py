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
                    if self.winCondition():
                        print('Gewonnen!')
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

    def winCondition(self):
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
                        return True
            return False

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
                        return True
            return False
 
        def isDiagonalLeftWin():
            colLen = len(self.BOARD)
            rowLen = len(self.BOARD[0])
            for col in range(colLen):
                for row in range(rowLen):
                    if not (col <= self.WIN_COUNT - 2 or rowLen-1 - row <= self.WIN_COUNT - 2):
                        color = set()
                        for c in range(self.WIN_COUNT):
                            color.add(self.BOARD[col-c][row-c][1])
                        print(color)
                        # TODO: check amount of colors in set (and take care of BOARD_COLOR)
            return False

        def isDiagonalRightWin():
            return False

        return isHorizontalWin() or isVerticalWin() or isDiagonalLeftWin() or isDiagonalRightWin()

if __name__=="__main__":
    TicTacToe()