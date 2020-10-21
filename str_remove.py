name_costumers = []
costumers = ["Mr. Max Demian", "Jairo Castañeda"]

for costumer in costumers:
    name_costumers.append(costumer.removeprefix("Mr. "))

print(name_costumers)

"""
Salida

['Max Demian', 'Jairo Castañeda']
"""
