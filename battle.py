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
        self.encounter_list = []

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
                self.encounter_forest()

            elif self.area == "mountain":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy = random.choice([Golem(), Giant()])
                self.encounter_mountain()

            elif self.area == "cave":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy = random.choice([Troll(), Goblin()])
                self.encounter_cave()

            elif self.area == "boss":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy = random.choice([Dragon(), VampireLord()])
                self.encounter_boss()

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
        first_choice = input(f"{random.choice(self.encounter_list)} what do you do? (run/fight): ").lower()

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
                attack = self.shop.bowdamage
                self.enemy.damage(attack)
                round_num += 1
                if round_num > 2:
                    self.shop.damage(self.enemy.ap)

            if attack_weapon == "sword":
                attack = self.shop.sworddamage
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

    def encounter_forest(self):
        self.encounter_list = [f"As you are following the path, you hear rustling in a bush, a {self.enemy.name} "
                               f"emerges.",

                               f"As you are passing by a tree, you hear rustling in the limbs above,\n a "
                               f"{self.enemy.name} drops down in front of you.",

                               f"You hear noises ahead, you look and see a {self.enemy.name} wandering towards you."]

    def encounter_mountain(self):
        self.encounter_list = [f"As you are traversing the side of the mountain, you notice a {self.enemy.name} ahead"
                               f"of you.",

                               f"As you traverse the mountain path, a large pile of stones start shifting.\n a "
                               f"{self.enemy.name} emerges from the pile.",

                               f"As you are walking along a cliff, a stone falls in front of you.\n You look up and see "
                               f"a {self.enemy.name} throwing rocks at you."]

    def encounter_cave(self):
        self.encounter_list = [f"As you delve deeper into the cave you hear footsteps behind you, you look back and see"
                               f" a {self.enemy.name}.",

                               f"As you follow deeper into the cave, you see a light ahead of you.\n There is a bonfire "
                               f"ahead with a {self.enemy.name} sitting next to it.",

                               f"You walk for a while and take a break. While you are resting, you hear grunting coming"
                               f" from up ahead.\n You see a {self.enemy.name} running towards you."]

    def encounter_boss(self):
        self.encounter_list = [f"You feel a great power coming from the castle in front of you.\n You enter the castle "
                               f"and go room to room until you find a {self.enemy.name} waiting for you.\n It turns to "
                               f"you and says 'You have mettle, I'll give you that. But this will be your end.'",

                               f"You feel a vicious aura coming for the heart of the forest.\n You go to investigate and"
                               f" find a {self.enemy.name} in the middle of a clearing.\n You don't think they know you"
                               f" are there.",

                               f"You see giant menacing cloud swirling around the top of Mount Simply_Aurtistic. "
                               f"Lightning striking it left and right. You decide to investigate. As you get close to "
                               f"the clouds, you hear a booming voice call out, 'You know not what you are doing. "
                               f"BEGONE!' At that moment, a man comes flying out of the whirlwind and falls before "
                               f"your feet. You look closer and see a {self.enemy.name} in the middle of the storm."]
