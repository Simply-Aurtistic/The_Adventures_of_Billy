
import pandas
from shop import Shop

round_num = 1
game_is_on = True
shop = Shop()

print("As you enter Trevoria, a small quiet town, you are greeted by a old man. \n"
      "'Welcome to our fair little town.' He looks around a bit then continues 'We have been plagued by a monster "
      "horde of late.' \n"
      "He looks at your sword. 'Perhaps you can help us with this problem. You look capable enough at least. \n"
      "If you are looking for upgrades for your equipment, Buzz can help you over in his shop, the Iron Maiden'\n"
      "You head over to the Iron Maiden. As you walk through the door, you are greeted by a big gruff man. \n"
      "'Hello my name is Beelzebub, but you can call me Buzz. You must be that new adventurer I have heard about' \n"
      "Buzz turns and gets back behind the counter. 'What can i get for you today.'")
shop.store()

while game_is_on:
    print("You arrive back at base")
    hp = shop.max_health
    choice = input("would you like to go shopping, adventuring, or go back to the inn? (shop/adventure/inn): ").lower()
    while choice not in ["shop", "adventure", "pause"]:
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
