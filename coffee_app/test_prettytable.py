from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Bisasam", "Squirtle"])
table.add_column("Type", ["Electric", "Plant", "Water"])

table.align = "l"

print(table)

