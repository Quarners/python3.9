# news type hints native whithout  import  Dict or  List by typing


def print_content_list(costumers: list):
    for costumer in costumers:
        print(costumer)

def print_content_dict(costumer:dict):
    for key_costumer in costumer.keys():
        print(costumer[key_costumer])

print("Costumer List")
costumers = ["Mr. Andrew ng", "Jairo Pacheco", "Mr. Angel Diaz", "Carlos Antonio"]

print_content_list(costumers=costumers)

print()
print("Costumer Dict")

costumer_dict = {
    "name":"Andrew ng",
    "email":"andrewng@doamin.com",
    "age":40
}

print_content_dict(costumer=costumer_dict)