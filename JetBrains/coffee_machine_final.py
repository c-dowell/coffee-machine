import sys

espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}


class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.money = water
        self.cups = milk
        self.beans = beans
        self.milk = cups
        self.water = money

    @staticmethod
    def check_resource(res_avail, coffee, resource):
        if (res_avail - coffee[resource]) < 0:
            print(f"Sorry, not enough {resource}!")
            return 1

    @staticmethod
    def user_input():
        command = input()
        if command[0] in "1234567890":
            return int(command)
        else:
            return command

    def run_machine(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit): ")
            action = self.user_input()
            if action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
                choice = self.user_input()
                if choice == 1:
                    if self.check_resource(self.water, espresso, 'water') == 1:
                        continue
                    if self.check_resource(self.milk, espresso, 'milk') == 1:
                        continue
                    if self.check_resource(self.beans, espresso, 'beans') == 1:
                        continue
                    print("I have enough resources, making you a coffee!")
                    self.water -= espresso['water']
                    self.milk -= espresso['milk']
                    self.beans -= espresso['beans']
                    self.cups -= 1
                    self.money += espresso['cost']
                elif choice == 2:
                    if self.check_resource(self.water, latte, 'water') == 1:
                        continue
                    elif self.check_resource(self.milk, latte, 'milk') == 1:
                        continue
                    elif self.check_resource(self.beans, latte, 'beans') == 1:
                        continue
                    print("I have enough resources, making you a coffee!")
                    self.water -= latte['water']
                    self.milk -= latte['milk']
                    self.beans -= latte['beans']
                    self.cups -= 1
                    self.money += latte['cost']
                elif choice == 3:
                    if self.check_resource(self.water, cappuccino, 'water') == 1:
                        continue
                    elif self.check_resource(self.milk, cappuccino, 'milk') == 1:
                        continue
                    elif self.check_resource(self.beans, cappuccino, 'beans') == 1:
                        continue
                    print("I have enough resources, making you a coffee!")
                    self.water -= cappuccino['water']
                    self.milk -= cappuccino['milk']
                    self.beans -= cappuccino['beans']
                    self.cups -= 1
                    self.money += cappuccino['cost']
                elif choice == 'back':
                    continue
            elif action == "fill":
                print("Write how many ml of water you want to add: ")
                self.water += (self.user_input())
                print("Write how many ml of milk you want to add: ")
                self.milk += (self.user_input())
                print("Write how many grams of coffee beans you want to add: ")
                self.beans += (self.user_input())
                print("Write how many disposable cups of coffee you want to add: ")
                self.cups += (self.user_input())
            elif action == "take":
                print(f"I gave you ${self.money}")
                self.money = 0
            elif action == "remaining":
                print(f"""
                The coffee machine has:
                {self.water} ml of water
                {self.milk} ml of milk
                {self.beans} g of coffee beans
                {self.cups} disposable cups
                ${self.money} of money \n
                """)
            elif action == "exit":
                sys.exit()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.run_machine()