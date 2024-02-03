MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_coins():
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .10
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies: ")) * .01
    return total


def is_transaction_successful(money_received, cost):
    if money_received < cost:
        print(f"You didn't put enough money. Your money has been refunded.")
        return False
    else:
        change = format(round((money_received - cost), 2), ".2f")
        print(f"Here is your change: ${change}.")
        global profit
        profit += cost
        return True


def make_coffee(drink_name, ingredients_used):
    for item in ingredients_used:
        resources[item] -= ingredients_used[item]
    print(f"Here is your {drink_name} ☕️. Enjoy! ")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"profit: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
    else:
        print("Invalid input, try again")
