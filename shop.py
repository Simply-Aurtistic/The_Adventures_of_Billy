import random
import pandas


class Shop:

    def __init__(self):
        self.call_save()
        self.max_health = self.load_data.iat[0, 2]
        self.health_upgrade_costs = self.load_data.iat[1, 2]
        self.sword_upgrade_costs = self.load_data.iat[2, 2]
        self.bow_upgrade_costs = self.load_data.iat[3, 2]
        self.armor_upgrade_costs = self.load_data.iat[4, 2]
        self.gold = self.load_data.iat[5, 2]
        self.sworddamage = self.load_data.iat[6, 2]
        self.bowdamage = self.load_data.iat[7, 2]
        self.defense = self.load_data.iat[8, 2]
        self.low_potion = self.load_data.iat[9, 2]
        self.high_potion = self.load_data.iat[10, 2]
        self.hp = self.max_health
        self.shopping = True

    def store(self):
        while self.shopping:
            print(f"You have {self.gold} gold")
            print(f"As you walk though the door, Buzz turns to you and says 'Welcome back, \n"
                  f"Would you like to upgrade your armor for {self.armor_upgrade_costs} gold, \n"
                  f"your sword damage for {self.sword_upgrade_costs} gold, \n"
                  f"your bow damage for {self.bow_upgrade_costs} gold, \n"
                  f"your health for {self.health_upgrade_costs} gold?\n"
                  f"or would you like a buy a low potion for 5 gold or high potion for 20 gold")
            shop_choice = input("(armor/sword/bow/health/low/high/back): ").lower()

            if shop_choice == "armor":
                if int(self.gold) >= int(self.armor_upgrade_costs):
                    self.defense += 1
                    self.gold -= self.armor_upgrade_costs
                    self.armor_upgrade_costs += 5
                else:
                    print("Not enough money")

            elif shop_choice == "sword":
                if self.gold >= self.sword_upgrade_costs:
                    self.sworddamage += 1
                    self.gold -= self.sword_upgrade_costs
                    self.sword_upgrade_costs += 5
                else:
                    print("Not enough money")

            elif shop_choice == "bow":
                if self.gold >= self.bow_upgrade_costs:
                    self.bowdamage += 1
                    self.gold -= self.bow_upgrade_costs
                    self.bow_upgrade_costs += 5
                else:
                    print("Not enough money")

            elif shop_choice == "health":
                if self.gold >= self.health_upgrade_costs:
                    self.health_upgrade()
                else:
                    print("Not enough money")

            elif shop_choice == "low":
                if self.gold >= 5:
                    self.low_potion += 1
                else:
                    print("Not enough money")
            elif shop_choice == "high":
                if self.gold >= 20:
                    self.high_potion += 1
                else:
                    print("Not enough money")

            elif shop_choice == "back":
                self.shopping = False
                return

    def gold(self, monster):
        self.gold += monster

    def health_upgrade(self):
        self.max_health += random.randint(1, 3)
        self.gold -= self.health_upgrade_costs
        self.health_upgrade_costs += 5

    def call_save(self):
        game = input("New game or load a game (new/load): ").lower()
        if game == "new":
            self.load_data = pandas.read_csv("start.csv")
            print("As you enter Trevoria, a small quiet town, you are greeted by a old man. \n"
                  "'Welcome to our fair little town.' He looks around a bit then continues 'We have been plagued by a "
                  "monster horde of late.' \n"
                  "He looks at your sword. 'Perhaps you can help us with this problem. You look capable enough at "
                  "least. \n"
                  "If you are looking for upgrades for your equipment, Buzz can help you over in his shop, the Iron "
                  "Maiden'\n"
                  "You head over to the Iron Maiden. As you walk through the door, you are greeted by a big gruff man."
                  " \n"
                  "'Hello my name is Beelzebub, but you can call me Buzz. You must be that new adventurer I have heard "
                  "about' \n"
                  "Buzz turns and gets back behind the counter. 'Here. Take this bow, it will help you with the fights "
                  "to come.' \n"
                  "As you turn to leave Buzz calls out, 'Good luck and come back if you need anything, you hear'")

        else:
            self.game_load = input("What is the save name: ").lower()
            self.game_load_save = self.game_load + ".csv"
            self.load_data = pandas.read_csv(self.game_load_save)
            return self.load_data

    def damage1(self, enemy):
        defense = round(self.sworddamage / 2) + self.defense
        damage = enemy - defense
        if damage < 0:
            damage = 0
        self.hp -= damage

    def damage2(self, enemy):
        defense = self.defense
        damage = enemy - defense
        if damage < 0:
            damage = 0
        self.hp -= damage
