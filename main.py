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
    "cappucino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_suff(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there isn't enough {item}.")
            is_enough = False
    return is_enough


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    quarters_ct = int(input("How many quarters do you have? ")) * .25
    dimes_ct = int(input("How many dimes do you have? ")) * .1
    nickels_ct = int(input("How many nickels do you have? ")) * .05
    pennies_ct = int(input("How many penies do you have? ")) * .01
    money = quarters_ct + dimes_ct + nickels_ct + pennies_ct
    return money


def transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    """Deduct required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")

power = True

while power:
    choice = input("What would you like? (espresso/latte/cappucino): ").lower()
    if choice == "off":
        power = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_suff(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])


