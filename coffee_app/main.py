from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Initialize 
machine_running = True 
os.system('cls')

while machine_running: 
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "off":
        machine_running = False
        print("Ok, bye.") 
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        refill_item = input(f"Which ingredient would you like to refill? (water, milk, coffee): ")
        refill_amount = int(input(f"How much would you like to refill? (ml/g): "))
        coffee_maker.resources[refill_item] += refill_amount
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        
