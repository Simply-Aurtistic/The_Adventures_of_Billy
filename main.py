

from player import Player
from weapons import Sword, Bow
import random
import pandas

player = Player()
sword = Sword()
bow = Bow()
round_num = 1
game_is_on = True


game = input("New game or load a game (new/load): ").lower()
if game == "new":
    health_upgrade_costs = 5
    sword_upgrade_costs = 5
    bow_upgrade_costs = 5
    armor_upgrade_costs = 5
    max_health = player.hp
    gold = player.gold

elif game == "load":
    game_load = input("What is the save name: ") + ".csv"
    load_data = pandas.read_csv(game_load)
    max_health = load_data.iat[0, 2]
    health_upgrade_costs = load_data.iat[1, 2]
    sword_upgrade_costs = load_data.iat[2, 2]
    bow_upgrade_costs = load_data.iat[3, 2]
    armor_upgrade_costs = load_data.iat[4, 2]
    gold = load_data.iat[5, 2]

while game_is_on:
    print("You are at base")
    player.hp = max_health
    choice = input("would you like to go shopping, adventuring, or pause for now? (shop/adventure/pause): ").lower()
    while choice not in ["shop", "adventure", "pause"]:
        print("Try to keep to right choices.")
        choice = input("would you like to go shopping, adventuring, or pause for now? (shop/adventure/pause): ").lower()

    while choice == "shop":
        print(f"You have {gold} gold")
        print(f"Would you like to upgrade your armor for {armor_upgrade_costs} gold, your sword damage for "
              f"{sword_upgrade_costs} gold, your bow damage for {bow_upgrade_costs} gold, or your health for "
              f"{health_upgrade_costs} gold?")
        shop_choice = input("(armor/sword/bow/health/back): ").lower()

        if shop_choice == "armor":
            if gold >= armor_upgrade_costs:
                player.upgrade_defense()
                gold -= armor_upgrade_costs
                armor_upgrade_costs += 5
            else:
                print("Not enough money")
        elif shop_choice == "sword":
            if gold >= sword_upgrade_costs:
                sword.upgrade_damage()
                gold -= sword_upgrade_costs
                sword_upgrade_costs += 5
            else:
                print("Not enough money")
        elif shop_choice == "bow":
            if gold >= bow_upgrade_costs:
                bow.upgrade_damage()
                gold -= bow_upgrade_costs
                bow_upgrade_costs += 5
            else:
                print("Not enough money")
        elif shop_choice == "health":
            if gold >= health_upgrade_costs:
                player.health_upgrade()
                gold -= health_upgrade_costs
                health_upgrade_costs += 5
                max_health = player.hp
        elif shop_choice == "back":
            choice = "back"
    while choice == "adventure":
        enemy_list = []
        area = input("Would you like to explore the forest, the mountain, the cave, or take on a boss? "
                     "(forest/mountain/cave/boss): ").lower()

        while area not in ["forest", "mountain", "cave", "boss"]:
            print("Try to keep to right choices.")
            area = input("Would you like to explore the forest, the mountain, the cave, or take on a boss? "
                         "(forest/mountain/cave/boss): ").lower()

        from enemies import Zombie, Skeleton, Troll, Goblin, Dragon, VampireLord, Golem, Giant

        if area == "forest":
            enemy_list = [Zombie(), Skeleton()]
        elif area == "mountain":
            enemy_list = [Golem(), Giant()]
        elif area == "cave":
            enemy_list = [Troll(), Goblin()]
        elif area == "boss":
            enemy_list = [Dragon(), VampireLord()]

        room = 1
        cont = True
        while cont:
            enemy = random.choice(enemy_list)
            print(f"{player.hp} hp")
            first_choice = input(f"You encounter a {enemy.name}, what do you do? (run/fight): ").lower()
            if first_choice == "run":
                cont = False
                battle = False
                choice = "back"

            else:
                round_num = 1
                battle = True
                while battle:
                    print(f"{player.hp} hp")
                    attack_weapon = input("Would you like to use your sword or bow?: ").lower()

                    if attack_weapon == "bow":
                        attack = bow.damage
                        enemy.damage(attack)
                        round_num += 1
                        if round_num > 2:
                            player.damage(enemy.ap)

                    if attack_weapon == "sword":
                        attack = sword.damage
                        enemy.damage(attack)
                        if enemy.hp > 0:
                            player.damage(enemy.ap)
                        round_num += 1
                    if player.hp <= 0:
                        print("You fainted, lose half your money")
                        gold /= 2
                        gold = round(gold)
                        battle = False
                        choice = "back"

                    if enemy.hp <= 0:
                        gold += enemy.gold
                        battle = False
                        print(f"{gold} gold")
                        print(f"{player.hp} hp")
                        cont = input("Continue on the path? (yes/no): ").lower()
                        if cont == "no":
                            cont = False
                            choice = "back"
                        elif cont == "yes":
                            room += 1
                            if room % 10 == 0:
                                print(f"You find a chest that had {room} gold in it!")
                                gold += room
    if choice == "pause":
        game_is_on = False
save_game_name = input("What is the save name?: ").lower() + ".csv"

save_game = {
    "variable": ["hp", "huc", "suc", "buc", "auc", "gold"],
    "values": [max_health, health_upgrade_costs, sword_upgrade_costs, bow_upgrade_costs, armor_upgrade_costs,
               gold]
    }
save_data = pandas.DataFrame(save_game)
save_data.to_csv(save_game_name)
