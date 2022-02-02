

class Level:
    def __init__(self):
        self.difficulty = 0

    def setlevel(self):
        self.difficulty = int(input("What difficulty would you like? 1 - 10(1 = EASY 10 = HARD)"))


class Forest(Level):

    def __init__(self):
        super().__init__()
        self.setlevel()
