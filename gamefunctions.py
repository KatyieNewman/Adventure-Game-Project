"""Functions used for a simple adventure game.

This file contains helper functions for the game.
It includes functions for printing a welcome message,
printing a shop menu, calculating purchases, and
generating a random monster.
"""

import random

def purchase_item(item_price, starting_money,quantity_to_purchase=1):
    """
    Calculates how many items can be purchased and how much money remains.

    Parameters:
        item_price (float/int)
        starting_money (float/int)
        quantity_to_purchase (int, default=1)

    Returns:
        (quantity_purchased, remaining_money)
    """
    max_affordable = starting_money // item_price

    if quantity_to_purchase <= max_affordable:
        quantity_purchased = quantity_to_purchase
    else:
        quantity_purchased = max_affordable

    total_cost = quantity_purchased * item_price
    remaining_money = starting_money - total_cost
    
    return quantity_purchased, remaining_money


def random_monster():
    """
    Generates a random monster with randomized stats.

    Returns:
        dict containing name, description, health, power, and money.
    """
    monster_type = random.choice(["Dragon", "Ghost", "Witch"])
    
    if monster_type == "Dragon":
        name = "A Dragon"
        description = "A huge scaly dragon leaps from the dark and coughs a ball of fire at you."
        health = random.randint(50,100)
        power = random.randint (20,100)
        money = random.randint (200,800)

    
    elif monster_type =="Ghost":
        name = "A Ghost"
        description = "A ghost sneaks up from behind and takes your most prize possession. "
        health = random.randint(1,3)
        power = random.randint (5,10)
        money = random.randint (100,250)

    else:
        name = "A Witch"
        description = "A witch casts a spell on you, turning you into a mouse."
        health = random.randint(12, 24)
        power = random.randint (5,7)
        money = random.randint (10,60)

    return{
        "name":name,
        "description":description,
        "health":health,
        "power": power,
        "money": money
    }



def print_welcome(name, width):
    """
    Prints a lovely centered welcome message.

    Parameters:
        name (str)
        width (int)
    """
    message = f"Hello, {name}!"
    print(message.center(width))

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Prints a bordered menu with two items and prices.

    Parameters:
        item1Name (str), item1Price (float)
        item2Name (str), item2Price (float)

    """
    topb = "/----------------------\\"
    bottomb = "\\----------------------/"

    price1 = f"${item1Price:.2f}"
    price2 = f"${item2Price:.2f}"

    line1 = f"| {item1Name:<12}{price1:>8} |"
    line2 = f"| {item2Name:<12}{price2:>8} |"

    print(topb)
    print(line1)
    print(line2)
    print(bottomb)

def test_functions():

	#Test purchase_item
	print("Test 1:", purchase_item(120,1000,3))
	print("Test 2: (cannot afford all):", purchase_item(10,45,6))
	print("Test 3: (default quantity):", purchase_item(300,2100))


	#Test random_monster
	print("Monster 1:", random_monster())
	print("Monster 2:", random_monster())
	print("Monster 3:", random_monster())

	#Test print_welcome
	print_welcome("Beans", 16)
	print_welcome("Kaytie", 13)
	print_welcome("Lilly", 8)

	#Test print_shop_menu
	print_shop_menu("32ozBeer", 6, "Coffee", 2.50)
	print_shop_menu("64ozBeer", 11, "BowloBeans", 2)
	print_shop_menu("BugSpray", 8, "Floss", 1)

if __name__ == "__main__":
    test_functions()







### ---------------- NEW GAME FUNCTIONS ----------------###



def print_main_menu(current_hp, current_gold):
    
    """Prints the main menu in town."""
    
    print()
    print("You are in a stinky town.")
    print(f"HP: {current_hp}, Gold: {current_gold}")
    print("What do you want to do?")
    print("1) Time to Explore?")
    print("2) Sleep. (Restore HP for 5 Gold)")
    print("3) Visit Shop")
    print("4) Show Inventtory")
    print("5) Equipt Weapon")
    print("6) Quit AND save")


def get_main_menu_choice():
    
    """Gets a valid menu choice."""
    
    choice = input("Enter choice: ")

    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("That is not a valid option. Try again.")
        choice = input("Enter choice: ")

    return choice


def sleep_in_town(current_hp, current_gold):
    
    """Restores HP if player has enough gold."""
    
    if current_gold >= 5:
        current_gold -= 5
        current_hp = 30
        print("You take a snooze. You feel much better.")
    else:
        print("You do not have enough gold to sleep SAD...")

    return current_hp, current_gold


def display_fight_stats(player_hp, monster_name, monster_hp):
    
    """fight info."""
    
    print()
    print("Fight:")
    print(f"Your HP: {player_hp}")
    print(f"{monster_name} HP: {monster_hp}")
    print("1) Attack!")
    print("2) Run")
    print("3) Use Magic Bomb")

    


def get_fight_choice():
    
    """Gets a fight choice."""
    
    choice = input("Enter choice: ")

    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Try again.")
        choice = input("Enter choice: ")

    return choice


def fight_monster(state):
    
    """fight loop."""
    
    monster = random_monster()

    player_hp = state["player_hp"]
    player_gold = state["player_gold"]

    monster_name = monster["name"]
    monster_hp = monster["health"]
    monster_power = monster["power"]

    print()
    print(f"A {monster_name} appears!")

    while player_hp > 0 and monster_hp > 0:
        display_fight_stats(player_hp, monster_name, monster_hp)
        choice = get_fight_choice()

        if choice == "1":
            print("You attack!")
            damage = 5 + get_weapon_damage(state)
            monster_hp -= damage

            if monster_hp > 0:
                print(f"The {monster_name} strikes you!")
                player_hp -= monster_power

        elif choice == "2":
            print("You run away!")
            break
        
        elif choice == "3":
            used_bomb = use_magic_bomb(state)

            if used_bomb:
                monster_hp = 0

    if player_hp <= 0:
        print("You lost the fight.")
        player_hp = 30
        print("You wake up back in town.")

    elif monster_hp <= 0:
        print("You won the fight!")
        player_gold += 5
        print("You found 5 gold.")

    state["player_hp"] = player_hp
    state["player_gold"] = player_gold

    return state



### ---------------------Inventory List (Project)-----------------------###


def create_new_state(player_name):
    
    """
    Creates a dictionary to store all game information.
    """

    state = {
        "player_name": player_name,
        "player_gold": 100,
        "player_hp": 30,
        "player_inventory": [],
        "equipped_weapon": None,
        "map_state": {
            "player_x": 0,
            "player_y": 0,
            "town_x": 0,
            "town_y": 0,
            "monster_x": 4,
            "monster_y": 4

        }   
    }

    return state

def move_player(game_state, direction):
    
    """
    Moves the player one space on the map.
    Returns:
        "moved"
        "town"
        "monster"
    """

    map_state = game_state["map_state"]

    if direction == "up" and map_state["player_y"] > 0:
        map_state["player_y"] -= 1

    elif direction == "down" and map_state["player_y"] < 9:
        map_state["player_y"] += 1

    elif direction == "left" and map_state["player_x"] > 0:
        map_state["player_x"] -= 1

    elif direction == "right" and map_state["player_x"] < 9:
        map_state["player_x"] += 1

    if (map_state["player_x"] == map_state["town_x"] and
        map_state["player_y"] == map_state["town_y"]):
        return "town"

    if (map_state["player_x"] == map_state["monster_x"] and
        map_state["player_y"] == map_state["monster_y"]):
        return "monster"

    return "moved"

def print_map(game_state):
    
    """
    Prints the 10x10 map.
    """

    map_state = game_state["map_state"]

    for y in range(10):
        for x in range(10):
            if x == map_state["player_x"] and y == map_state["player_y"]:
                print("P", end="")
            elif x == map_state["town_x"] and y == map_state["town_y"]:
                print("T", end="")
            elif x == map_state["monster_x"] and y == map_state["monster_y"]:
                print("M", end="")
            else:
                print(".", end="")
        print()


def run_map(game_state):
    
    """
    Runs the map until the player reaches town or monster.
    """

    while True:
        print()
        print("WORLD MAP")
        print_map(game_state)
        print("Use w a s d to move")

        choice = input("Enter move: ")

        if choice == "w":
            result = move_player(game_state, "up")
        elif choice == "s":
            result = move_player(game_state, "down")
        elif choice == "a":
            result = move_player(game_state, "left")
        elif choice == "d":
            result = move_player(game_state, "right")
        else:
            print("Invalid move.")
            continue

        if result == "town":
            return "town"
        elif result == "monster":
            return "monster"

def place_new_monster(game_state):
    
    """
    Places the monster in a new random square.
    """

    map_state = game_state["map_state"]

    new_x = random.randint(0, 9)
    new_y = random.randint(0, 9)

    while ((new_x == map_state["town_x"] and new_y == map_state["town_y"]) or
           (new_x == map_state["player_x"] and new_y == map_state["player_y"])):
        new_x = random.randint(0, 9)
        new_y = random.randint(0, 9)

    map_state["monster_x"] = new_x
    map_state["monster_y"] = new_y




def create_sword():
    
    """
    Creates a sword.
    """

    sword = {
        "name": "Sword",
        "type": "weapon",
        "maxDurability": 5,
        "currentDurability": 5,
        "equipped": False
    }

    return sword




def create_magic_bomb():
    
    """
    Creates a magicbomb.
    """

    magic_bomb = {
        "name": "Magic Bomb",
        "type": "special",
        "effect": "auto_win"
    }

    return magic_bomb



def get_shop_items():
    
    """
    Returns whats in the shop.
    """

    shop_items = [
        create_sword(),
        create_magic_bomb()
    ]

    return shop_items

    

def show_inventory(state):
    
    """
    Prints players inventory.
    """

    print("Inventory:")

    if len(state["player_inventory"]) == 0:
        print("Your inventory is empty.")
    else:
        for item in state["player_inventory"]:
            print(item["name"])



def buy_item(state, choice):
    
    """
    Buy an item from the shop.
    """

    shop_items = get_shop_items()

    if choice < 1 or choice > len(shop_items):
        print("That is not a valid option.")
        return

    item = shop_items[choice - 1]

    if state["player_gold"] >= 10:
        state["player_gold"] -= 10

        state["player_inventory"].append(item)

        print(f"You bought a {item['name']}.")
    else:
        print("You do not have enough gold.")
        

def use_magic_bomb(state):
    
    """
    Uses a magic bomb if the player has one.
    Removes it from inventory.
    Returns True if used, False if not.
    """

    for item in state["player_inventory"]:
        if item["name"] == "Magic Bomb":
            state["player_inventory"].remove(item)
            print("You used a Magic Bomb! BOOM 💥")
            return True

    print("You do not have a Magic Bomb.")
    return False


def equip_weapon(state):
    
    """
    Lets the player equip a weapon from inventory.
    """

    weapon_list = []

    for item in state["player_inventory"]:
        if item["type"] == "weapon":
            weapon_list.append(item)

    if len(weapon_list) == 0:
        print("You have no weapons to equip.")
        return

    print("Weapons:")

    for i in range(len(weapon_list)):
        print(f"{i + 1}) {weapon_list[i]['name']}")

    choice = int(input("Enter choice: "))

    if choice < 1 or choice > len(weapon_list):
        print("That is not a valid option.")
        return

    for item in state["player_inventory"]:
        if item["type"] == "weapon":
            item["equipped"] = False

    weapon_list[choice - 1]["equipped"] = True
    state["equipped_weapon"] = weapon_list[choice - 1]["name"]

    print(f"You equipped {state['equipped_weapon']}.")


def get_weapon_damage(state):
    """
    Returns extra damage from an equipped weapon.
    Also lowers durability by 1 each time it is used.
    """

    for item in state["player_inventory"]:
        if item["type"] == "weapon" and item["equipped"] is True:
            if item["currentDurability"] > 0:
                item["currentDurability"] -= 1
                print(f"You used {item['name']}.")
                print(f"{item['name']} durability is now {item['currentDurability']}.")
                return 5
            else:
                print(f"Your {item['name']} is broken.")
                item["equipped"] = False
                state["equipped_weapon"] = None
                return 0

    return 0
    
