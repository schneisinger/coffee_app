"""Functions for making coffee"""
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")


    def is_resource_sufficient(self, order, menu):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in menu:
            if order == item["name"]:
                if self.resources["water"] < int(item["water"]):
                    can_make = False
                elif self.resources["milk"] < int(item["milk"]):
                    can_make = False
                elif self.resources["coffee"] < int(item["coffee"]):
                    can_make = False
                else:
                    return can_make


    def make_coffee(self, order, menu):
        """Deducts the required ingredients from the resources."""
        for item in menu:
            if order == item["name"]:
                self.resources["water"] -= int(item["water"])
                self.resources["milk"] -= int(item["milk"])
                self.resources["coffee"] -= int(item["coffee"])
                # print(f"Here is your {item['name']} ☕️. Enjoy!")

    # alt
    # def is_resource_sufficient(self, drink):
    # """Returns True when order can be made, False if ingredients are insufficient."""
    # can_make = True
    # for item in drink.ingredients:
    #     if drink.ingredients[item] > self.resources[item]:
    #         print(f"Sorry there is not enough {item}.")
    #         can_make = False
    # return can_make

    # def make_coffee(self, order):
    #     """Deducts the required ingredients from the resources."""
    #     for item in order.ingredients:
    #         self.resources[item] -= order.ingredients[item]
    #     print(f"Here is your {order.name} ☕️. Enjoy!")


    def refill(self, item, amount):
        """Takes item & amount as user input and adds to resources."""
        self.resources[item] += amount
