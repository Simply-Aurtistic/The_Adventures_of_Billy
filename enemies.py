import random
from boards import Forest
import math


level = Forest()


class Enemies:

    def __init__(self):
        self.level = level.difficulty
        self.hp = self.health()
        self.ap = self.attack_damage(self.level)
        self.defense = 0
        self.min = 1
        self.max = 2
        self.gold = self.money(self.level)

    def money(self, challenge):
        base_gold = random.randint(self.min, self.max)
        factor = math.ceil(challenge / 3)
        total_gold = base_gold * factor
        return total_gold

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

    def attack_damage(self, challenge):
        total_attack = 0
        for levels in range(challenge):
            total_attack += random.randint(0, 2)
        if total_attack == 0:
            total_attack = 1
        return total_attack


class Zombie(Enemies):

    def __init__(self):
        super().__init__()
        self.defense = 0
        self.name = "Zombie"


class Skeleton(Enemies):

    def __init__(self):
        super().__init__()
        self.defense = 1
        self.name = "Skeleton"


class Troll(Enemies):

    def __init__(self):
        super().__init__()
        self.defense = 4
        self.min = 4
        self.max = 5
        self.name = "Troll"


class Goblin(Enemies):
    def __init__(self):
        super().__init__()
        self.defense = 0
        self.min = 1
        self.max = 2
        self.name = "Goblin"


class Dragon(Enemies):
    def __init__(self):
        super().__init__()
        self.defense = 4
        self.hp = self.health() * 5
        self.min = 12
        self.max = 15
        self.name = "Dragon"


class VampireLord(Enemies):
    def __init__(self):
        super().__init__()
        self.defense = 5
        self.hp = self.health() * 4
        self.min = 12
        self.max = 15
        self.name = "Vampire Lord"


class Golem(Enemies):
    def __init__(self):
        super().__init__()
        self.defense = 0
        self.hp = self.health() * 3
        self.min = 4
        self.max = 6
        self.name = "Golem"


class Giant(Enemies):
    def __init__(self):
        super().__init__()
        self.defense = 0
        self.hp = self.health() * 3
        self.min = 4
        self.max = 6
        self.name = "Giant"
