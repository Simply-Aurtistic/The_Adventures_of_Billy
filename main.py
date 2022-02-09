
import pandas
from shop import Shop

round_num = 1
game_is_on = True
shop = Shop()


shop.store()

while game_is_on:
    print("You arrive back at base")
    hp = shop.max_health
    choice = input("would you like to go shopping, adventuring, or go back to the inn to save? (shop/adventure/inn): ").lower()
    while choice not in ["shop", "adventure", "inn"]:
        print("Try to keep to right choices.")
        choice = input("would you like to go shopping, adventuring, or pause for now? (shop/adventure/pause): ").lower()

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

save_game_name = input("What is the save name?: ").lower() + ".csv"

save_game = {
    "variable": ["hp", "huc", "suc", "buc", "auc", "gold", "sword", "bow", "defense"],
    "values": [shop.max_health, shop.health_upgrade_costs, shop.sword_upgrade_costs, shop.bow_upgrade_costs,
               shop.armor_upgrade_costs, shop.gold, shop.sworddamage, shop.bowdamage, shop.defense]
    }
save_data = pandas.DataFrame(save_game)
save_data.to_csv(save_game_name)
