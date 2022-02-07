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
        self.shopping = True
        self.hp = self.max_health

    def store(self):
        while self.shopping:
            print(f"You have {self.gold} gold")
            print(f"Would you like to upgrade your armor for {self.armor_upgrade_costs} gold, your sword damage for "
                  f"{self.sword_upgrade_costs} gold, your bow damage for {self.bow_upgrade_costs} gold, or your health "
                  f"for {self.health_upgrade_costs} gold?")
            shop_choice = input("(armor/sword/bow/health/back): ").lower()

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
        else:
            game_load = input("What is the save name: ") + ".csv"
            self.load_data = pandas.read_csv(game_load)
            return self.load_data
