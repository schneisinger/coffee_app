"""Doc string for modules"""
import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO Test for FastAPI





coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# Initialize 
MACHINE_RUNNING = True
os.system('cls')

while MACHINE_RUNNING:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "off":
        MACHINE_RUNNING = False
        print("Ok, bye.")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        refill_item = input("Which ingredient would you like to refill? (water, milk, coffee): ")
        refill_amount = int(input("How much would you like to refill? (ml/g): "))
        coffee_maker.resources[refill_item] += refill_amount
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        