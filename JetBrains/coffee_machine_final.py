import sys

espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}


def check_resource(res_avail, coffee, resource):
    if (res_avail - coffee[resource]) < 0:
        print(f"Sorry, not enough {resource}!")
        return 1


def user_input():
    command = input()
    if command[0] in "1234567890":
        return int(command)
    else:
        return command


class CoffeeMachine:

    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    while True:
        print("Write action (buy, fill, take, remaining, exit): ")
        action = user_input()
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            choice = user_input()
            if choice == 1:
                if check_resource(water, espresso, 'water') == 1:
                    continue
                if check_resource(milk, espresso, 'milk') == 1:
                    continue
                if check_resource(beans, espresso, 'beans') == 1:
                    continue
                print("I have enough resources, making you a coffee!")
                water -= espresso['water']
                milk -= espresso['milk']
                beans -= espresso['beans']
                cups -= 1
                money += espresso['cost']
            elif choice == 2:
                if check_resource(water, latte, 'water') == 1:
                    continue
                elif check_resource(milk, latte, 'milk') == 1:
                    continue
                elif check_resource(beans, latte, 'beans') == 1:
                    continue
                print("I have enough resources, making you a coffee!")
                water -= latte['water']
                milk -= latte['milk']
                beans -= latte['beans']
                cups -= 1
                money += latte['cost']
            elif choice == 3:
                if check_resource(water, cappuccino, 'water') == 1:
                    continue
                elif check_resource(milk, cappuccino, 'milk') == 1:
                    continue
                elif check_resource(beans, cappuccino, 'beans') == 1:
                    continue
                print("I have enough resources, making you a coffee!")
                water -= cappuccino['water']
                milk -= cappuccino['milk']
                beans -= cappuccino['beans']
                cups -= 1
                money += cappuccino['cost']
            elif choice == 'back':
                continue
        elif action == "fill":
            print("Write how many ml of water you want to add: ")
            water += (user_input())
            print("Write how many ml of milk you want to add: ")
            milk += (user_input())
            print("Write how many grams of coffee beans you want to add: ")
            beans += (user_input())
            print("Write how many disposable cups of coffee you want to add: ")
            cups += (user_input())
        elif action == "take":
            print(f"I gave you ${money}")
            money = 0
        elif action == "remaining":
            print(f"""
            The coffee machine has:
            {water} ml of water
            {milk} ml of milk
            {beans} g of coffee beans
            {cups} disposable cups
            ${money} of money \n
            """)
        elif action == "exit":
            sys.exit()