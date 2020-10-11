costumers = ["Mr. Andrew ng", "Jairo Pacheco", "Mr. Angel Diaz", "Carlos Antonio"]

name_costumers = []
for costumer in costumers:

    name_costumers.append(costumer.removeprefix("Mr. "))


print(name_costumers)

"""
Result

['Andrew ng', 'Jairo Pacheco', 'Angel Diaz', 'Carlos Antonio']

"""
