user_one = {"name": "Winston Smith", "age": 39, "email": "wsmith@ingsoc.com"}
user_update = {"name": "Winston", "email": "winston@ingsoc.com", "is_online": True}

merge_dict = user_one | user_update
print(merge_dict)

"""
Salida:

{'name': 'Winston', 'age': 39, 'email': 'winston@ingsoc.com', 'is_online': True}
"""

user_one |= user_update
print(user_one)

"""
Salida:

{'name': 'Winston', 'age': 39, 'email': 'winston@ingsoc.com', 'is_online': True}
"""