# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""Doc string for modules"""
# import os
from enum import Enum
import asyncio
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Template
from pydantic import BaseModel, Field
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

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
    
class IngredientPrice(BaseModel):    
    cost: float = Field(2.5, gt=0, lt=10)

class Recipe(BaseModel):
    water: int = Field(100, gt=0, lt=9999)
    milk: int = Field(100, gt=0, lt=9999)
    coffee: int = Field(100, gt=0, lt=9999)
    cost: float = Field(2.5, gt=0, lt=10)

class MenuItem():
    name = str
    price = IngredientPrice
    ingredients = {
        Ingredients.WATER: IngredientAmount,
        Ingredients.MILK: IngredientAmount,
        Ingredients.COFFEE: IngredientAmount
    }

menu = [
    {"name":"latte", "water": 200, "milk": 150, "coffee": 24, "price": 2.5},
    {"name":"espresso", "water": 50, "milk": 0, "coffee": 18, "price": 1.5},
    {"name":"americano", "water": 125, "milk": 0, "coffee": 36, "price": 2.25},
    {"name":"cappuccino", "water": 75, "milk": 100, "coffee": 24, "price": 3.75},
    ]


# FastAPI:
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    ON = True
    return templates.TemplateResponse("index.html", {"request": request, "menu": menu, "ON": ON})


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


@app.put("/coffe_maker/{ingredient}")
async def refill_resources(ingredient: Ingredients, amount: IngredientAmount):
    """Takes ingredient and amount as user input to refill resources."""
    coffee_maker.refill(ingredient, amount.amount)
    return coffee_maker.resources[ingredient]


# @app.post("/menu/recipes/")
# async def add_recipe(menu_item: MenuItem):
#     """Takes user input and creats a new recipe."""
#     new_menu_item = menu_item
#     menu.append(new_menu_item)
#     return menu


@app.post("/money_machine/profit/")
async def update_profit():
    """Sends the current profit to the client."""
    money_machine.profit += 1           ## TODO nur Test!
    profit = money_machine.profit
    return profit

# ___________________________________________________________

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
