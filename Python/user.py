class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def print(self):
        print("id name", self.id, self.name)