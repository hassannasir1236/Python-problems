MENU = {
    "espresso": {"water": 50, "coffee": 18, "milk": 0, "cost": 1.5},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "cost": 2.5},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "cost": 3.0}
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

profit = 0

def report():
    print("\n--- REPORT ---")
    print("Water:", resources["water"])
    print("Milk:", resources["milk"])
    print("Coffee:", resources["coffee"])
    print("Money: $", profit)
    
def is_resource_sufficient(drink):
    for item in MENU[drink]:
        if item == "cost":
            continue
        if resources[item] < MENU[drink][item]:
            print(f"Sorry not enough {item}")
            return False
    return True
    
def process_coins():
    print("Insert coins:")
    total = (
        float(input("quarters: ")) * 0.25 +
        float(input("dimes: ")) * 0.10 +
        float(input("nickels: ")) * 0.05 +
        float(input("pennies: ")) * 0.01
    )
    return total
  
def make_coffee(drink):
    for item in MENU[drink]:
        if item != "cost":
            resources[item] -= MENU[drink][item]
    print(f"Here is your {drink} ☕")
    
  
  
running = True

while running:

    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        running = False

    elif choice == "report":
        report()

    elif choice in MENU:

        if is_resource_sufficient(choice):

            payment = process_coins()
            cost = MENU[choice]["cost"]

            if payment >= cost:
                change = round(payment - cost, 2)
                print(f"Here is ${change} in change")

                profit += cost
                make_coffee(choice)

            else:
                print("Sorry not enough money. Money refunded.")  
  
  
  
  
  
  
  
  
  
    
    