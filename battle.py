from enemies import Zombie, Skeleton, Troll, Goblin, Dragon, VampireLord, Golem, Giant
import random


class Battle:

    def __init__(self, shop_class=None):
        self.shop = shop_class
        self.choice = "start"
        self.choosing_path = True
        self.room = 1
        self.area = "start"
        self.fight = True
        self.cont = True
        self.enemy = "none"

    def damage(self, e_attack):
        damage_dealt = e_attack - self.shop.defense
        if damage_dealt < 0:
            damage_dealt = 0
        self.shop.hp -= damage_dealt

    def path_choice(self):
        while self.choosing_path:
            self.area = input("Would you like to explore the forest, the mountain, the cave, or take on a boss? "
                              "(forest/mountain/cave/boss): ").lower()

            while self.area not in ["forest", "mountain", "cave", "boss", "leave"]:
                print("Try to keep to right choices.")
                self.area = input("Would you like to explore the forest, the mountain, the cave, or take on a boss? "
                                  "(forest/mountain/cave/boss): ").lower()

            if self.area == "forest":
                self.choice = "start"
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy = random.choice([Zombie(), Skeleton()])

            elif self.area == "mountain":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy = random.choice([Golem(), Giant()])

            elif self.area == "cave":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy = random.choice([Troll(), Goblin()])

            elif self.area == "boss":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy = random.choice([Dragon(), VampireLord()])

            elif self.area == "leave":
                self.choice = "back"
                self.fight = False
                self.cont = False
                self.choosing_path = False
                return

    def initiate_fight(self):
        while self.cont:
            if self.area == "leave":
                self.choice = "back"
                self.cont = False
                return

            elif self.area in ["forest", "mountain", "cave", "boss"]:
                self.fight = True
                while self.fight:
                    self.battle()

    def adventures(self):
        if self.area == "leave":
            return
        elif self.shop.hp <= 0:
            return
        elif self.shop.hp > 0:
            if self.area != "leave":
                self.path_choice()
                self.initiate_fight()
            else:
                return

    def battle(self):
        print(f"{self.shop.hp} hp")
        first_choice = input(f"You encounter a {self.enemy.name}, what do you do? (run/fight): ").lower()

        if first_choice == "run":
            self.choice = "back"
            self.fight = False
            self.cont = False
            return
        round_num = 1
        self.enemy.hp = self.enemy.health()
        while self.enemy.hp > 0 and self.choice != "back":
            print(f"{self.shop.hp} hp")
            attack_weapon = input("Would you like to use your sword or bow?: ").lower()
            if attack_weapon == "bow":
                attack = self.shop.bow.damage
                self.enemy.damage(attack)
                round_num += 1
                if round_num > 2:
                    self.shop.damage(self.enemy.ap)

            if attack_weapon == "sword":
                attack = self.shop.sword.damage
                self.enemy.damage(attack)
                if self.enemy.hp > 0:
                    self.shop.damage(self.enemy.ap)
                round_num += 1

            if self.shop.hp <= 0:
                print("You fainted, lose half your money")
                self.shop.gold /= 2
                self.shop.gold = round(self.shop.gold)
                self.choice = "back"
                return

            if self.enemy.hp <= 0:
                self.shop.gold += self.enemy.gold

                print("It's dead.")
                print(f"{self.shop.gold} gold")
                print(f"{self.shop.hp} hp")

                cont = input("Continue on the path? (yes/no): ").lower()
                if cont == "no":
                    self.fight = False
                    self.cont = False
                    self.choice = "back"
                elif cont == "yes":
                    self.room += 1
                    if self.room % 10 == 0:
                        print(f"You find a chest that had {self.room} gold in it!")
                        self.shop.gold += self.room
