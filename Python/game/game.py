import pygame
from game.minimax import minimax

class Game:
    __blockSize = 50
    __blockPadding = 5
    __chipColor = {0: (255,255,255), 1: (255, 0, 0), -1: (255, 0, 255), 2: (60, 235, 184)}
    gameStateEnum = {
        "PLAYING": 0,
        "PLAYER": 1,
        "KI": 2,
        "DRAW": 3,
    }

    def __init__(self, screen, gameWidth, gameHeight, currentGame, difficulty):
        self.SCREEN = screen
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.SCREEN.get_size()
        self.BOARD = [[0 for x in range(self.gameWidth)] for y in range(self.gameHeight)]
        self.initBoard()
        self.currentGame = currentGame
        self.difficulty = difficulty
        self.winnerState = self.gameStateEnum["PLAYING"]
    def eventHandler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handleClickEvent(event.pos[0], event.pos[1])
                

    def tick(self, event):
        if self.currentGame.getCurrPlayer() == 1 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handleClickEvent(event.pos[0], event.pos[1])
        elif self.currentGame.getCurrPlayer() == -1:
            aiMove = minimax(self.currentGame, self.currentGame.getBoardState(), int(self.difficulty)+1, self.currentGame.getCurrPlayer())
            if len(aiMove[3]) > 0:
                self.currentGame.clickBlock(aiMove[3][1], aiMove[3][2])
            self.currentGame.clickBlock(aiMove[0], aiMove[1])
            
        self.drawCurrentState(self.currentGame.getBoardState())
        self.drawCurrentPiece(self.currentGame.getCurrPiece())
        self.winnerState = self.currentGame.getGameState()
        if self.winnerState != self.gameStateEnum["PLAYING"]:
            return (1,self.winnerState)
        return (0,self.currentGame.getCurrPlayer())

    def handleClickEvent(self, eventPosX, eventPosY):
        for col in range(len(self.BOARD)):
            for row in range(len(self.BOARD[0])):
                if pygame.Rect.collidepoint(self.BOARD[col][row], (eventPosX, eventPosY)):
                    self.currentGame.clickBlock(col, row)

    def drawCurrentState(self, state):
        for col in range(len(state)):
            for row in range(len(state[0])):
                self.BOARD[col][row] = self.__drawBlock(self.__chipColor[state[col][row]], col, row)

    def drawCurrentPiece(self, piece):
        if piece[0]:
            col = piece[1]
            row = piece[2]
            self.BOARD[col][row] = self.__drawBlock(self.__chipColor[2], col, row)

    def __drawBlock(self, color, posY, posX):
        fieldWidth = (self.__blockSize + self.__blockPadding) * self.gameWidth - self.__blockPadding
        fieldHeight = (self.__blockSize + self.__blockPadding) * self.gameHeight - self.__blockPadding
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldWidth / 2)
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldHeight / 2)
        return pygame.draw.rect(self.SCREEN, color, (offsetX + (posX * (self.__blockSize + self.__blockPadding)), offsetY + (posY * (self.__blockSize + self.__blockPadding)), self.__blockSize, self.__blockSize))

    def initBoard(self):
        fieldWidth = (self.__blockSize + self.__blockPadding) * self.gameWidth - self.__blockPadding
        fieldHeight = (self.__blockSize + self.__blockPadding) * self.gameHeight - self.__blockPadding
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldWidth / 2) - self.__blockPadding
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldHeight / 2) - self.__blockPadding
        pygame.draw.rect(self.SCREEN, (80, 80, 80), (offsetX, offsetY, fieldWidth + 2 * self.__blockPadding, fieldHeight + 2 * self.__blockPadding))

        self.drawCurrentState(self.BOARD)
