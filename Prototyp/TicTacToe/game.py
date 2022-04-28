from tkinter.tix import COLUMN
import pygame
from tictactoe import TicTacToe
from minimax import minimax

class Game:
    blockSize = 50
    blockPadding = 5
    chipColor = {0: (255,255,255), 1: (255, 0, 0), -1: (255, 0, 255)}
    gameStateEnum = {
        "PLAYING": 0,
        "PLAYER": 1,
        "KI": 2,
        "DRAW": 3,
    }

    def __init__(self, gameWidth, gameHeight, currentGame):
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        pygame.init()
        self.SCREEN = pygame.display.set_mode((400, 400))
        self.SCREEN.fill((31, 31, 31))
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.SCREEN.get_size()
        self.BOARD = [[0 for x in range(self.gameWidth)] for y in range(self.gameHeight)]
        self.initBoard()
        self.currentGame = currentGame

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # or self.currentGame.isGameOver(self.currentGame.getBoardState()):
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.handleClickEvent(event.pos[0], event.pos[1]):
                        if self.currentGame.getCurrPlayer() == -1:
                            aiMove = minimax(self.currentGame, self.currentGame.getBoardState(), 4, currentGame.getCurrPlayer())
                            self.currentGame.clickBlock(aiMove[0], aiMove[1])
                        self.drawCurrentState(currentGame.getBoardState())
                        winnerState = currentGame.getGameState()
                        if winnerState == self.gameStateEnum["DRAW"]:
                            print('Unentschieden!')
                        elif winnerState == self.gameStateEnum["PLAYER"]:
                            print('Der/Die SpielerIn hat gewonnen!')
                        elif winnerState == self.gameStateEnum["KI"]:
                            print('Die KI hat gewonnen!')
            pygame.display.flip()

        print("Exit program")
        pygame.quit()



    def handleClickEvent(self, eventPosX, eventPosY):
        for col in range(len(self.BOARD)):
            for row in range(len(self.BOARD[0])):
                if pygame.Rect.collidepoint(self.BOARD[col][row], (eventPosX, eventPosY)):
                    return self.currentGame.clickBlock(col, row)

    def drawCurrentState(self, state):
        for col in range(len(state)):
            for row in range(len(state[0])):
                self.BOARD[col][row] = self.__drawBlock(self.chipColor[state[col][row]], col, row)

    def __drawBlock(self, color, posY, posX):
        fieldWidth = (self.blockSize + self.blockPadding) * self.gameWidth - self.blockPadding
        fieldHeight = (self.blockSize + self.blockPadding) * self.gameHeight - self.blockPadding
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldWidth / 2)
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldHeight / 2)
        return pygame.draw.rect(self.SCREEN, color, (offsetX + (posX * (self.blockSize + self.blockPadding)), offsetY + (posY * (self.blockSize + self.blockPadding)), self.blockSize, self.blockSize))

    def initBoard(self):
        fieldWidth = (self.blockSize + self.blockPadding) * self.gameWidth - self.blockPadding
        fieldHeight = (self.blockSize + self.blockPadding) * self.gameHeight - self.blockPadding
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldWidth / 2) - self.blockPadding
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldHeight / 2) - self.blockPadding
        pygame.draw.rect(self.SCREEN, (80, 80, 80), (offsetX, offsetY, fieldWidth + 2 * self.blockPadding, fieldHeight + 2 * self.blockPadding))

        self.drawCurrentState(self.BOARD)
        
if __name__=="__main__":
    gameWidth = 6
    gameHeight = 6

    Game(gameWidth, gameHeight,TicTacToe(4, gameWidth, gameHeight))