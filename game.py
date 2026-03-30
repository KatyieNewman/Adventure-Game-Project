
"""Main game file that runs the adventure game."""

import gamefunctions


def main():
    player_hp = 30
    player_gold = 10
    keep_playing = True

    while keep_playing:
        gamefunctions.print_main_menu(player_hp, player_gold)
        user_choice = gamefunctions.get_main_menu_choice()

        if user_choice == "1":
            player_hp, player_gold = gamefunctions.fight_monster(player_hp, player_gold)
        elif user_choice == "2":
            player_hp, player_gold = gamefunctions.sleep_in_town(player_hp, player_gold)
        elif user_choice == "3":
            print("Thanks for playing!")
            keep_playing = False


if __name__ == "__main__":
    main()
