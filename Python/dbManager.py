import sqlite3
import hashlib
from user import User

class DbManager: 

    def __init__(self):
        self.createTables()

    def createTables(self):
        connection = self.__openDb()
        cursor = connection.cursor()
        createTableUser = """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) NOT NULL UNIQUE,
                password VARCHAR(30) NOT NULL,
                registered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """

        createTableGame = """
            CREATE TABLE IF NOT EXISTS game (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) NOT NULL UNIQUE
            );
            """

        fillTableGame = """
            INSERT OR IGNORE INTO game (name) VALUES
            ("Bauernschach"), ("Dame"), ("TicTacToe");

        """

        createTableScore = """
            CREATE TABLE IF NOT EXISTS score (
                userid INTEGER,
                gameid INTEGER,
                difficulty INTEGER,
                win INTEGER,
                loss INTEGER,
                PRIMARY KEY(userid, gameid, difficulty)
            );       
            """

        cursor.execute(createTableUser)
        cursor.execute(createTableGame)
        cursor.execute(fillTableGame)
        cursor.execute(createTableScore)

        connection.commit()
        connection.close()

# Benutzer registrieren
    def register(self, username, password):
        connection = self.__openDb()
        hashedPass = hashlib.sha3_512(password.encode())
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name FROM user WHERE name = ?;
            """,
            (username,)
        )
        usernameResult = cursor.fetchall() 
        if len(usernameResult) == 0:
            cursor.execute("""
                INSERT INTO user (name, password)
                VALUES (?, ?);
                """,
                (username, hashedPass.hexdigest())
            )
            connection.commit()
            result = True
        else:
            result = False

        connection.close()
        return result
# Benutzer einloggen
    def login(self, username, password):
        connection = self.__openDb()
        hashedPass = hashlib.sha3_512(password.encode())
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name
            FROM user
            WHERE name = ? AND password = ?;
            """,
            (username, hashedPass.hexdigest())
        )
        userResult = cursor.fetchall() 
        if len(userResult) == 0:
            result = False
        else:
            result = User(userResult[0][0], userResult[0][1])
        connection.close()
        return result
    
    def __openDb(self):
        return sqlite3.connect("Database/SpieleKollektion.db")

    def getUserFromId(self, id):
        connection = self.__openDb()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name
            FROM user
            WHERE id = ?;
            """,
            (id,)
        )
        userResult = cursor.fetchall() 
        if len(userResult) == 0:
            result = False
        else:
            result = User(userResult[0][0], userResult[0][1])
        connection.close()
        return result

# Alle Spiele bekommen
    def getGames(self):
        connection = self.__openDb()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM game;""")
        gameResult = cursor.fetchall()
        connection.close()
        return gameResult

    def getGameIdFromName(self, name):
        games = self.getGames()
        for game in games:
            if game[1] == name:
                return game[0]
        return -1

# Bestenlisten
    def getBestPlayer(self, gameId, difficulty):
        connection = self.__openDb()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM score where gameid = ? AND difficulty = ? ORDER BY win;
        """, (gameId, difficulty))
        result = cursor.fetchall()
        connection.close()
        return result

    def updateScore(self, userId, gameId, difficulty, win):
        connection = self.__openDb()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM score where userid = ? AND gameid = ? AND difficulty = ?;
        """, (userId, gameId, difficulty))
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute("""
                INSERT INTO score (userid, gameid, difficulty, win, loss)
                VALUES (?, ?, ?, 0, 0);
            """, (int(userId), int(gameId), int(difficulty)))
            result = cursor.fetchall()
            connection.commit()
        
        if win:
            cursor.execute("""
                UPDATE score SET win = win + 1 WHERE userid = ? AND gameid = ? AND difficulty = ?
                """, (userId, gameId, difficulty))
        else:
            cursor.execute("""
                UPDATE score SET loss = loss + 1 WHERE userid = ? AND gameid = ? AND difficulty = ?
                """, (userId, gameId, difficulty))
        connection.commit()
        connection.close()
    
    def getWinLossFromUser(self, user, gameId, difficulty):
        connection = self.__openDb()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT win, loss FROM score where userid = ? AND gameid = ? AND difficulty = ?;
        """, (user.getId(), gameId, difficulty))

        result = cursor.fetchall()
        connection.close()
        return result 
        connection.close()