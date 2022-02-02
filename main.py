from enemies import Zombie, Skeleton
from boards import Forest
from player import Player
from weapons import Sword, Bow
import random


sword_upgrade_costs = 5
bow_upgrade_costs = 5
armor_upgrade_costs = 5
player = Player()
sword = Sword()
bow = Bow()
battle = True
round_num = 1


print("you are at base")
choice = input("would you like to go shopping or adventuring?").lower()

while choice == "shopping":
    print(player.gold)
    print(f"Would you like to upgrade your armor for {armor_upgrade_costs}, your sword damage for "
          f"{sword_upgrade_costs}, or you bow damage for {bow_upgrade_costs}?")
    shop_choice = input("(armor/sword/bow)")

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
    else:
        choice = "adventure"

while choice == "adventuring":
    level_map = Forest()
    enemy_list = [Zombie(), Skeleton()]
    enemy = random.choice(enemy_list)
    print(player.hp)
    first_choice = input(f"You encounter a {enemy}, what do you do? (run/fight)").lower()
    if first_choice == "run":
        battle = False

    else:
        while battle:
            print(player.hp)
            attack_weapon = input("Would you like to use your sword or bow?").lower()

            if attack_weapon == "bow":
                attack = bow.damage
                enemy.damage(attack)
                if round_num > 1:
                    player.damage(enemy.ap)
                    round_num += 1

            if attack_weapon == "sword":
                attack = sword.damage
                enemy.damage(attack)
                player.damage(enemy.ap)
                round_num += 1

            if enemy.hp <= 0:
                player.gold += enemy.gold
                battle = False
                print(player.gold)
                print(player.hp)
                cont = input("Countinue on the path? (yes/no)")
                if cont == "no":
                    choice = "shopping"
