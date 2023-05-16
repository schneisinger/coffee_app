# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""Doc string for modules"""
import os
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from typing import Union
import asyncio


#TODO Test for FastAPImissing-class-docstring

class Unit(Enum):
    GRAMM ="g"
    MILLILITER = "ml"

class Euro(Enum):
    CURRENCY ="Euro"

class Ingredient(BaseModel):
    name: str
    amount: int
    unit: Unit

test = [
    {"name": "test", "price": 7, "type": "maybe"},
    {"name": "test", "price": 7, "type": "maybe"},
    {"name": "test", "price": 7, "type": "maybe"},
    {"name": "test", "price": 7, "type": "maybe"}
]

app = FastAPI()


@app.get("/test/")
async def testit():
    return test




### 23 05 16 - old code below

# coffee_maker = CoffeeMaker()
# money_machine = MoneyMachine()
# menu = Menu()
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
#         refill_item = input("Which ingredient would you like to refill? (water, milk, coffee): ")
#         refill_amount = int(input("How much would you like to refill? (ml/g): "))
#         coffee_maker.resources[refill_item] += refill_amount
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
        