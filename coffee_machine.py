water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups_of_coffee = int(input("Write how many cups of coffee you will need:\n"))
cups = 0
while water > 199 and milk > 49 and coffee_beans > 14:
    cups += 1
    water -= 200
    milk -= 50
    coffee_beans -= 15
if cups == cups_of_coffee:
    print("Yes, I can make that amount of coffee")
elif cups > cups_of_coffee:
    print(f"Yes, I can make that amount of coffee (and even {cups - cups_of_coffee} more than that)")
elif cups < cups_of_coffee:
    print(f"No, I can make only {cups} cups of coffee")
