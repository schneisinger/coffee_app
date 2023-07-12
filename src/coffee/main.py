# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

"""Doc string for modules"""
import re
from enum import Enum
import asyncio
from pathlib import Path
from fastapi import FastAPI, Request,HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Template
import psycopg2
import psycopg2.extras
from pydantic import BaseModel, Field, BaseSettings
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

# credentials for DB
class Config(BaseSettings):
    class Config:
        env_prefix = 'coffee_app_'
    hostname: str
    database: str = 'postgresql'
    username:str
    passwd: str
    port_id: int = 5432

COFFEE_APP_DB = 'coffee_app'

CONFIG = Config()

# Initialize DB
def initialize_db():
    conn = psycopg2.connect(host = CONFIG.hostname, user = CONFIG.username, password = CONFIG.passwd, port = CONFIG.port_id)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    conn.autocommit = True

    # cur.execute("DROP DATABASE IF EXISTS coffee_app;")    # Test wg. tox

    cur.execute("""
            SELECT * FROM pg_catalog.pg_database
            ORDER BY 1;""")

    dbs = cur.fetchall()
    db_exists = False

    for elem in dbs:
        if elem[1] == "coffee_app":
            db_exists = True

    if not db_exists:
        cur.execute("CREATE DATABASE coffee_app;")

    cur.close()
    conn.close()

    conn = psycopg2.connect(host = CONFIG.hostname, dbname = COFFEE_APP_DB, user = CONFIG.username, password = CONFIG.passwd, port = CONFIG.port_id)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    conn.autocommit = True

    cur.execute("""
            CREATE TABLE IF NOT EXISTS coffee_menu(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            water NUMERIC,
            milk NUMERIC,
            coffee NUMERIC,
            price NUMERIC NOT NULL
            );
            """)

    cur.execute("""SELECT COUNT (*)
                FROM coffee_menu;""")

    count = cur.fetchall()

    if count[0][0] == 0:
        cur.execute("""
                INSERT INTO coffee_menu(name,water,milk,coffee,price)
                VALUES('espresso',50,0,18,1.5),
                    ('latte',200,150,24,2.5),
                    ('americano',125,0,36,2.25),
                    ('cappuccino',75,100,36,3.75);
                """)

    cur.close()
    conn.close()


# FastAPI:
initialize_db()
app = FastAPI()

app.mount("/static", StaticFiles(packages=[('coffee', 'static')]), name="static")

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@app.get("/")
async def read_root(request: Request):
    conn = psycopg2.connect(host = CONFIG.hostname, dbname = COFFEE_APP_DB, user = CONFIG.username, password = CONFIG.passwd, port = CONFIG.port_id)
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM coffee_menu")
    menu = cur.fetchall()
    cur.close()
    conn.close()
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


@app.put("/coffee_maker/{order}")
async def brew_product(order: str):
    """Takes order from user and brews product if resources sufficient."""
    conn = psycopg2.connect(host = CONFIG.hostname, dbname = COFFEE_APP_DB, user = CONFIG.username, password = CONFIG.passwd, port = CONFIG.port_id)
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM coffee_menu")
    menu = cur.fetchall()

    product = re.search("(?<=brew_).*", order).group()

    choice = ""
    for drink in menu:
        if drink["name"] == product:
            choice = drink["name"]
            price = drink["price"]
    if coffee_maker.is_resource_sufficient(choice, menu):
        coffee_maker.make_coffee(choice, menu)
        money_machine.profit += price
    else:
        raise HTTPException(
            status_code=418,
            detail="Resources insufficient",
            headers={"X-Error": "Resources insufficient"},
        )
    cur.close()
    conn.close()
    return None


@app.put("/menu/")
async def add_recipe(data: dict):
    """Takes user input and edits an existing or creates a new recipe."""
    conn = psycopg2.connect(host = CONFIG.hostname, dbname = COFFEE_APP_DB, user = CONFIG.username, password = CONFIG.passwd, port = CONFIG.port_id)
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM coffee_menu")
    menu = cur.fetchall()

    exists = False
    for item in menu:
        if item["name"] == data["name"].lower():
            exists = True

    if exists:
        cur.execute("""
            UPDATE coffee_menu
            SET water=%(water)s, milk=%(milk)s, coffee=%(coffee)s, price=%(price)s
            WHERE name=%(name)s;
            """,
            {'name': data["name"], 'water': data["water"], 'milk': data["milk"], 'coffee': data["coffee"], 'price': data["price"]}
            )
        conn.commit()
    else:
        cur.execute("""
        INSERT INTO coffee_menu (name, water, milk, coffee, price)
        VALUES (%(name)s, %(water)s, %(milk)s, %(coffee)s, %(price)s);
        """,
        {'name': data["name"], 'water': data["water"], 'milk': data["milk"], 'coffee': data["coffee"], 'price': data["price"]}
        )
    cur.close()
    conn.close()
    return None


@app.delete("/menu/{product}")
async def delete_recipe(product: str):
    """User deletes a recipe by a button."""
    conn = psycopg2.connect(host = CONFIG.hostname, dbname = COFFEE_APP_DB, user = CONFIG.username, password = CONFIG.passwd, port = CONFIG.port_id)
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM coffee_menu")
    menu = cur.fetchall()

    del_product = re.search("(?<=delete_).*", product).group()

    cur.execute(
        """
        DELETE FROM coffee_menu
        WHERE name = %(name)s;
        """,
        {'name': del_product}
    )
    cur.close()
    conn.close()
    return menu
