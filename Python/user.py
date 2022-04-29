class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    @staticmethod
    def setCurrUser(user):
        global __currUser
        __currUser = user

    @staticmethod
    def getCurrUser():
        try:
            return __currUser
        except:
            return False

    def print(self):
        print("id name", self.id, self.name)