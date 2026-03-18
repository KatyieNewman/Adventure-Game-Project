"""Game that uses functions from gamefunctions.py"""

import gamefunctions

def main():
    name = input("What's your name? ")
    gamefunctions.print_welcome(name, 20)

    print("Welcome to the shop!")
    gamefunctions.print_shop_menu("64ozBeer", 11, "BugSpray", 8)

    money = float(input("How much money do you have? "))
    quantity = int(input("How many oz of beer do you want? "))
    result = gamefunctions.purchase_item(11, money, quantity)

    print("You bought", result[0], "item(s).")
    print("You have", result[1], "money left.")

    print("A monster appears!")
    monster = gamefunctions.random_monster()

    print(monster["name"])
    print(monster["description"])
    print("Health:", monster["health"])
    print("Power:", monster["power"])
    print("Money:", monster["money"])

if __name__ == "__main__":
    main()
