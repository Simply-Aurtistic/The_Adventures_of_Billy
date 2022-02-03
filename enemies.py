import random
from boards import Forest


level = Forest()


class Enemies:

    def __init__(self):
        self.level = level.difficulty
        self.hp = self.health()
        self.ap = self.attack_damage(self.level)
        self.defense = 0
        self.min = 1
        self.max = 2
        self.gold = random.randint(self.min, self.max)

    def damage(self, attack):
        damage_dealt = attack - self.defense
        if damage_dealt < 0:
            damage_dealt = 0
        self.hp -= damage_dealt

    def health(self):
        health_points = 2
        if self.level > 1:
            for _ in range(self.level - 1):
                health_points += random.randint(1, 3)
        return health_points

    def attack_damage(self, leveled):
        total_attack = 0
        for levels in range(leveled):
            total_attack += random.randint(0, 2)
        if total_attack == 0:
            total_attack = 1
        return total_attack


class Zombie(Enemies):

    def __init__(self):
        super().__init__()
        self.defense = 1


class Skeleton(Enemies):

    def __init__(self):
        super().__init__()
        self.defense = 1
