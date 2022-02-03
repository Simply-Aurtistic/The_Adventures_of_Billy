

class Level:
    def __init__(self):
        self.difficulty = 0
        self.set_level()

    def set_level(self):
        self.difficulty = int(input("What difficulty would you like? 1 - 10(1 = EASY 10 = HARD): "))

    def get_level(self):
        return self.difficulty


class Forest(Level):

    def __init__(self):
        super().__init__()
