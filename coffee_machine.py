water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def buy_coffee():
    global water
    global milk
    global coffee_beans
    global cups
    global money
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()
    if choice.__eq__("back"):
        return
    elif int(choice) == 1:
        if water - 250 < 0:
            print("Sorry, not enough water!")
        elif coffee_beans - 16 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee_beans -= 16
            cups -= 1
            money += 4
    elif int(choice) == 2:
        if water - 350 < 0:
            print("Sorry, not enough water!")
        elif milk - 75 < 0:
            print("Sorry, not enough milk!")
        elif coffee_beans - 20 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 7
    elif int(choice) == 3:
        if water - 200 < 0:
            print("Sorry, not enough water!")
        elif milk - 100 < 0:
            print("Sorry, not enough milk!")
        elif coffee_beans - 12 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee_beans -= 12
            cups -= 1
            money += 6
    print()


def fill_coffee_machine():
    global water
    global milk
    global coffee_beans
    global cups
    print()
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())
    print()


def take_money():
    global money
    print(f"""
I gave you ${money}
""")
    money -= money


def remaining():
    global water
    global milk
    global coffee_beans
    global cups
    global money
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
${money} of money
""")


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action.__eq__("buy"):
        buy_coffee()
    elif action.__eq__("fill"):
        fill_coffee_machine()
    elif action.__eq__("take"):
        take_money()
    elif action.__eq__("remaining"):
        remaining()
    elif action.__eq__("exit"):
        break
