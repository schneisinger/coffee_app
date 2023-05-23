# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""Doc string for modules"""
# import os
from enum import Enum
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel, Field
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Define data types:
class IngredientUnit(Enum):
    GRAMM ="g"
    MILLILITER = "ml"

class Ingredients(str, Enum):
    WATER = "water"
    MILK = "milk"
    COFFEE = "coffee"

class IngredientAmount(BaseModel):
    amount: int = Field(100, gt=0, lt=9999)


# FastAPI: 
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello Coffee!"}


@app.get("/menu/")
async def get_menu():
    """Returns items on the menu with prices."""
    return menu.get_items()


@app.get("/coffee_maker/")
async def get_report():
    """Returns available ingredient-resources."""
    report = coffee_maker.resources
    return report


@app.get("/money_machine/")
async def get_money_report():
    """Returns current money in machine."""
    report = f"{money_machine.CURRENCY} {money_machine.profit}"
    return report


@app.put("/coffe_maker/")
async def update_resources(ingredient: Ingredients, amount: IngredientAmount):
    """Takes ingredient and amount as user input to refill resources."""
    coffee_maker.refill(ingredient, amount.amount)
    return coffee_maker.resources[ingredient]


@app.post("/money_machine/profit/")
async def update_profit():
    """Sends the current profit to the client."""
    money_machine.profit += 1           ## TODO nur Test!
    profit = money_machine.profit
    return profit


# @app.put("/coffe_maker/{ingr_id}")
# async def update_resources(ingr_id: Ingredients, item):
#     coffee_maker.resources[ingr_id] = item

### 23 05 16 - old code below

# # Initialize
# MACHINE_RUNNING = True
# os.system('cls')

# while MACHINE_RUNNING:
#     options = menu.get_items()
#     choice = input(f"What would you like? {options}: ").lower()
#     if choice == "off":
#         MACHINE_RUNNING = False
#         print("Ok, bye.")
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     elif choice == "refill":
#        TODO Durch coffe_maker.refill ersetzen 
#         refill_item = input("Which ingredient would you like to refill? (water, milk, coffee): ")
#         refill_amount = int(input("How much would you like to refill? (ml/g): "))
#         coffee_maker.resources[refill_item] += refill_amount
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
