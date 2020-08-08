class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def start(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action.__eq__("buy"):
                CoffeeMachine.buy_coffee(self)
            elif action.__eq__("fill"):
                CoffeeMachine.fill_coffee_machine(self)
            elif action.__eq__("take"):
                CoffeeMachine.take_money(self)
            elif action.__eq__("remaining"):
                CoffeeMachine.remaining(self)
            elif action.__eq__("exit"):
                break

    def buy_coffee(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        if choice.__eq__("back"):
            return
        elif int(choice) == 1:
            if self.water - 250 < 0:
                print("Sorry, not enough water!")
            elif self.coffee_beans - 16 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
        elif int(choice) == 2:
            if self.water - 350 < 0:
                print("Sorry, not enough water!")
            elif self.milk - 75 < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - 20 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
        elif int(choice) == 3:
            if self.water - 200 < 0:
                print("Sorry, not enough water!")
            elif self.milk - 100 < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - 12 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
        print()

    def fill_coffee_machine(self):
        print()
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())
        print()

    def take_money(self):
        print(f"""
    I gave you ${self.money}
    """)
        self.money -= self.money

    def remaining(self):
        print(f"""
    The coffee machine has:
    {self.water} of water
    {self.milk} of milk
    {self.coffee_beans} of coffee beans
    {self.cups} of disposable cups
    ${self.money} of money
    """)


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(water=400, milk=540, coffee_beans=120, cups=9, money=550)
    coffee_machine.start()
