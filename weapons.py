class Weapon:

    def __init__(self):
        self.damage = 2

    def upgrade_damage(self):
        self.damage += 1


class Sword(Weapon):

    def __init__(self):
        super().__init__()
        self.defense = 1
        self.damage = 2


class Bow(Weapon):

    def __init__(self):
        super().__init__()
        self.defense = 0
        self.damage = 2
