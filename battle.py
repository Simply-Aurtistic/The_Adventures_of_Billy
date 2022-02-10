from enemies import Enemies, Zombie, Skeleton, Troll, Goblin, Dragon, VampireLord, Golem, Giant
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
        self.enemy_list = []
        self.encounter_list = []
        self.enemy = Enemies()

    def path_choice(self):
        while self.choosing_path:
            self.area = input("Would you like to explore the forest, the mountain, the cave, or take on a boss? "
                              "(forest/mountain/cave/boss): ").lower()
            print("\n")
            while self.area not in ["forest", "mountain", "cave", "boss", "leave"]:
                print("Try to keep to right choices.")
                self.area = input("Would you like to explore the forest, the mountain, the cave, or take on a boss? "
                                  "(forest/mountain/cave/boss): ").lower()
                print("\n")
            if self.area == "forest":
                self.choice = "start"
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy_list = [Zombie(), "Zombie", Skeleton(), "Skeleton"]

            elif self.area == "mountain":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy_list = [Golem(), "Golem", Giant(), "Giant"]

            elif self.area == "cave":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy_list = [Troll(), "Troll", Goblin(), "Goblin"]
                
            elif self.area == "boss":
                self.fight = True
                self.cont = True
                self.choosing_path = False
                self.enemy_list = [Dragon(), "Dragon", VampireLord(), "Vampire Lord"]

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
        if self.area == "forest":
            self.choose_enemy()
            self.encounter_forest()
        elif self.area == "mountain":
            self.choose_enemy()
            self.encounter_mountain()
        elif self.area == "cave":
            self.choose_enemy()
            self.encounter_cave()
        elif self.area == "boss":
            self.choose_enemy()
            self.encounter_boss()

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
                if self.enemy.hp > 0:
                    if round_num > 2:
                        self.shop.damage2(self.enemy.ap)

            elif attack_weapon == "sword":
                attack = self.shop.sworddamage
                self.enemy.damage(attack)
                if self.enemy.hp > 0:
                    self.shop.damage1(self.enemy.ap)
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
                    if self.shop.low_potion > 0 or self.shop.high_potion > 0:
                        drink = input(f"you have {self.shop.low_potion} low potions and {self.shop.high_potion} high "
                                      f"potions left. would you like to drink one?\n"
                                      f"(low/high)")
                        if drink == "low":
                            self.drink_L_P()

                        elif drink == "high":
                            self.drink_H_P()
                print("\n")

    def encounter_forest(self):
        self.encounter_list = [f"As you are following the path, you hear rustling in a bush, a {self.enemy.name} "
                               f"emerges.",

                               f"As you are passing by a tree, you hear rustling in the limbs above, \na "
                               f"{self.enemy.name} drops down in front of you.",

                               f"You hear noises ahead, you look and see a {self.enemy.name} wandering towards you."]

    def encounter_mountain(self):
        self.encounter_list = [f"As you are traversing the side of the mountain, you notice a {self.enemy.name} ahead"
                               f"of you.",

                               f"As you traverse the mountain path, a large pile of stones start shifting. \na "
                               f"{self.enemy.name} emerges from the pile.",

                               f"As you are walking along a cliff, a stone falls in front of you. \n"
                               f"You look up and see a {self.enemy.name} throwing rocks at you."]

    def encounter_cave(self):
        self.encounter_list = [f"As you delve deeper into the cave you hear footsteps behind you, you look back and see"
                               f" a {self.enemy.name}.",

                               f"As you follow deeper into the cave, you see a light ahead of you. \n"
                               f"There is a bonfire ahead with a {self.enemy.name} sitting next to it.",

                               f"You walk for a while and take a break. While you are resting, you hear grunting coming"
                               f" from up ahead. \nYou see a {self.enemy.name} running towards you."]

    def encounter_boss(self):
        self.encounter_list = [f"You feel a great power coming from the castle in front of you. \n"
                               f"You enter the castle and go room to room until you find a {self.enemy.name} waiting "
                               f"for you. \n"
                               f"It turns to you and says 'You have mettle, I'll give you that. But this will be your "
                               f"end.'",

                               f"You feel a vicious aura coming for the heart of the forest. \n"
                               f"You go to investigate and find a {self.enemy.name} in the middle of a clearing. \n"
                               f"You don't think they know you are there.",

                               f"You see giant menacing cloud swirling around the top of Mount Simply_Aurtistic, \n"
                               f"lightning striking it left and right. You decide to investigate. \n"
                               f"As you get close to the clouds, you hear a booming voice call out, \n"
                               f"'You know not what you are doing. BEGONE!' \n"
                               f"At that moment, a man comes flying out of the whirlwind and falls before your feet. \n"
                               f"You look closer and see a {self.enemy.name} in the middle of the storm."]

    def drink_L_P(self):
        if self.shop.low_potion >= 1:
            self.shop.hp += random.randint(1, 4)
            self.shop.low_potion -= 1
        else:
            print("no full low potions")

    def drink_H_P(self):
        if self.shop.high_potion >= 1:
            self.shop.hp += random.randint(10, 15)
            self.shop.high_potion -= 1
        else:
            print("No full high potions")

    def choose_enemy(self):
        if self.enemy == self.enemy_list[0]:
            self.enemy = self.enemy_list[2]
        elif self.enemy == self.enemy_list[2]:
            self.enemy = self.enemy_list[0]
        elif self.enemy.name == self.enemy_list[1]:
            self.enemy = self.enemy_list[2]
        elif self.enemy.name == self.enemy_list[3]:
            self.enemy = self.enemy_list[0]
        else:
            self.enemy = random.choice(self.enemy_list)
