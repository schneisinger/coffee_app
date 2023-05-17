# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""Doc string for modules"""
import os
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

#TODO Test for FastAPI

class Unit(Enum):
    GRAMM ="g"
    MILLILITER = "ml"

class Euro(Enum):
    CURRENCY ="Euro"

class Ingredients(str, Enum):
    water = "water"
    milk = "milk"
    coffee = "coffee"
 

class IngredientAmount(BaseModel):
    amount: int = Field(100, gt=0, lt=9999)
    #unit: Unit

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello Coffee!"}


@app.get("/menu/")
async def get_menu():
    return menu.get_items()


@app.get("/coffee_maker/")
async def get_report():
    report = coffee_maker.resources
    return report


#TODO Types Ingredients & IngredientAmount
@app.put("/coffe_maker/{ingr_id}")
async def update_resources(ingr_id, ingredient: Ingredients, amount: IngredientAmount):
    #coffee_maker.refill(ingr_id, amount)
    #report = coffee_maker.resources
    coffee_maker.resources[ingr_id] = ingredient
    return coffee_maker.resources[ingr_id]




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
