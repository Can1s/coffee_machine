water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def buy_coffee():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = int(input())
    if choice == 1:
        print(f"""
The coffee machine has:
{water - 250} of water
{milk} of milk
{coffee_beans - 16} of coffee beans
{cups - 1} of disposable cups
{money + 4} of money""")
    elif choice == 2:
        print(f"""
The coffee machine has:
{water - 350} of water
{milk - 75} of milk
{coffee_beans - 20} of coffee beans
{cups - 1} of disposable cups
{money + 7} of money""")
    elif choice == 3:
        print(f"""
The coffee machine has:
{water - 200} of water
{milk - 100} of milk
{coffee_beans - 12} of coffee beans
{cups - 1} of disposable cups
{money + 6} of money""")


def fill_coffee_machine(wtr, mlk, beans, cps, mn):
    print("Write how many ml of water do you want to add:")
    wtr += int(input())
    print("Write how many ml of milk do you want to add:")
    mlk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cps += int(input())
    print(f"""
The coffee machine has:
{wtr} of water
{mlk} of milk
{beans} of coffee beans
{cps} of disposable cups
{mn} of money""")


def take_money(wtr, mlk, beans, cps, mn):
    print(f"I gave you ${mn}")
    mn = 0
    print(f"""
The coffee machine has:
{wtr} of water
{mlk} of milk
{beans} of coffee beans
{cps} of disposable cups
{mn} of money""")


print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
{money} of money""")


print("Write action (buy, fill, take):")
action = input()
if action.__eq__("buy"):
    buy_coffee()
elif action.__eq__("fill"):
    fill_coffee_machine(water, milk, coffee_beans, cups, money)
elif action.__eq__("take"):
    take_money(water, milk, coffee_beans, cups, money)
