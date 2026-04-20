
"""Main game file that runs the adventure game."""

import json
import os
import gamefunctions


def save_game(state, filename):
    """Save the game state to a file."""
    with open(filename, "w") as file:
        json.dump(state, file)


def load_game(filename):
    """Load the game state from a file."""
    with open(filename, "r") as file:
        state = json.load(file)
    return state


def main():
    
    print("1) New Game")
    print("2) Load Game")
    start_choice = input("Enter choice: ")

    if start_choice == "2":
        filename = input("Enter save file name: ")

        if os.path.exists(filename):
            state = load_game(filename)
            print("Game loaded successfully!")
        else:
            print("Save file not found. Starting a new game.")
            player_name = input("Enter your name: ")
            state = gamefunctions.create_new_state(player_name)
    else:
        player_name = input("Enter your name: ")
        state = gamefunctions.create_new_state(player_name)

    keep_playing = True

    while keep_playing:
        gamefunctions.print_main_menu(state["player_hp"], state["player_gold"])
        user_choice = gamefunctions.get_main_menu_choice()
        if user_choice == "1":
            result = gamefunctions.run_map(state)
        
            if result == "monster":
                state = gamefunctions.fight_monster(state)
                gamefunctions.place_new_monster(state)
            
        elif user_choice == "2":
            state["player_hp"], state["player_gold"] = gamefunctions.sleep_in_town(
                state["player_hp"], state["player_gold"]
            )
        elif user_choice == "3":

            print("Shop:")
            print("1) Sword - 10 Gold")
            print("2) Magic Bomb - 10 Gold")

            shop_choice = int(input("Enter choice: "))
            gamefunctions.buy_item(state, shop_choice)
            
        elif user_choice == "4":
            gamefunctions.show_inventory(state)

        elif user_choice == "5":
            gamefunctions.equip_weapon(state)

        elif user_choice == "6":
            filename = input("Enter save file name: ")
            save_game(state, filename)
            print("Game saved.")
            print("Thanks for playing!")
            keep_playing = False


if __name__ == "__main__":
    main()
