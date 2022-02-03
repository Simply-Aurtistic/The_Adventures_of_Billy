from player import Player
from weapons import Sword, Bow
import random


sword_upgrade_costs = 5
bow_upgrade_costs = 5
armor_upgrade_costs = 5
player = Player()
sword = Sword()
bow = Bow()
round_num = 1
game_is_on = True


while game_is_on:
    print("You are at base")
    choice = input("would you like to go shopping, adventuring, or pause for now? (shop/adventure/pause): ").lower()
    while choice == "shop":
        print(f"You have {player.gold} gold")
        print(f"Would you like to upgrade your armor for {armor_upgrade_costs} gold, your sword damage for "
              f"{sword_upgrade_costs} gold, or you bow damage for {bow_upgrade_costs} gold?")
        shop_choice = input("(armor/sword/bow/back): ").lower()

        if shop_choice == "armor":
            if player.gold >= armor_upgrade_costs:
                player.upgrade_defense()
                player.gold -= armor_upgrade_costs
                armor_upgrade_costs += 5
            else:
                print("Not enough money")
        elif shop_choice == "sword":
            if player.gold >= sword_upgrade_costs:
                sword.upgrade_damage()
                player.gold -= sword_upgrade_costs
                sword_upgrade_costs += 5
            else:
                print("Not enough money")
        elif shop_choice == "bow":
            if player.gold >= bow_upgrade_costs:
                bow.upgrade_damage()
                player.gold -= bow_upgrade_costs
                bow_upgrade_costs += 5
            else:
                print("Not enough money")
        elif shop_choice == "back":
            choice = "back"
    while choice == "adventure":

        from enemies import Zombie, Skeleton
        enemy_list = [Zombie(), Skeleton()]
        enemy = random.choice(enemy_list)
        print(f"{player.hp} hp")
        first_choice = input(f"You encounter a {enemy}, what do you do? (run/fight): ").lower()
        if first_choice == "run":
            battle = False
            choice = "back"

        else:
            battle = True
            while battle:
                print(f"{player.hp} hp")
                print(round_num)
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
                    player.damage(enemy.ap)
                    round_num += 1
                if player.hp <= 0:
                    print("You fainted, lose half your money")
                    player.gold /= 2
                    player.gold = round(player.gold)
                    battle = False
                    choice = "back"

                if enemy.hp <= 0:
                    player.gold += enemy.gold
                    battle = False
                    print(player.gold)
                    print(player.hp)
                    cont = input("Countinue on the path? (yes/no): ").lower()
                    if cont == "no":
                        choice = "back"
    if choice == "pause":
        game_is_on = False
