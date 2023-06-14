# """Functions for ingredients and the menu"""
# class MenuItem:
#     """Models each Menu Item."""
#     def __init__(self, name, water, milk, coffee, cost):
#         self.name = name
#         self.cost = cost
#         self.ingredients = {
#             "water": water,
#             "milk": milk,
#             "coffee": coffee
#         }


# class Menu:
#     """Models the Menu with drinks."""
#     def __init__(self, name, water, milk, coffee, cost):
#         self.menu = [
#             {name="latte", water=200, milk=150, coffee=24, cost=2.5},
#             {name="espresso", water=50, milk=0, coffee=18, cost=1.5},
#             {name="americano", water=125, milk=0, coffee=36, cost=2.25},
#             {name="cappuccino", water=75, milk=100, coffee=24, cost=3.75},
#         ]

#     def get_items(self):
#         """Returns all the names of the available menu items"""
#         options = {}
#         for item in self.menu:
#             options[item.name] = item.cost
#         return options

#     def find_drink(self, order_name):
#         """Searches menu for a drink by name. Returns that item if it exists, else returns None"""
#         for item in self.menu:
#             if item.name == order_name:
#                 return item
#         print("Sorry, that item is not available.")
