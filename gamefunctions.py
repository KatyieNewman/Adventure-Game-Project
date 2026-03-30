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
    print("1) Fight a monster?")
    print("2) Sleep. (Restore HP for 5 Gold)")
    print("3) Quit")


def get_main_menu_choice():
    
    """Gets a valid menu choice."""
    
    choice = input("Enter choice: ")

    while choice not in ["1", "2", "3"]:
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


def get_fight_choice():
    
    """Gets a fight choice."""
    
    choice = input("Enter choice: ")

    while choice not in ["1", "2"]:
        print("Invalid choice. Try again.")
        choice = input("Enter choice: ")

    return choice


def fight_monster(player_hp, player_gold):
    
    """fight loop."""
    
    monster = random_monster()

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
            monster_hp -= 5

            if monster_hp > 0:
                print(f"The {monster_name} strikes you!")
                player_hp -= monster_power

        elif choice == "2":
            print("You run away!")
            break

    if player_hp <= 0:
        print("You lost the fight.")
        player_hp = 30
        print("You wake up back in town.")

    elif monster_hp <= 0:
        print("You won the fight!")
        player_gold += 5
        print("You found 5 gold.")

    return player_hp, player_gold















    




    
    
