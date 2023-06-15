# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""Doc string for modules"""
# import os
from enum import Enum
import asyncio
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Template
from pydantic import BaseModel, Field
from coffee.coffee_maker import CoffeeMaker
from coffee.money_machine import MoneyMachine


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

app.mount("/static", StaticFiles(packages=[('coffee', 'static')]), name="static")

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "menu": menu})


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


@app.put("/coffee_maker/")
async def refill_resources(data: dict):
    """Takes ingredient and amount as user input to refill resources."""
    for ingr, amount in data.items():
            coffee_maker.refill(ingr, amount)
    return coffee_maker.resources


@app.put("/menu/")
async def add_recipe(data: dict):
    """Takes user input and edits or creates a recipe."""
    exists = False
    i = 0
    for item in menu:
        if item["name"] == data["name"].lower():
            item.update({"name": data["name"], "water": data["water"], "milk": data["milk"], "coffee": data["coffee"], "price": data["price"]})
            exists = True
            result = menu[i]
        if not exists:
            i += 1
    if not exists:
        menu.append(data)
        result = menu[-1]
    return result


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
