
class Player:
    def __init__(self):
        self.hp = 10
        self.gold = 10
        self.defense = 0

    def damage(self, e_attack):
        damage_dealt = e_attack - self.defense
        if damage_dealt < 0:
            damage_dealt = 0
        self.hp -= damage_dealt

    def gold(self, monster):
        self.gold += monster

    def upgrade_defense(self):
        self.defense += 1
