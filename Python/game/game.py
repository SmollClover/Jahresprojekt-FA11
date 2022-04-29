import pygame
from game.minimax import MiniMax

class Game:
    __blockSize = 50
    __blockPadding = 5
    __boardColor = (255,255,255)

    gameStateEnum = {
        "PLAYING": 0,
        "PLAYER": 1,
        "KI": 2,
        "DRAW": 3,
    }

    def __init__(self, dbManager, screen, gameWidth, gameHeight, currentGame, difficulty):
        self.SCREEN = screen
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.SCREEN.get_size()
        self.BOARD = [[0 for x in range(self.gameWidth)] for y in range(self.gameHeight)]
        self.initBoard()
        self.currentGame = currentGame
        self.difficulty = difficulty
        self.winnerState = self.gameStateEnum["PLAYING"]
        self.__aiMove = None

        gameName = dbManager.getGame(self.currentGame.id)[0][0]
        self.__imageType = {
            1: pygame.image.load(f"./sprite/{gameName}_Player.png"), 
            -1: pygame.image.load(f"./sprite/{gameName}_KI.png"), 
            2: pygame.image.load(f"./sprite/{gameName}_Player_Selected.png")
        }
        
    def eventHandler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handleClickEvent(event.pos[0], event.pos[1])
                

    def tick(self, event):
        if self.currentGame.getCurrPlayer() == 1 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handleClickEvent(event.pos[0], event.pos[1])
        elif self.currentGame.getCurrPlayer() == -1:
            self.__aiMove = MiniMax(self.currentGame, self.currentGame.getBoardState(), int(self.difficulty)+1, self.currentGame.getCurrPlayer()).calc()
            if len(self.__aiMove[3]) > 0:
                self.currentGame.clickBlock(self.__aiMove[3][1], self.__aiMove[3][2])
            self.currentGame.clickBlock(self.__aiMove[0], self.__aiMove[1])
            
        self.drawCurrentState(self.currentGame.getBoardState())
        self.drawCurrentPiece(self.currentGame.getCurrPiece())
        self.winnerState = self.currentGame.getGameState()
        if self.winnerState != self.gameStateEnum["PLAYING"]:
            return (1,self.winnerState)
        return (0,self.currentGame.getCurrPlayer())

    def getDebugInfo(self):
        if self.__aiMove == None:
            return str(None)
        else:
            if len(self.__aiMove[3]) > 2:
                debugInfo = "Column {} Row {} to Column {} Row {} with Score {}".format(self.__aiMove[1] + 1, self.__aiMove[0] + 1, self.__aiMove[3][2] + 1, self.__aiMove[3][1] + 1, self.__aiMove[2])
            else:
                debugInfo = "Column {} Row {} with Score {}".format(self.__aiMove[1] + 1, self.__aiMove[0] + 1, self.__aiMove[2])
            return debugInfo

    def handleClickEvent(self, eventPosX, eventPosY):
        for col in range(len(self.BOARD)):
            for row in range(len(self.BOARD[0])):
                if pygame.Rect.collidepoint(self.BOARD[col][row], (eventPosX, eventPosY)):
                    self.currentGame.clickBlock(col, row)

    def drawCurrentState(self, state):
        for col in range(len(state)):
            for row in range(len(state[0])):
                newRect = self.__drawBlock(col, row)

                if state[col][row] != 0:
                    self.__drawImage(self.__imageType[state[col][row]], col, row)

                self.BOARD[col][row] = newRect

    def drawCurrentPiece(self, piece):
        if piece[0]:
            col = piece[1]
            row = piece[2]
            newRect = self.__drawBlock(col, row)
            self.__drawImage(self.__imageType[2], col, row)
            self.BOARD[col][row] = newRect

    def __drawBlock(self, posY, posX):
        fieldWidth = (self.__blockSize + self.__blockPadding) * self.gameWidth - self.__blockPadding
        fieldHeight = (self.__blockSize + self.__blockPadding) * self.gameHeight - self.__blockPadding
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldWidth / 2)
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldHeight / 2)
        return pygame.draw.rect(self.SCREEN, self.__boardColor, (offsetX + (posX * (self.__blockSize + self.__blockPadding)), offsetY + (posY * (self.__blockSize + self.__blockPadding)), self.__blockSize, self.__blockSize))

    def __drawImage(self, image, posY, posX):
        fieldWidth = (self.__blockSize + self.__blockPadding) * self.gameWidth - self.__blockPadding
        fieldHeight = (self.__blockSize + self.__blockPadding) * self.gameHeight - self.__blockPadding
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldWidth / 2)
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldHeight / 2)
        return self.SCREEN.blit(pygame.transform.scale(image, (self.__blockSize, self.__blockSize)), (offsetX + (posX * (self.__blockSize + self.__blockPadding)), offsetY + (posY * (self.__blockSize + self.__blockPadding)), self.__blockSize, self.__blockSize))

    def initBoard(self):
        fieldWidth = (self.__blockSize + self.__blockPadding) * self.gameWidth - self.__blockPadding
        fieldHeight = (self.__blockSize + self.__blockPadding) * self.gameHeight - self.__blockPadding
        offsetX = int(self.WINDOW_WIDTH / 2 - fieldWidth / 2) - self.__blockPadding
        offsetY = int(self.WINDOW_HEIGHT / 2 - fieldHeight / 2) - self.__blockPadding
        pygame.draw.rect(self.SCREEN, (80, 80, 80), (offsetX, offsetY, fieldWidth + 2 * self.__blockPadding, fieldHeight + 2 * self.__blockPadding))

        self.drawCurrentState(self.BOARD)
