
"""Main game file that runs the adventure game."""

import gamefunctions


def main():
    player_name = input("Enter your name: ")
    state = gamefunctions.create_new_state(player_name)
    keep_playing = True

    while keep_playing:
        gamefunctions.print_main_menu(state["player_hp"], state["player_gold"])
        user_choice = gamefunctions.get_main_menu_choice()

        if user_choice == "1":
            state = gamefunctions.fight_monster(state)
            
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
            print("Thanks for playing!")
            keep_playing = False


if __name__ == "__main__":
    main()
