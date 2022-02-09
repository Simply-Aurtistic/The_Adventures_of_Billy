
import pandas
from shop import Shop

round_num = 1
game_is_on = True
shop = Shop()


while game_is_on:
    print("\n")
    print("You arrive back at base")
    hp = shop.max_health
    choice = input("would you like to go shopping, adventuring, go back to the inn to save, of get info? "
                   "(shop/adventure/inn/info): ").lower()
    print("\n")
    while choice not in ["shop", "adventure", "inn", "info"]:
        print("Try to keep to right choices.")
        choice = input("would you like to go shopping, adventuring, or pause for now? (shop/adventure/pause): ").lower()
        print("\n")
    if choice == "info":
        print(f"bow: get a free round of damage if used first in battle, current damage is: {shop.bowdamage}, and costs"
              f" {shop.bow_upgrade_costs} gold to upgrade.\n"
              f"sword: provides minimal defense (1/4 of sword damage), current damage is: {shop.sworddamage}, and costs"
              f" {shop.sword_upgrade_costs} gold to upgrade\n"
              f"armor: reduces damage from enemies, current armor is: {shop.defense}, and costs "
              f"{shop.armor_upgrade_costs} gold to upgrade\n"
              f"health: health is base 10 and increases by a random amount up to 3 points, current max health is: "
              f"{shop.max_health},\n and costs {shop.health_upgrade_costs} gold to upgrade\n"
              f"low potion: adds 1 to 4 temporary health points and costs 5 gold.\n"
              f"high potion: adds 10 to 15 temporary health  points and costs 20 gold.")

    while choice == "shop":

        shop.store()
        choice = "back"

    while choice == "adventure":
        from battle import Battle
        battle_cry = Battle(shop)
        battle_cry.adventures()
        choice = "back"
    if choice == "inn":
        game_is_on = False

print(f"current save name is {shop.game_load}\n"
      f"please don't save over the start file\n"
      f"game saves as lowercase name")
save_game_name = input("What is the save name?: ").lower() + ".csv"

save_game = {
    "variable": ["hp", "huc", "suc", "buc", "auc", "gold", "sword", "bow", "defense", "low_potion", "high_potion"],
    "values": [shop.max_health, shop.health_upgrade_costs, shop.sword_upgrade_costs, shop.bow_upgrade_costs,
               shop.armor_upgrade_costs, shop.gold, shop.sworddamage, shop.bowdamage, shop.defense, shop.low_potion,
               shop.high_potion]
    }
save_data = pandas.DataFrame(save_game)
save_data.to_csv(save_game_name)

