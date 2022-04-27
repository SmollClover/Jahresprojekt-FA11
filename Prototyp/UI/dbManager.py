import sqlite3



class DbManager: 

    def __init__(self):
        print("Hallo, ich bin ein DB-Manager.")

        self.connection = sqlite3.connect("Datenbank/minimax.db")
        self.createTables()

    def createTables(self):
        cursor = self.connection.cursor()
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
                name VARCHAR(30) NOT NULL
            );
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
        cursor.execute(createTableScore)

        self.connection.commit()
        self.connection.close()






        # Benutzer registrieren

# INSERT INTO user (name, password)
# VALUES ({SQL-INJECTION-PROOF-NAME}, {HASHED-PW});

# Benutzer einloggen

# SELECT id, name
# FROM user
# WHERE name={SQL-INJECTION-PROOF-NAME} AND password={HASHED-PW};

